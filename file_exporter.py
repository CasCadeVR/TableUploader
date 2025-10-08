import os

from datetime import datetime

from urllib.parse import urlparse

from typing import List
from typing import Dict

from contracts import FileExporterInterface

from logger_config import setup_logger

from data_processor import process_value

class FileExporter(FileExporterInterface):
    """<inheridoc see="FileExporterInterface">"""
    def __init__(self, output_dir: str = "."):
        self.output_dir = output_dir
        self.logger = setup_logger(__name__)

    def export(self, data: List[Dict], api_url: str) -> str:
        os.makedirs(self.output_dir, exist_ok=True)

        parsed_url = urlparse(api_url)
        api_method = os.path.splitext(os.path.basename(parsed_url.path))[0] or "api_data"
        current_date = datetime.now().strftime("%Y_%m_%d")
        filename = os.path.join(self.output_dir, f"{api_method}.{current_date}.txt")

        with open(filename, 'w', encoding='utf-8') as file:
            if not data:
                file.write("No data available\n")
                
            else:
                self._write_table(data, file)

        self.logger.info(f"Data exported to {filename}")
        return filename

    def _write_table(self, data: List[Dict], file):
        if not data:
            return

        headers = set()
        for item in data:
            headers.update(item.keys())
        headers = sorted(headers)

        column_widths = {}
        for header in headers:
            width = max(len(header), max(len(str(item.get(header, ""))) for item in data))
            column_widths[header] = width + 2

        header_row = "".join(h.ljust(column_widths[h]) for h in headers)
        separator = "".join("=" * column_widths[h] for h in headers)

        file.write(header_row + "\n")
        file.write(separator + "\n")

        for item in data:
            row = "".join(process_value(item.get(h, ""), h).ljust(column_widths[h]) for h in headers)
            file.write(row + "\n")
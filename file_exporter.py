import os
import re

from datetime import datetime

from urllib.parse import urlparse

from typing import List
from typing import Dict

from contracts import FileExporterInterface

from logger_config import setup_logger

from data_processor import process_value

def extract_method_name(url: str) -> str:
    parsed = urlparse(url)
    path_parts = [p for p in parsed.path.strip('/').split('/') if p]
    
    for part in reversed(path_parts):
        if part and part[0].isalpha():
            return part
        
    return "api_data"

def extract_version(url: str) -> str:
    match = re.search(r'/v(\d+)/', url)
    return f"v{match.group(1)}" if match else ""

class FileExporter(FileExporterInterface):
    """Экспортер файлов"""
    def __init__(self, output_dir: str = "."):
        """Инициализирует новый экземпляр"""
        self.output_dir = output_dir
        self.logger = setup_logger(__name__)

    def export(self, data: List[Dict], api_url: str) -> str:
        os.makedirs(self.output_dir, exist_ok=True)

        method_name = extract_method_name(api_url)
        version = extract_version(api_url)
        current_date = datetime.now().strftime("%Y_%m_%d")

        filename = f"{method_name}"
        
        if version:
            filename += f".{version}"
            
        filename += f".{current_date}.txt"
        filepath = os.path.join(self.output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as file:
            if not data:
                file.write("Нету данных для обработки\n")
                
            else:
                self._write_result_table(data, file)

        self.logger.info(f"Данные успешно экспортированы в {filepath}")
        return filepath

    def _write_result_table(self, data: List[Dict], file):
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

        header_row =  "|" + "".join(header.ljust(column_widths[header]) + "|" for header in headers)
        separator = "|" + "".join("=" * column_widths[header] + "|" for header in headers)

        file.write(header_row + "\n")
        file.write(separator + "\n")

        for item in data:
            row = "|" + "".join(process_value(item.get(header, ""), header).ljust(column_widths[header])+ "|" for header in headers)
            file.write(row + "\n")
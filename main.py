from api_client import ApiClient
from data_processor import DataProcessor
from file_exporter import FileExporter
from config import Config

def main():
    """Входная точка программы"""
    client = ApiClient(verify_ssl=Config.VERIFY_SSL)
    processor = DataProcessor()
    exporter = FileExporter(output_dir=Config.OUTPUT_DIR)

    data = client.fetch_data(Config.API_URL)
    processed_data = processor.process(data)
    exporter.export(processed_data, Config.API_URL)

if __name__ == "__main__":
    main()
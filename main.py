import asyncio
import argparse

from api_client import ApiClient

from data_processor import DataProcessor

from file_exporter import FileExporter

from config import Config

async def main():
    """Входная точка программы"""
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, default=Config.API_URL)
    args = parser.parse_args()
    
    api_url = args.url
    
    client = ApiClient(verify_ssl=Config.VERIFY_SSL)
    processor = DataProcessor()
    exporter = FileExporter(output_dir=Config.OUTPUT_DIR)

    try:
        data = await client.fetch_data(api_url)
        processed_data = processor.process(data)
        exporter.export(processed_data, api_url)
        
    except Exception as e:
        print(f"Ошибка при выполнении: {e}")


if __name__ == "__main__":
    asyncio.run(main())
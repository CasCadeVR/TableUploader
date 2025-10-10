import asyncio

from api_client import ApiClient

from data_processor import DataProcessor

from file_exporter import FileExporter

from config import Config

from logger_config import setup_logger

async def main():
    """Входная точка программы"""
    api_url="https://localhost:7258/Api/Works"
    
    logger = setup_logger(__name__)
    client = ApiClient(logger, verify_ssl=Config.VERIFY_SSL)
    processor = DataProcessor(logger)
    exporter = FileExporter(logger, output_dir=Config.OUTPUT_DIR)

    try:
        data = await client.fetch_data(api_url)
        processed_data = processor.process(data)
        exporter.export(processed_data, api_url)
        
    except Exception as e:
        logger.error(f"Ошибка при выполнении: {e}")

if __name__ == "__main__":
    asyncio.run(main())
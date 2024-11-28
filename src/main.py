from agent.exchange_client import ExchangeClient
from agent.email_processor import EmailProcessor
from agent.knowledge_base import KnowledgeBase
from config import Config
from utils.logger import setup_logger

def main():
    logger = setup_logger()
    logger.info("Starting the Exchange Knowledge Agent")

    # Initialize components
    config = Config()
    knowledge_base = KnowledgeBase()
    exchange_client = ExchangeClient(config)
    email_processor = EmailProcessor(knowledge_base)

    # Main processing loop
    emails = exchange_client.fetch_new_emails()
    for email in emails:
        processed_data = email_processor.process(email)
        knowledge_base.store(processed_data)

if __name__ == "__main__":
    main() 
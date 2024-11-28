from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        load_dotenv()
        
        self.exchange_email = os.getenv("EXCHANGE_EMAIL")
        self.exchange_password = os.getenv("EXCHANGE_PASSWORD")
        self.exchange_server = os.getenv("EXCHANGE_SERVER") 
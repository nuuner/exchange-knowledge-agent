from dataclasses import dataclass
from datetime import datetime

@dataclass
class EmailData:
    subject: str
    sender: str
    received_time: datetime
    content: str
    processed_content: dict 
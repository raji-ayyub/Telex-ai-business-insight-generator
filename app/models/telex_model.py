from pydantic import BaseModel
from typing import Optional

class TelexMessage(BaseModel):
    text: str
    sender: str
    timestamp: Optional[str] = None

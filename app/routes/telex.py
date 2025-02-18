from fastapi import APIRouter
from app.database.mongodb import messages_collection
from app.services.telex_service import process_telex_message
from app.models.telex_model import TelexMessage

router = APIRouter()

@router.post("/receive-message/")
async def receive_message(payload: TelexMessage):
    """Receives messages from Telex and processes them"""
    messages_collection.insert_one(payload.dict())  # Store raw message
    response = process_telex_message(payload.dict())
    return {"status": "Message received", "response": response}

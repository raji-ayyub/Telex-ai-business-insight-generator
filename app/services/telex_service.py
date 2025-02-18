import datetime
from app.database.mongodb import reports_collection

def process_telex_message(payload: dict):
    """Process incoming Telex messages and generate AI reports."""
    message_text = payload.get("text", "")
    sender = payload.get("sender", "Unknown")
    
    # Generate an AI summary (for now, just a placeholder)
    summary = f"Summary: Received message from {sender}: {message_text[:50]}..."
    
    report_data = {
        "original_message": message_text,
        "summary": summary,
        "created_at": datetime.datetime.utcnow(),
    }
    
    reports_collection.insert_one(report_data)
    return summary

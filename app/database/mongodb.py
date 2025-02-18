from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

MONGO_URI = os.getenv("MONGO_URI")  # MongoDB connection string
DB_NAME = "telex_reports"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

messages_collection = db["messages"]
reports_collection = db["reports"]

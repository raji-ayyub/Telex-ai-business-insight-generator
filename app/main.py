from fastapi import FastAPI
from app.routes.telex import router as telex_router

app = FastAPI(title="AI Business Insights Reporter")

# Include routes
app.include_router(telex_router)

@app.get("/")
def home():
    return {"message": "AI Insights Reporter is running!"}

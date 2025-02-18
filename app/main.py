from fastapi import FastAPI
from app.routes.telex import router as telex_router

import uvicorn
from app.main import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

    
app = FastAPI(title="AI Business Insights Reporter")

# Include routes
app.include_router(telex_router)

@app.get("/")
def home():
    return {"message": "AI Insights Reporter is running!"}

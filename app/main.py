# import fastAPI
from fastapi import FastAPI

# create an instance of the FastAPI class
app = FastAPI(
    title="Text Analyzer API",
    description="Microservice API for analyzing text",
    version="1.0.0"
)

# create route health, verify if the API is working
@app.get("/health")
async def health_check():
    return {"status": "ok"}
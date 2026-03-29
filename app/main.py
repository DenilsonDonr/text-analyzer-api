# import fastAPI
from fastapi import FastAPI

# import the analysis router
from app.routers import analysis

# create an instance of the FastAPI class
app = FastAPI(
    title="Text Analyzer API",
    description="Microservice API for analyzing text",
    version="1.0.0"
)

# include the analysis router in the main app
app.include_router(analysis.router)

# create route health, verify if the API is working
@app.get("/health")
async def health_check():
    return {"status": "ok"}
# Import API router and HTTPException from FastAPI
from fastapi import APIRouter, HTTPException

# Import eschemas and services
from app.schemas.text import TextRequest, TextResponse
from app.services.analyzer import analyze_text

# Create an API router instance
router = APIRouter(prefix="/analysis", tags=["analysis"])

@router.post("/", response_model=TextResponse)
async def analyze(request: TextRequest) -> TextResponse:
    try:
        # call the analyze_text function from the services
        result = analyze_text(request.text)
        return TextResponse(**result) # unpacking of dictionary to match the TextResponse model
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))
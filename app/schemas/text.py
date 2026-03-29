# import baseModel and field from pydantic
from pydantic import BaseModel, field_validator

# define a class TextRequest that inherits from BaseModel
class TextRequest(BaseModel):
    text: str
    
    # validate that the text is not empty and has at least 10 characters
    @field_validator('text')
    @classmethod
    def text_not_empty(cls, v: str) -> str:
        stripped = v.strip()
        
        if not stripped:
            raise ValueError("The text cannot be empty")
        if len(stripped) < 10:
            raise ValueError("The text must have at least 10 characters")
        
        return stripped

# define a class TextResponse that inherits from BaseModel
class TextResponse(BaseModel):
    text: str
    language: str
    language_confidence: str
    character_count: int
    word_count: int
    
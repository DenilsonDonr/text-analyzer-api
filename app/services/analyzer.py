# import detect, detect_langs, langDetectException and TypedDict
from typing import TypedDict
from langdetect import detect, detect_langs  # type: ignore
from langdetect.lang_detect_exception import LangDetectException  # type: ignore


# Necessary to define the return type of the analyze_text function
class AnalysisResult(TypedDict):
    text: str
    language: str
    language_confidence: str
    character_count: int
    word_count: int


# Analyz text and return the text, the language, confidence, character count and word count
def analyze_text(text: str) -> AnalysisResult:
    
    language: str
    confidence: str
    
    try:
        language = detect(text)  # type: ignore
        langs = detect_langs(text)  # type: ignore
        confidence = f"{langs[0].prob:.0%}"  # type: ignore
    except LangDetectException:
        language = "unknown"
        confidence = "0%"
    
    return {
        "text": text,
        "language": language,
        "language_confidence": confidence,
        "character_count": len(text),
        "word_count": len(text.split())
    }
# import TestClient from fastapi.testclient and app from main
from fastapi.testclient import TestClient
from app.main import app

# create an instance of TestClient with the app
client = TestClient(app)

def test_analyze_text_empty():
    text = ""
    response = client.post("/analysis", json={"text": text})
    assert response.status_code == 422
    
def test_analyze_text_valid():
    text = "Hi, I'm good. How are you doing today?"
    response = client.post("/analysis", json={"text": text})
    assert response.status_code == 200
    
def test_analyze_text_word_count():
    text = "Hi, I'm good. How are you doing today?"
    response = client.post("/analysis", json={"text": text})
    assert response.status_code == 200
    data = response.json()
    assert data["word_count"] == 8
    
def test_analyze_text_character_count():
    text = "Hi, I'm good. How are you doing today?"
    response = client.post("/analysis", json={"text": text})
    assert response.status_code == 200
    data = response.json()
    assert data["character_count"] == 38
    
def test_analyze_text_inglish():
    text = "Hi, Good morning!"
    response = client.post("/analysis", json={"text": text})
    assert response.status_code == 200
    data = response.json()
    assert data["language"] == "en"
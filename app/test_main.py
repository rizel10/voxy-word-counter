from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_count_words():
    response = client.post(  
        "/", 
        data={"content": "   texto de cinco palavras hehe    "},
        headers={ 'Content-Type': 'application/x-www-form-urlencoded'}
    )
    assert response.json() == 5
    assert response.status_code == 200

def test_empty_text_error():
    response = client.post(  
        "/", 
        data={"content": ""},
        headers={ 'Content-Type': 'application/x-www-form-urlencoded'}
    )
    assert response.status_code == 422


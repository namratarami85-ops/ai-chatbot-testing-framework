from app.main import get_mock_ai_response

def test_capital_of_france():
    response = get_mock_ai_response("What is the capital of France?")
    assert response == "Paris"

def test_hamlet_author():
    response = get_mock_ai_response("Who wrote Hamlet?")
    assert response == "William Shakespeare"

def test_basic_math():
    response = get_mock_ai_response("What is 2 + 2?")
    assert response == "4"

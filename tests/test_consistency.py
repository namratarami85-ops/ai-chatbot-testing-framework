from app.main import get_mock_ai_response

def test_same_prompt_returns_same_response():
    prompt = "What is the capital of France?"
    response_1 = get_mock_ai_response(prompt)
    response_2 = get_mock_ai_response(prompt)
    assert response_1 == response_2 == "Paris"

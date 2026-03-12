from app.main import get_mock_ai_response

def test_unknown_question_should_not_fake_answer():
    response = get_mock_ai_response("Who is the president of Mars?")
    assert response == "I am not sure."

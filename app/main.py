def get_mock_ai_response(prompt: str) -> str:
    mock_responses = {
        "What is the capital of France?": "Paris",
        "Who wrote Hamlet?": "William Shakespeare",
        "What is 2 + 2?": "4"
    }
    return mock_responses.get(prompt, "I am not sure.")

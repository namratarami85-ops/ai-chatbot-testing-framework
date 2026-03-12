import csv
from app.main import get_mock_ai_response

def test_dataset_prompts():
    with open("data/test_prompts.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            prompt = row["prompt"]
            expected = row["expected_answer"]
            response = get_mock_ai_response(prompt)
            assert response == expected

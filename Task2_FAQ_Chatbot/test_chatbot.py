from app import get_response

TEST_QUESTIONS = [
    "How many projects do I need to finish?",
    "Where can I submit my code?",
    "Can I get a certificate?",
    "Tell me about cooking recipes",
]

for question in TEST_QUESTIONS:
    result = get_response(question)
    print(f"Q: {question}")
    print(f"Matched FAQ: {result['matched_question']}")
    print(f"Similarity: {result['score']}")
    print(f"A: {result['answer']}\n")

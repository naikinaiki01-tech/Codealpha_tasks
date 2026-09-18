# CodeAlpha Task 2 — FAQ Chatbot

A complete NLP-based FAQ chatbot for the CodeAlpha AI internship. The application cleans questions, converts FAQ text into TF-IDF vectors, calculates cosine similarity, and returns the closest answer through a simple web chat interface.

## Features

| Requirement | Implementation |
|---|---|
| Collect FAQs | `FAQS` list in `app.py` |
| Text preprocessing | Lowercasing, punctuation removal, whitespace normalization |
| NLP matching | TF-IDF vectorization with unigrams and bigrams |
| Similarity | Cosine similarity |
| Best answer | Highest-scoring FAQ response |
| Chat UI | Flask + HTML/CSS/JavaScript |
| Unknown question handling | Confidence threshold and fallback response |

## Run locally

```bash
python -m venv venv
# Windows: venv\\Scripts\\activate
# Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in a browser.

## How the NLP works

1. The FAQ questions are cleaned with `clean_text()`.
2. `TfidfVectorizer` converts the cleaned questions into numerical vectors.
3. The user's question is converted using the same vectorizer.
4. `cosine_similarity()` compares the query vector with every FAQ vector.
5. The answer with the highest similarity is returned if the score is at least `0.16`; otherwise, the chatbot asks the user to try another topic.

## Viva explanation

**Why TF-IDF?** It gives higher importance to words that distinguish one FAQ from the others. **Why cosine similarity?** It measures how closely the question vectors point in the same direction, which works well for short text matching. **Why a threshold?** It prevents the chatbot from returning an unrelated answer when the question does not belong to the FAQ dataset.

## Example API response

```json
{
  "answer": "You must complete at least two tasks. Completing three tasks is also acceptable.",
  "matched_question": "How many tasks must I complete?",
  "score": 0.816
}
```

## Suggested GitHub repository name

`CodeAlpha_FAQ_Chatbot`

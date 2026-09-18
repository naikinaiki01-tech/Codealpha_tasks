from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

app = Flask(__name__)

FAQS = [
    {"question": "What is CodeAlpha?", "answer": "CodeAlpha is a software development company that offers internship opportunities in emerging technologies."},
    {"question": "How do I apply for the internship?", "answer": "You can apply through the official CodeAlpha application or communication channel shared by the program coordinators."},
    {"question": "What tasks are available in the AI internship?", "answer": "The AI task list includes a language translation tool, FAQ chatbot, music generation with AI, and object detection and tracking."},
    {"question": "How many tasks or projects must I complete?", "answer": "You must complete at least two tasks. Completing three tasks is also acceptable."},
    {"question": "How many tasks or projects do I need to finish?", "answer": "You must complete at least two tasks. Completing three tasks is also acceptable."},
    {"question": "Where should I upload my source code?", "answer": "Upload your complete source code to GitHub in a repository named CodeAlpha_ProjectName."},
    {"question": "Do I need to share my internship status?", "answer": "Yes. Share your internship status on LinkedIn and tag CodeAlpha."},
    {"question": "Will I receive a certificate?", "answer": "Eligible interns may receive a completion certificate with QR verification and a unique ID certificate."},
    {"question": "What is Task 2?", "answer": "Task 2 is an FAQ chatbot. It preprocesses questions, finds the most similar FAQ using NLP, and displays the best matching answer."},
    {"question": "What NLP technique is used in this chatbot?", "answer": "This chatbot cleans text, converts it into TF-IDF vectors, and uses cosine similarity to match a user's question with the closest FAQ."},
    {"question": "How can I contact CodeAlpha?", "answer": "You can visit www.codealpha.tech or contact the program team through the official WhatsApp and email details provided in the internship document."},
]

def clean_text(text: str) -> str:
    """Lowercase text, remove punctuation, and normalize whitespace."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()

questions = [faq["question"] for faq in FAQS]
vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
faq_matrix = vectorizer.fit_transform([clean_text(q) for q in questions])


def get_response(user_question: str):
    cleaned = clean_text(user_question)
    if not cleaned:
        return {"answer": "Please type a question so I can help you.", "score": 0, "matched_question": None}

    query_vector = vectorizer.transform([cleaned])
    scores = cosine_similarity(query_vector, faq_matrix)[0]
    best_index = scores.argmax()
    best_score = float(scores[best_index])
    threshold = 0.16

    if best_score < threshold:
        return {
            "answer": "Sorry, I could not find a close FAQ match. Try asking about tasks, certificates, GitHub, or internship requirements.",
            "score": round(best_score, 3),
            "matched_question": None,
        }

    return {
        "answer": FAQS[best_index]["answer"],
        "score": round(best_score, 3),
        "matched_question": FAQS[best_index]["question"],
    }

@app.route("/")
def home():
    return render_template("index.html", faqs=FAQS)

@app.post("/ask")
def ask():
    data = request.get_json(silent=True) or {}
    question = str(data.get("question", ""))
    return jsonify(get_response(question))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

# Example questions for testing:
# python -c "from app import get_response; print(get_response('How many projects do I need?'))"
# python -c "from app import get_response; print(get_response('Where do I submit code?'))"
# python -c "from app import get_response; print(get_response('Tell me about cooking'))"

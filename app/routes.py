from flask import Blueprint, render_template, request
from app.preprocess import clean_text, load_vectorizer
from app.model import load_model, predict

bp = Blueprint('main', __name__)

model = load_model()
vectorizer = load_vectorizer()

@bp.route('/')
def index():
    return render_template("index.html")

@bp.route('/predict', methods=['POST'])
def predict_news():
    news_text = request.form['news']
    cleaned = clean_text(news_text)
    label = predict(cleaned, model, vectorizer)
    result = "Fake News" if label == 1 else "Real News"
    return render_template("result.html", prediction=result)

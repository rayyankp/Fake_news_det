import re
import pickle

def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z]", " ", text)
    text = text.lower()
    return text

def load_vectorizer():
    with open("vectorizer.pkl", "rb") as f:
        return pickle.load(f)

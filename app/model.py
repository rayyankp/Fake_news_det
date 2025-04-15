import pickle

def load_model():
    with open("fake_news_model.pkl", "rb") as f:
        return pickle.load(f)

def predict(text, model, vectorizer):
    vector = vectorizer.transform([text])
    return model.predict(vector)[0]

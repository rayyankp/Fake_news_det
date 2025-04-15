import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Load data
fake_df = pd.read_csv('data/Fake.csv')
real_df = pd.read_csv('data/True.csv')

# Label them
fake_df['label'] = 1
real_df['label'] = 0

# Combine and clean
df = pd.concat([fake_df, real_df])
df['text'] = df['text'].str.lower().str.replace(r'[^a-z\s]', '', regex=True)

X = df['text']
y = df['label']

# Vectorize
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_vect = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
with open('fake_news_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("Model and vectorizer saved.")

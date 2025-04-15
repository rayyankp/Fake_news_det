📰 Fake News Detector
This project is a machine learning-based web application that classifies news as Fake or Real using Natural Language Processing (NLP) techniques. Built using Python, Flask, and Scikit-learn, the app allows users to input news content and receive instant predictions.

🔧 Features
Preprocessing of text data (removal of punctuation, stopwords, etc.)

Model training using classical ML algorithms

Vectorization using TF-IDF

Web interface to input news and display results

Reusable and modular code structure

🗂 Project Structure
graphql
Copy
Edit
.
├── app/
│   ├── _init_.py           # App initialization
│   ├── model.py              # ML model loading logic
│   ├── preprocess.py         # Text preprocessing functions
│   ├── routes.py             # Flask routes
│   ├── train_model.py        # Model training script
│
├── data/
│   ├── Fake.csv              # Dataset with fake news
│   ├── True.csv              # Dataset with real news
│
├── templates/
│   ├── index.html            # Form to enter news
│   ├── result.html           # Display result
│
├── venv/                     # Virtual environment
├── .venv/                    # Virtual environment (editor-specific)
├── main.py                   # Flask entry point
├── fake_news_model.pkl       # Trained model
├── vectorizer.pkl            # TF-IDF vectorizer
├── requirements.txt          # Python dependencies
└── README.md                 # Project overview
🚀 Getting Started
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector
2. Create & activate virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Train the model (optional)
bash
Copy
Edit
python app/train_model.py
5. Run the app
bash
Copy
Edit
python main.py
Then open http://127.0.0.1:5000 in your browser.

📊 Model
Algorithm: Logistic Regression / Naive Bayes (depending on what’s implemented)

Vectorization: TF-IDF

Training Data: Fake.csv and True.csv

🧹 Preprocessing Steps
Lowercasing

Removing punctuation

Removing stopwords

Lemmatization or stemming (if applied)

🖥 UI Screens
index.html: News submission form

result.html: Displays prediction result

📦 Dependencies
See requirements.txt. Major libraries:

Flask

Scikit-learn

Pandas

NLTK

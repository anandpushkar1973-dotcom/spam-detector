from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

texts = [
    "win money now",
    "free prize win",
    "hello friend",
    "how are you",
    "click this link",
    "earn cash fast"
]

labels = [1, 1, 0, 0, 1, 1]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
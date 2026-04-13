import re

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)

    words = text.split()

    stopwords = ["is", "the", "and", "a", "to", "you", "for", "on"]

    filtered = [word for word in words if word not in stopwords]

    return " ".join(filtered)
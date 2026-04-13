from flask import Flask, render_template, request, jsonify
import pickle
from preprocessing import preprocess

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']

    processed = preprocess(text)
    vector = vectorizer.transform([processed])

    prediction = model.predict(vector)[0]

    if prediction == 1:
        result = "Spam ❌"
    else:
        result = "Not Spam ✅"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
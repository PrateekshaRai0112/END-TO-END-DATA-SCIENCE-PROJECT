from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model1.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = model.predict([features])[0]
    iris_classes = ['Setosa', 'Versicolor', 'Virginica']
    result = iris_classes[prediction]
    return render_template("index.html", prediction_text=f"Predicted Species: {result}")

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize Flask app and model
app = Flask(__name__)
classifier = pipeline("sentiment-analysis")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        text = data.get("text", "")
        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Make predictions
        result = classifier(text)
        return jsonify({"predictions": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

"""Launch Flask application"""
# Import libraries
import logging
from flask.logging import create_logger
from flask import Flask, request, jsonify

from utils.data import CarFeatures
from utils.mllib import UsedCarPriceModel

# Lauch & Set-up application
app = Flask(__name__)

model = UsedCarPriceModel()

LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route("/")
def home():
    html = "<h3>Predict the Price for a used cars</h3>"
    return html.format(format)

@app.route("/predict", methods=['POST'])
def predict():
    """Predicts Price for a used cars."""
    # Get data from POST requests
    json_payload = request.json
    LOG.info(f"JSON payload: {json_payload}")

    # Predict
    car = CarFeatures(json_payload)
    prediction = model.predict(car)
    print(prediction)
    return jsonify(prediction)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
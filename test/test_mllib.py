""" Test ML library
Tests most of the functions & class necessary to train/predict data
"""
# Import libraries
import math
from utils.data import CarFeatures
from utils.mllib import UsedCarPriceModel


# Load persisted model
model = UsedCarPriceModel()


# Test scoring method
def test_squared_score():
    score = model.score([1, 0, 1, 0], [1, 0, 0, 1])
    assert score == 0.5


def test_score():
    score = model.score([1, 0, 1, 0], [1, 0, 0, 1], squared=False)
    assert score == math.sqrt(0.5)


# Test model
def test_predict():
    # Features of a car
    features = {
        "model": "A1",
        "year": 2017,
        "transmission": "Manual",
        "mileage": 15735,
        "fuelType": "Petrol",
        "tax": 150,
        "mpg": 55.4,
        "engineSize": 1.4,
        "manufacter": "Audi",
    }
    
    # Result
    result = {
        "Prediction": -0.24357285015756264,
        "Unscaled prediction": 14402.081648257788
    }

    car = CarFeatures(features)
    prediction = model.predict(car)
    assert prediction == result

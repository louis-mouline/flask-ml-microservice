""" Test ML library
Tests most of the functions & class necessary to train/predict data
"""
# Import libraries
import math
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

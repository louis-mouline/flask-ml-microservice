""" Test Data Handling library
Tests most of the functions & class necessary to ingest data
"""

# Import library
from dataclasses import asdict
from utils.data import CarFeatures, load_data


def test_ingest():
    """Test class initialization."""
    # Tested feature
    features = {'model': 'A1', 
                'year': 2017, 
                'transmission': 'Manual', 
                'mileage': 15735, 
                'fuelType': 'Petrol', 
                'tax': 150, 
                'mpg': 55.4, 
                'engineSize': 1.4, 
                'manufacter': 'Audi'}
    
    car = CarFeatures(features)

    features['registrationAge'] = 4

    assert asdict(car) == features


def test_load():
    """Test loading data from .csv."""
    used_vehicles = load_data()
    columns = ['model', 'year', 'price', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize', 'manufacter']

    assert list(used_vehicles.columns) == columns

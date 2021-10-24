""" Data Handling library
Defines all functions & class necessary to ingest data
"""
# Import libraries
import pandas as pd
from dataclasses import dataclass, field


# Define Car features
@dataclass(repr=True)
class CarFeatures():
    """Class holder of car features object."""
    # Initialized attributes
    model: str
    year: int
    transmission: str
    mileage: int
    fuelType: str
    tax: int
    mpg: float
    engineSize: float
    manufacter: str

    # Genreated attribute
    registrationAge: int

    def __init__(self, features: dict, current_year: int=2021) -> None:
        for feature_name, feature_value in features.items():
            setattr(self, feature_name, feature_value)
        self.registrationAge = current_year - self.year


# Define util function to load data
def load_data(data_path: str='./data/used_vehicles.csv') -> pd.DataFrame:
    """Load .csv dataset into a pandas.DataFrame"""
    df = pd.read_csv(data_path)
    return df

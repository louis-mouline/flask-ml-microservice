""" MLOps Library 
Define all functions used to predict & retrain the model
"""
# Import libraries
import joblib
import logging
import numpy as np
import pandas as pd
from dataclasses import asdict
from utils.data import CarFeatures, load_data

# Import ML libraries
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Ignore warnings
import warnings

warnings.filterwarnings("ignore", category=UserWarning)


# Start logging function
logging.basicConfig(level=logging.INFO)


class UsedCarPriceModel:
    """Class holder for the model."""

    def __init__(
        self,
        model_path: str = "./data/model.zlib",
        target_scaler_path: str = "./data/target_scaler.zlib",
    ) -> None:
        # Load model from disk
        with open(model_path, "rb") as file:
            self.model = joblib.load(file)
        # Load target scaler from disk
        with open(target_scaler_path, "rb") as file:
            self.target_scaler = joblib.load(target_scaler_path)

        logging.debug(f"Model loaded from {model_path} & {target_scaler_path}")

    def fit(
        self,
        data_path: str = "./data/used_vehicles.csv",
        current_year: int = 2021,
        test_size: float = 0.2,
        random_state: int = 0,
        suffle: bool = True,
        squared: bool = True,
        parameters: dict = None,
        model_path: str = "./data/model.zlib",
        target_scaler_path: str = "./data/target_scaler.zlib",
    ) -> None:
        """Retrain the model.
        See the notebook Used_Car_Price_Prediction.ipynb
        """
        # Load data
        used_vehicles = load_data(data_path)

        # Transform data
        X, y = self.transform(used_vehicles, current_year)
        y_scaler = self.target_scaler.fit(y)
        y_scaled = y_scaler.transform(y)

        # Split dataset into training/test sets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y_scaled, test_size=test_size, random_state=random_state, shuffle=suffle
        )

        # Set parameters
        if not parameters == None:
            logging.debug(f"Set following parameters for the model: {parameters}")
            self.model.set_params(parameters)

        # Fit the model
        self.model.fit(X_train, y_train)

        # Show model metric
        pred_train = self.model.predict(X_train)
        pred_test = self.model.predict(X_test)

        metric = "MSE" if squared else "RMSE"
        model_score = {
            f"{metric} (training)": self.score(y_train, pred_train, squared=squared),
            f"{metric} (test)": self.score(y_test, pred_test, squared=squared),
        }

        logging.debug(f"Model score: {model_score}")

        self.save(model_path, target_scaler_path)

    def predict(self, car: CarFeatures) -> dict:
        """Predict the price for a car."""
        # Transform data
        cars_df = pd.DataFrame(data=asdict(car), index=[0])
        cars_df.drop(columns=["year"], inplace=True)

        prediction = self.model.predict(cars_df)
        prediction = prediction.reshape(-1, 1)
        prediction_unscaled = self.target_scaler.inverse_transform(prediction)

        logging.debug(f"Prediction for {car}")

        return {"Prediction": prediction[0][0], "Unscaled prediction": prediction_unscaled[0][0]}

    def save(
        self,
        model_path: str = "./data/model.zlib",
        target_scaler_path: str = "./data/target_scaler.zlib",
    ) -> None:
        """Persist the model."""
        # Persist model to disk
        with open(model_path, "wb") as file:
            joblib.dump(self.model, file)
        # Persist target scaler to disk
        with open(target_scaler_path, "wb") as file:
            joblib.dump(self.target_scaler, file)

        logging.debug(f"Model saved to {model_path} & {target_scaler_path}")

    @staticmethod
    def transform(
        data: pd.DataFrame, current_year: int = 2021
    ) -> tuple((pd.DataFrame, np.ndarray)):
        """Clean & Preprocess the database.
        See Used_Car_Price_Prediction.ipynb"""
        # Correct manufacter value
        data["manufacter"].replace(
            {
                "audi": "Audi",
                "bmw": "BMW",
                "ford": "Ford",
                "hyundi": "Hyundai",
                "merc": "Mercedes",
                "skoda": "Skoda",
                "toyota": "Toyota",
                "vauxhall": "Vauxhall",
                "vw": "Volkswagen",
            },
            inplace=True,
        )

        # Strip model of the vehicle
        data["model"] = data["model"].str.strip()

        # Replace year 2060 by 2010
        data.loc[data.year == 2060, "year"] = 2010

        # Transform year column to registration age
        data["registrationAge"] = current_year - data["year"]
        data.drop(columns=["year"], inplace=True)

        # Split features/target
        X = data.loc[:, data.columns != "price"]
        y = data["price"]

        logging.debug({"Features shape": X.shape, "Target shape": y.shape})

        # Reshape values
        y = y.values.reshape(-1, 1)

        return X, y

    @staticmethod
    def score(y_true, y_pred, squared=True) -> float:
        """Compute the RMSE/MSE"""
        return mean_squared_error(y_true, y_pred, squared=squared)

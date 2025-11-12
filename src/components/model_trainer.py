import os
import sys
from dataclasses import dataclass
import numpy as np
from sklearn.metrics import r2_score
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from catboost import CatBoostRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainerConfig:
    train_model_file_path = os.path.join('artifacts', 'model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_arr, test_arr):
        try:
            logging.info("Splitting training and testing data")

            X_train, y_train = train_arr[:, :-1], train_arr[:, -1]
            X_test, y_test = test_arr[:, :-1], test_arr[:, -1]

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "KNN Regressor": KNeighborsRegressor(),
                "XGBoost Regressor": XGBRegressor(),
                "CatBoost Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            model_report = evaluate_models(
                X_train = X_train, y_train=y_train,
                X_test = X_test, y_test = y_test, models= models
            )

            best_model_score = max(model_report.values())
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            logging.info(f"Best model found: {best_model_name} with R2 score: {best_model_score}")

            if best_model_score < 0.6:
                raise CustomException("No good model found! Performance too low.")

            # TRAIN the best model
            best_model.fit(X_train, y_train)

            save_object(
                file_path=self.model_trainer_config.train_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)
            r2 = r2_score(y_test, predicted)

            logging.info(f"Model Trainer Completed. R2 Score: {r2}")
            return r2

        except Exception as e:
            raise CustomException(e, sys)

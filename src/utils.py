import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException
from src.logger import logging

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models: dict):
    """
    Trains each model in `models` (a dict name -> estimator),
    evaluates on test set using R2, and returns a dict:
      { model_name: test_r2_score }
    """
    try:
        report = {}
        for name, model in models.items():
            logging.info(f"Training model: {name}")
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            logging.info(f"{name} → Train R2: {train_model_score:.4f}, Test R2: {test_model_score:.4f}")
            report[name] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)


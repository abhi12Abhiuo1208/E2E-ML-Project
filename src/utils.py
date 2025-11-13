# src/utils.py
import os
import sys
import logging
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        # use dill for robustness (can handle more python objects)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models: dict, params: dict):
    """
    Trains each model in `models` (dict name->estimator) using the corresponding
    param grid in `params` (dict name->param_grid). Returns dict of {name: test_r2}.
    """
    try:
        report = {}
        for name, model in models.items():
            logging.info(f"Started training model: {name}")

            # get param grid for this model (may be empty or not provided)
            param_grid = params.get(name, None)

            if param_grid and len(param_grid) > 0:
                logging.info(f"Running GridSearchCV for {name} with params: {param_grid}")
                gs = GridSearchCV(model, param_grid, cv=3, n_jobs=-1, verbose=0)
                gs.fit(X_train, y_train)
                best_params = gs.best_params_
                logging.info(f"Best params for {name}: {best_params}")
                model.set_params(**best_params)
            else:
                logging.info(f"No param grid for {name} - training with default params")

            # train the (possibly tuned) model
            model.fit(X_train, y_train)

            # predictions & scoring
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_score = r2_score(y_train, y_train_pred)
            test_score = r2_score(y_test, y_test_pred)

            logging.info(f"{name} -> train R2: {train_score:.4f}, test R2: {test_score:.4f}")

            report[name] = test_score

        return report

    except Exception as e:
        raise CustomException(e, sys)

    
# def load_object(file_path):
#     try:
#         with open(file_path, "rb") as file_obj:
#             return pickle.load(file_obj)

#     except Exception as e:
#         raise CustomException(e, sys)

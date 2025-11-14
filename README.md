🎓 Student Exam Performance Prediction
End-to-End Machine Learning Project with CI/CD & Flask Deployment

This project predicts a student’s Math Score based on demographic & academic attributes using a complete ML pipeline — including data ingestion → transformation → model training → hyperparameter tuning → prediction pipeline → Flask web app.

📌 Project Structure
├── artifacts/
│   ├── train.csv
│   ├── test.csv
│   ├── data.csv
│   ├── preprocessor.pkl
│   ├── model.pkl
│
├── notebooks/
│   └── dataset/
│       └── stud.csv
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── predict_pipeline.py
│   │   └── __init__.py
│   │
│   ├── exception.py
│   ├── logger.py
│   ├── utils.py
│
├── templates/
│   ├── index.html
│   └── home.html
│
├── app.py
└── README.md

🚀 Features
✔ End-to-End Pipeline

Data ingestion (load + train-test split)

Data preprocessing (imputation, scaling, encoding)

Model building (7 ML models tested)

Hyperparameter tuning using GridSearchCV

Best-model selection using R² score

Model and preprocessor saving using pickle/dill

Prediction pipeline for new unseen data

✔ Flask Web APP

User-friendly HTML form

Accepts categorical & numerical features

Sends input → preprocess → ML model → predicted score

Displays final predicted Math score on UI

✔ Error Handling + Logging

Centralized custom exception handling

Logging for debugging & monitoring

📊 Models Used
Algorithm	Tuned?	Notes
Random Forest	✔	Best performing in most cases
Gradient Boosting	✔	Robust for tabular data
XGBoost	✔	High performance model
CatBoost	✔	Handles categorical data well
Decision Tree	✔	Baseline
Linear Regression	—	Simple baseline
AdaBoost	✔	Boosted performance

GridSearchCV selects the best model based on test R² score.

🧠 Key Learnings / Problems Solved
🔹 1. ModuleNotFoundError (src not found)

Solved by running scripts as modules:

python -m src.components.data_ingestion

🔹 2. ValueError: Too many values to unpack

Fixed by aligning return structure of data transformation.

🔹 3. dill / pickle errors

Installed dill and updated save/load functions.

🔹 4. Wrong column names (race_ethinicity vs race_ethnicity)

Synced column names between dataset, transformation, and UI.

🔹 5. HTML → Flask mapping mismatch

Corrected naming to ensure form → backend → pipeline worked smoothly.

🔹 6. Virtual environment issues

Created stable venv:

python -m venv projenv
projenv\Scripts\activate
pip install flask scikit-learn xgboost catboost dill

🖥 Run Locally
1️⃣ Create virtual environment
python -m venv projenv
projenv\Scripts\activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Train the model
python -m src.components.data_ingestion

4️⃣ Run the Flask app
python app.py


Open browser:
➡ http://127.0.0.1:5000/

🧪 Make Predictions

Fill details in the UI:

Gender

Ethnicity

Parent Education

Lunch

Test Preparation

Reading Score

Writing Score

Click → Predict your Math Score

# TrafficFlowPrediction

#📁 Project Overview
This project aims to predict hourly traffic volume on a highway using historical data, weather conditions, and time-based features. It uses a machine learning regression model to forecast traffic volume and includes data preprocessing, model training, prediction, and visualization.

#📦Dependencies
Install dependencies using:
pip install -r requirements.txt

#📊Dataset Description
Key Features:
date_time: Timestamp of observation
traffic_volume: Number of cars passing through
temp, rain_1h, snow_1h: Weather metrics
clouds_all: Cloud coverage
holiday: Holiday indicator

#🧹Data Preprocessing (preprocess.py)
Converts date_time to datetime format
Extracts hour, dayofweek, and month
Selects relevant features
Drops missing values

#🧠Model Training (train_model.py)
Loads preprocessed data
Splits into training and testing sets
Trains a RandomForestRegressor
Evaluates using Mean Absolute Error (MAE)
Saves model as traffic_model.pkl

#🔮Prediction (predict.py)
Loads saved model
Accepts input features (hour, dayofweek, month, temp, rain, snow)
Outputs predicted traffic volume.

#🚀How to Run in IntelliJ
Open IntelliJ IDEA and create a Python project.
Add the folder structure and files.
Install dependencies via terminal.
Run train_model.py to train and save the model.
Run predict.py to test predictions.

#✅Future Improvements
Use advanced models like XGBoost or LSTM
Add holiday and weather condition encoding
Build a Streamlit dashboard for interactive predictions

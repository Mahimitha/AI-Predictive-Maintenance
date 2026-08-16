# AI Predictive Maintenance System

## Project Overview

The AI Predictive Maintenance System is a machine learning project designed to predict the Remaining Useful Life (RUL) of aircraft engines and identify their health condition before failure.

The project uses the NASA C-MAPSS FD004 dataset, which contains multivariate time-series data from aircraft engine simulations. An XGBoost machine learning model is used to predict the remaining operational cycles of each engine.

A Streamlit dashboard is developed to display the predicted RUL, machine health status, degradation indicators, and maintenance recommendations.

## Objectives

- Predict the Remaining Useful Life (RUL) of aircraft engines.
- Identify the health condition of each engine.
- Detect potential HPC and Fan degradation.
- Classify machines into Healthy, Warning, and Critical conditions.
- Provide maintenance recommendations based on predicted machine health.
- Develop an interactive dashboard for monitoring engine health.

## Dataset

The project uses the NASA C-MAPSS FD004 dataset.

Dataset characteristics:

- Training trajectories: 248
- Test trajectories: 249
- Operating conditions: 6
- Fault modes: 2
  - HPC Degradation
  - Fan Degradation
- Each record contains engine operating information and sensor measurements.

The dataset contains multiple multivariate time series, where each time series represents the operational history of a different engine.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Joblib
- Streamlit
- Matplotlib
- NASA C-MAPSS Dataset

## Machine Learning Model

The project uses an XGBoost regression model to predict the Remaining Useful Life of aircraft engines.

The model is trained using processed sensor and operational data. Feature engineering and sensor-based degradation indicators are used to improve the prediction process.

The trained model is saved as:

`xgb_capped_model.pkl`

The feature list used by the model is saved as:

`final_features.pkl`

## Degradation Analysis

The project analyzes two major degradation modes:

### HPC Degradation

HPC-related sensors used:

- sensor_3
- sensor_7
- sensor_11

### Fan Degradation

Fan-related sensors used:

- sensor_8
- sensor_13
- sensor_18

Recent sensor values are processed to generate HPC and Fan degradation scores.

The system estimates the dominant degradation mode based on these scores.

## Health Classification

The predicted RUL is used to classify engine health into three categories:

- 🟢 Healthy
- 🟡 Warning
- 🔴 Critical

The final test results contain predictions for 248 machines.

Health status distribution:

- Healthy: 174 machines
- Warning: 39 machines
- Critical: 35 machines

## Model Performance

The model was evaluated using Mean Absolute Error (MAE) and Root Mean Square Error (RMSE).

### Results

- MAE: 22.71
- RMSE: 30.28

These metrics measure the difference between the actual RUL values and the predicted RUL values.

## Streamlit Dashboard

An interactive Streamlit dashboard was developed for visualizing the prediction results.

The dashboard provides:

- Fleet overview
- Machine selection
- Predicted RUL
- Health status
- HPC degradation score
- Fan degradation score
- Esti
- mated degradation mode
- Maintenance recommendation
- Machine prediction details
The dashboard helps users quickly identify machines that may require maintenance.

## Project Workflow

NASA C-MAPSS FD004 Dataset
            ↓
Data Preprocessing
            ↓
Feature Engineering
            ↓
Sensor Analysis
            ↓
HPC & Fan Degradation Analysis
            ↓
XGBoost Model Training
            ↓
RUL Prediction
            ↓
Health Classification
            ↓
Streamlit Dashboard
            ↓
Maintenance Recommendation

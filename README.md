# Credit Card Fraud Detection API

This project is a Django-based web application that serves a machine learning model to detect fraudulent credit card transactions. The model is trained on a highly imbalanced dataset from Kaggle, and this repository contains the full workflow from data analysis in a Jupyter Notebook to a deployed web API.

[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Django Version](https://img.shields.io/badge/django-5.2+-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Project Overview

The primary goal is to build a reliable classifier to distinguish between legitimate and fraudulent transactions. The project tackles the core challenge of extreme class imbalance using techniques like SMOTE and evaluates models using appropriate metrics like Average Precision.

### Features
* **Exploratory Data Analysis (EDA)** to understand data distributions and class imbalance.
* **Feature Engineering** to create more predictive features from existing data (`Amount_log`, `Hourly`).
* **Baseline Model** (Logistic Regression) to establish an initial performance benchmark.
* **Advanced Model** (SMOTE + Random Forest) for superior performance on the imbalanced data.
* **Django API** to serve the trained model and provide real-time predictions via a web interface.

## Dataset

The project uses the "Credit Card Fraud Detection" dataset from Kaggle.
* **Source:** [Kaggle Dataset Link](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
* **Description:** The dataset contains transactions made by European cardholders. It presents a total of 284,807 transactions, of which only 492 (0.172%) are fraudulent. The features `V1` to `V28` are the result of a PCA transformation to protect user identity.

## Project Structure

```
card_fraud/
│
├── fraud_detection/      # Django Project Directory
│   ├── manage.py
│   ├── fraud_detection/  # Project settings
│   ├── fraud_app/        # Django App
│   │   ├── templates/
│   │   │   └── fraud_app/
│   │   │       └── predict.html
│   │   ├── migrations/
│   │   ├── urls.py
│   │   └── views.py
│   └── ml_models/
│       └── fraud_detection_pipe.pkl  # Serialized ML model
│
├── fraud.ipynb           # Jupyter Notebook for EDA and Model Training
├── myenv/                  # Virtual Environment
└── README.md
```

## Setup and Installation

Follow these steps to set up the project locally.

**1. Clone the Repository**
```bash
git clone [https://github.com/your-username/fraud_detection.git](https://github.com/your-username/fraud_detection.git)
cd fraud_detection
```

**2. Create and Activate Virtual Environment**
```bash
python3 -m venv myenv
source myenv/bin/activate
```
*(On Windows, use `myenv\Scripts\activate`)*

**3. Install Dependencies**
First, create a `requirements.txt` file from your active environment:
```bash
pip freeze > requirements.txt
```
Then, install the required packages:
```bash
pip install -r requirements.txt
```

**4. Place the Model File**
Ensure your trained model (`fraud_detection_pipe.pkl`) is placed inside the `card_fraud/fraud_detection/ml_models/` directory.

## Running the Application

Once the setup is complete, you can run the Django development server.

```bash
cd fraud_detection/
python3 manage.py runserver
```
The application will be available at `http://127.0.0.1:8000/`.

## Model Performance

Two models were developed and evaluated. The advanced model using SMOTE and Random Forest showed significantly better performance, especially in handling the imbalanced nature of the data.

| Model                               | Evaluation Metric     | Score (on Cross-Validation) |
| ----------------------------------- | --------------------- | --------------------------- |
| Logistic Regression (Baseline)      | Average Precision     | ~0.713                      |
| **SMOTE + Random Forest (Advanced)** | **Average Precision** | **~0.845** |

**Recommendation:** For deployment, the **SMOTE + Random Forest** model (`smote_pipe` in the notebook) should be trained and serialized, as it provides a much more reliable prediction.



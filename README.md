# 🧠 SugarSense — Diabetes Prediction with Machine Learning

SugarSense is an end-to-end machine learning project designed to predict the likelihood of diabetes in individuals based on diagnostic health data. Built using Python and Scikit-learn, it applies classic classification algorithms to real-world medical datasets and evaluates their effectiveness in healthcare risk prediction.

 📌 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Features](#features)
- [Modeling Approach](#modeling-approach)
- [Results](#results)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Author](#author)
- [License](#license)


## 📖 Overview

This project explores how supervised machine learning algorithms can aid in early diabetes detection using patient-level medical data. It includes:

- Data preprocessing
- Feature scaling
- Model training and comparison
- Evaluation metrics
- Final model serialization (`.sav` file)

🔗 Read the full blog on Medium- https://medium.com/@qureshisadiq397/predicting-diabetes-with-machine-learning-a-hands-on-data-science-project-b870534970f6
---

## 📊 Dataset

- Source: Kaggle - Diabetes Dataset - https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset
- Original Contributor**: National Institute of Diabetes and Digestive and Kidney Diseases
- Samples: 768 patients
- Features: 8 numeric medical predictors + 1 binary outcome

---

## 📋 Features Used

- Pregnancies  
- Glucose  
- Blood Pressure  
- Skin Thickness  
- Insulin  
- BMI  
- Diabetes Pedigree Function  
- Age  
- Outcome (0 = Non-Diabetic, 1 = Diabetic)

---

## 🤖 Modeling Approach

The following models were implemented and compared:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier ✅ (best performer)
- Gaussian Naive Bayes

Key techniques:
- Imputation of biologically impossible values (e.g., 0 insulin)
- Feature scaling using `StandardScaler`
- 80-20 train-test split
- Model evaluation using accuracy, precision, recall, and F1-score


## ✅ Results

Random Forest Classifier showed the best performance with:
- Accuracy: ~81%
- Strong generalization on test data
- Low false negatives (important in healthcare)


## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/sxdiq07/SugarSense.git
cd SugarSense

****# Final Year Student Skill Gap Analysis with Feast

## 📌 Project Overview

This project focuses on analyzing the skill gaps of final-year students and predicting their placement readiness.

The project uses student academic scores, technical skills, projects, certifications, internships, and placement readiness information to identify the student's skill gap level.

The project also demonstrates the use of **Feast Feature Store** for managing and serving machine learning features.

---

## 🎯 Objectives

- Analyze the technical and professional skills of final-year students.
- Identify skill gaps among students.
- Create meaningful features from the available student data.
- Store and manage ML features using Feast.
- Train a machine learning model to predict the Skill Gap Level.
- Retrieve online features using Feast for real-time prediction.

---

## 📊 Dataset

The dataset contains **3000 student records** and **22 original columns**.

### Important attributes include:

- Roll Number
- Student Name
- Department
- Year
- Section
- Gender
- Programming Language
- Database Skill
- Cloud Skill
- Web Technology
- Data Tool
- Soft Skill Strength
- Coding Score
- Aptitude Score
- Communication Score
- Technical Score
- Projects Completed
- Certifications
- Internships
- Preferred Career
- Placement Readiness Score
- Skill Gap Level

The dataset contains three Skill Gap Levels:

- **Low**
- **Medium**
- **High**

### Skill Gap Distribution

| Skill Gap Level | Count | Percentage |
|-----------------|------:|----------:|
| Low | 1573 | 52.43% |
| Medium | 1284 | 42.80% |
| High | 143 | 4.77% |
| **Total** | **3000** | **100%** |

---

## ⚙️ Feature Engineering

Three additional features were created:

### 1. Technical Average

The average of:

- Coding Score
- Aptitude Score
- Communication Score
- Technical Score
2. Experience Score

The experience score is calculated using projects, certifications, and internships.

experience_score =
Projects_Completed + Certifications + Internships
3. Skill Strength Score

The overall skill strength is calculated using the technical average and experience score.

skill_strength_score =
(technical_average × 0.7) + (experience_score × 2)

The resulting value is restricted to a range of 0 to 100.

Machine Learning

A machine learning classification model was developed to predict the Skill Gap Level of students.

The features used for prediction are:

Coding_Score
Aptitude_Score
Communication_Score
Technical_Score
Projects_Completed
Certifications
Internships
Placement_Readiness_Score
technical_average
experience_score
skill_strength_score

A Balanced Random Forest model was evaluated on the test dataset.

Model Accuracy
Balanced Random Forest Accuracy: 48.33%
Classification Report
Class	Precision	Recall	F1-Score
High	0.00	0.00	0.00
Low	0.51	0.68	0.59
Medium	0.41	0.30	0.34

The dataset is imbalanced because the High Skill Gap category contains only 143 students compared with 1573 Low and 1284 Medium students. This imbalance affects the model's ability to correctly predict the High category.

Feast Feature Store

Feast is used as the feature store for managing and serving the machine learning features.

Entity

The project uses:

student_id

as the unique entity identifier for each student.

Feature View

The Feast Feature View is:

student_skill_gap_features

It contains the student's technical, academic, experience, and placement-related features.

Offline Feature Store

The offline feature data is stored in:

data/skill_gap_features.parquet

The feature dataset contains 3000 records and 13 columns.

Online Feature Store

The project uses the local SQLite online store provided through the Feast configuration.

Feast Workflow
Student Dataset
       |
       v
Data Preprocessing
       |
       v
Feature Engineering
       |
       v
Feature Extraction
       |
       v
Parquet Feature Dataset
       |
       v
Feast Feature Store
       |
       +------------------+
       |                  |
       v                  v
Offline Features     Online Features
       |                  |
       +--------+---------+
                |
                v
       Machine Learning Model
                |
                v
       Skill Gap Prediction
Online Feature Retrieval

Feast was used to materialize the historical features into the online store.

An online feature retrieval test was performed for the student:

Student ID: IT0001

The retrieved features included:

Internships: 3
Certifications: 4
Technical_Score: 69
Placement_Readiness_Score: 80
Coding_Score: 78
technical_average: 80.25
Projects_Completed: 0
experience_score: 7
Communication_Score: 92
Aptitude_Score: 82
skill_strength_score: 70.175

The machine learning model predicted:

Predicted Skill Gap Level: Low
Project Structure
final-year-student-skill-gap-feast/
│
├── 231FA04157_MLOps_Feast_SkillGap.ipynb
├── final_year_skill_gap_dataset_3000.csv
├── skill_gap_model.pkl
│
└── feature_repo/
    ├── feature_store.yaml
    ├── features.py
    │
    └── data/
        ├── .gitkeep
        └── skill_gap_features.parquet
Technologies Used
Python
Pandas
Scikit-learn
Matplotlib
Feast
Apache Parquet
SQLite
Google Colab
GitHub
How to Run
1. Open the Notebook

Open the following notebook:

231FA04157_MLOps_Feast_SkillGap.ipynb

The notebook contains the complete workflow including data loading, preprocessing, feature engineering, machine learning, Feast feature extraction, feature retrieval, and prediction.

2. Install Required Libraries
pip install pandas scikit-learn matplotlib feast pyarrow
3. Run the Notebook

Run the notebook cells sequentially to perform:

Dataset loading
Data preprocessing
Feature engineering
Feature extraction
Machine learning model training
Model evaluation
Feast feature store setup
Historical feature retrieval
Online feature materialization
Online feature retrieval
Skill gap prediction
4. Feast Configuration

The Feast configuration is available inside:

feature_repo/feature_store.yaml

The feature definitions are available inside:

feature_repo/features.py
5. Apply Feast Configuration

From the Feast repository directory:

feast apply
6. Materialize Features
feast materialize 2026-01-01T00:00:00 2026-12-31T23:59:59
Conclusion

This project demonstrates an end-to-end student skill gap analysis workflow using Machine Learning and the Feast Feature Store.

The system performs data preprocessing and feature engineering, creates meaningful student skill features, stores them using Feast, retrieves online features, and uses a machine learning model to predict the student's Skill Gap Level.

The current model achieved an accuracy of 48.33%. The results also show that class imbalance is an important factor affecting prediction performance, especially for the High Skill Gap category.

The project provides a foundation that can be further improved using better class-balancing techniques, additional student features, and improved machine learning models.
technical_average =
(Coding_Score + Aptitude_Score + Communication_Score + Technical_Score) / 4
****

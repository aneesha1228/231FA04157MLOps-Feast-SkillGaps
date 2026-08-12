# Curriculum-Industry Skill Gap Feature Store Using Feast

## Student Details

**Name:** Aneesha  
**Register Number:** 231FA04157  
**Section:** H

---

## 1. Problem Statement

The goal of this project is to analyze the curriculum-industry skill gap among final-year students using a student skill-gap dataset and convert the important information into a Feast-based feature store.

The project performs feature engineering on student academic, technical, experience, and placement-related information. The engineered features are stored using Feast and can be retrieved for both historical machine-learning training and online prediction.

The project demonstrates an end-to-end workflow including feature engineering, Feast entity creation, data source creation, FeatureView creation, historical feature retrieval, online materialization, online feature retrieval, and machine-learning based Skill Gap prediction.

---

## 2. Dataset

The project uses a final-year student skill-gap dataset containing **3000 student records**.

### Number of Skills / Skill-related Attributes

The dataset contains curriculum and industry-oriented skill attributes such as:

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
- Placement Readiness Score

### Dataset Columns

The original dataset contains **22 columns**:

- Roll_No
- Student_Name
- Department
- Year
- Section
- Gender
- Programming_Language
- Database_Skill
- Cloud_Skill
- Web_Technology
- Data_Tool
- Soft_Skill_Strength
- Coding_Score
- Aptitude_Score
- Communication_Score
- Technical_Score
- Projects_Completed
- Certifications
- Internships
- Preferred_Career
- Placement_Readiness_Score
- Skill_Gap_Level

### Target

The target variable is:

```text
Skill_Gap_Level
```

The target contains three classes:

- Low
- Medium
- High

### Dataset Distribution

| Skill Gap Level | Count | Percentage |
|---|---:|---:|
| Low | 1573 | 52.43% |
| Medium | 1284 | 42.80% |
| High | 143 | 4.77% |
| **Total** | **3000** | **100%** |

### How the Entries Were Created

The dataset was created as a curriculum-industry skill-gap dataset containing student academic scores, technical skills, practical experience, certifications, internships, placement readiness, and the resulting Skill Gap Level.

---

## 3. Feature Engineering

Feature engineering was performed to create useful features for the Feast Feature Store and machine-learning model.

The following 11 features are stored in the Feast FeatureView.

| Feature | Meaning |
|---|---|
| Coding_Score | Student's coding performance score |
| Aptitude_Score | Student's aptitude performance score |
| Communication_Score | Student's communication performance score |
| Technical_Score | Student's technical skill score |
| Projects_Completed | Number of projects completed by the student |
| Certifications | Number of certifications completed |
| Internships | Number of internships completed |
| Placement_Readiness_Score | Student's readiness for placement |
| technical_average | Average of the four technical-related scores |
| experience_score | Combined score from projects, certifications, and internships |
| skill_strength_score | Overall calculated skill strength score |

### Technical Average

The technical average is calculated using Coding Score, Aptitude Score, Communication Score, and Technical Score.

```text
technical_average =
(Coding_Score + Aptitude_Score + Communication_Score + Technical_Score) / 4
```

For example, for student IT0001:

```text
(78 + 82 + 92 + 69) / 4 = 80.25
```

### Experience Score

The experience score is a derived feature based on projects, certifications, and internships.

```text
experience_score =
Projects_Completed + Certifications + Internships
```

For student IT0001:

```text
0 + 4 + 3 = 7
```

### Skill Strength Score

The skill strength score combines the technical average and experience score.

```text
skill_strength_score =
(technical_average × 0.7) + (experience_score × 2)
```

The resulting score is restricted to the required range.

---

## 4. Feast Architecture

The overall architecture of the project is:

```text
Original Dataset
       |
       v
Feature Engineering
       |
       v
Parquet Offline Data
       |
       v
Feast FeatureView
       |
       +-----------------------------+
       |                             |
       v                             v
Historical Features             Materialization
       |                             |
       v                             v
Model Training                 Online Store
                                     |
                                     v
                              Online Retrieval
                                     |
                                     v
                                 Prediction
```

---

## 5. Feast Implementation

### Entity

The entity used in the Feast implementation is:

```text
student_id
```

Each student is uniquely identified using `student_id`.

The `student_id` is created from the student's Roll Number.

### Data Source

The feature data is stored in a Parquet file:

```text
data/skill_gap_features.parquet
```

Feast uses a `FileSource` with:

```text
timestamp_field = event_timestamp
```

The event timestamp is required by Feast for time-aware feature retrieval.

### FeatureView

The FeatureView is named:

```text
student_skill_gap_features
```

It contains the 11 engineered and selected features required for machine-learning prediction.

### Feast Configuration

The project uses a local Feast provider.

The configuration contains:

```yaml
project: skill_gap
provider: local
registry: data/registry.db

online_store:
  path: data/online_store.db

offline_store:
  type: file
```

### Feast Apply

The command:

```bash
feast apply
```

registers the Feast objects defined in `feature_store.yaml` and `features.py`.

The implementation successfully created:

- Project: `skill_gap`
- Entity: `student_id`
- FeatureView: `student_skill_gap_features`

### Historical Feature Retrieval

Historical features were retrieved from the feature store for machine-learning use.

The historical feature dataset had:

```text
Historical Feature Shape: (3000, 13)
```

The 13 columns include:

- student_id
- event_timestamp
- 11 feature columns

### Materialization

The Feast features were materialized from:

```text
2026-01-01 00:00:00+00:00
```

to:

```text
2026-12-31 23:59:59+00:00
```

Materialization loads the historical feature values into the online store so that they can be retrieved for online prediction.

### Online Feature Retrieval

Online features were successfully retrieved for:

```text
Student ID: IT0001
```

The retrieved features included:

```text
Internships: 3
Certifications: 4
Technical_Score: 69.0
Placement_Readiness_Score: 80.0
Coding_Score: 78.0
technical_average: 80.25
Projects_Completed: 0
experience_score: 7.0
Communication_Score: 92.0
Aptitude_Score: 82.0
skill_strength_score: 70.175
```

---

## 6. Machine Learning Model

A machine-learning classification model was developed using the Feast features.

The model uses the following input features:

```text
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
```

A Balanced Random Forest model was evaluated for predicting the Skill Gap Level.

### Model Accuracy

```text
Balanced Random Forest Accuracy: 48.33%
```

### Classification Report

| Class | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| High | 0.00 | 0.00 | 0.00 |
| Low | 0.51 | 0.68 | 0.59 |
| Medium | 0.41 | 0.30 | 0.34 |

The High class has very few samples compared with the Low and Medium classes, which affects the model's ability to predict the High category.

---

## 7. Results

### Historical Feature Output

The historical feature dataset was successfully generated with:

```text
Historical Feature Shape: (3000, 13)
```

Example historical record:

```text
Student ID: IT0001
Coding Score: 78
Aptitude Score: 82
Communication Score: 92
Technical Score: 69
Projects Completed: 0
Certifications: 4
Internships: 3
Placement Readiness Score: 80
technical_average: 80.25
experience_score: 7
skill_strength_score: 70.175
```

### Model Result

```text
Balanced Random Forest Accuracy: 48.33%
```

### Online Feature Output

For:

```text
Student ID: IT0001
```

the online store returned the student's feature values successfully.

### Final Prediction

```text
Student ID: IT0001
Predicted Skill Gap Level: Low
```

---

# 8. Required Analysis

## 1. What is the entity in your Feast implementation?

The entity in the Feast implementation is `student_id`.

It uniquely identifies each student. The entity is defined using the student's Roll Number as the join key.

---

## 2. List the features stored in your FeatureView.

The FeatureView `student_skill_gap_features` stores the following 11 features:

1. Coding_Score
2. Aptitude_Score
3. Communication_Score
4. Technical_Score
5. Projects_Completed
6. Certifications
7. Internships
8. Placement_Readiness_Score
9. technical_average
10. experience_score
11. skill_strength_score

---

## 3. Explain how one feature was calculated.

The `technical_average` feature is calculated as the average of Coding Score, Aptitude Score, Communication Score, and Technical Score.

```text
technical_average =
(Coding_Score + Aptitude_Score + Communication_Score + Technical_Score) / 4
```

For IT0001:

```text
(78 + 82 + 92 + 69) / 4
= 80.25
```

Therefore, the technical average for IT0001 is 80.25.

---

## 4. What is the difference between your original dataset and the feature dataset?

The original dataset contains 3000 student records with 22 columns covering student information, curriculum skills, technical scores, experience, placement readiness, and the target Skill Gap Level.

The feature dataset is a reduced dataset prepared specifically for Feast. It contains the student entity, event timestamp, and the 11 features required for machine-learning and online feature retrieval.

The generated Feast feature dataset has:

```text
3000 rows × 13 columns
```

The target `Skill_Gap_Level` is not stored as a Feast feature because it is the prediction target used by the machine-learning model.

---

## 5. What is the purpose of the offline store?

The offline store is used for storing and retrieving historical feature data.

It is useful for creating training datasets and performing historical feature retrieval without manually calculating the features again.

In this project, the offline feature data is maintained using the Parquet file source.

---

## 6. What is the purpose of the online store?

The online store is used to provide the latest available feature values quickly for prediction.

In this project, the local Feast configuration uses SQLite as the online store.

After materialization, the model can retrieve features for a particular student using the student's `student_id`.

---

## 7. What is the purpose of `feast apply`?

`feast apply` registers and applies the Feast objects defined in the feature repository.

It creates or updates:

- Entities
- FeatureViews
- Feature definitions
- Feast registry information

In this project, `feast apply` successfully created the `skill_gap` project, `student_id` entity, and `student_skill_gap_features` FeatureView.

---

## 8. What does materialization do?

Materialization copies feature values from the historical/offline source into the Feast online store for a specified time range.

In this project, features were materialized for the year 2026.

After materialization, the online store could provide feature values for students such as IT0001.

---

## 9. What is the advantage of retrieving features through Feast instead of manually calculating them separately during training and prediction?

Using Feast provides a consistent feature definition for both training and prediction.

Without a feature store, features may be calculated differently during model training and online prediction, which can lead to inconsistent results.

Feast helps maintain the same feature definitions and makes the features reusable for historical and online retrieval.

It also reduces the need to manually recreate the feature calculations every time a prediction is required.

---

## 10. State two limitations of your current dataset.

### Limitation 1: Class Imbalance

The Skill Gap Level distribution is imbalanced.

Only 143 out of 3000 records belong to the High category, while Low and Medium contain many more records.

This makes it difficult for the model to correctly predict the High category.

### Limitation 2: Limited Curriculum-Industry Evidence

The current dataset contains student skill and performance information, but it has limited direct industry evidence such as detailed job-role requirements, employer skill requirements, or real placement outcomes.

---

## 11. State two ways your feature store could be improved when more curriculum and industry evidence becomes available.

### Improvement 1: Add Industry Skill Features

Industry-oriented features such as job-role requirements, employer-required skills, technology demand, and role-specific skill scores can be added to the FeatureView.

### Improvement 2: Add More Historical and Real-Time Evidence

More curriculum updates, placement results, internship outcomes, certification information, and industry requirements can be incorporated into the feature store.

This would make the features more representative of current industry expectations and improve the usefulness of the Skill Gap prediction system.

---

## 9. Project Structure

```text
final-year-student-skill-gap-feast/
│
├── 231FA04157_MLOps_Feast_SkillGap.ipynb
├── final_year_skill_gap_dataset_3000.csv
├── skill_gap_model.pkl
│
└── feature_repo/
    │
    ├── feature_store.yaml
    ├── features.py
    │
    └── data/
        ├── .gitkeep
        └── skill_gap_features.parquet
```

---

## 10. Technologies Used

- Python
- Pandas
- Scikit-learn
- Feast
- Apache Parquet
- SQLite
- Matplotlib
- Google Colab
- GitHub

---

## 11. Conclusion

This project converts a curriculum-industry student skill-gap dataset into a Feast-based feature store.

The project demonstrates feature engineering, Feast entity creation, data source creation, FeatureView creation, registration using `feast apply`, historical feature retrieval, materialization into the online store, online feature retrieval, and use of Feast features in a machine-learning model.

For the tested student IT0001, the online features were successfully retrieved and the model predicted:

```text
Skill Gap Level: Low
```

The Balanced Random Forest model achieved an accuracy of:

```text
48.33%
```

The current implementation provides a foundation for integrating additional curriculum and industry evidence into the feature store in the future.

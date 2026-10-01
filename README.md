# Student Performance Analysis

A Python-based **Student Performance Analysis** project developed for Problem Based Learning (PBL) Activity 3. The project uses a real-world student dataset to perform data cleaning, descriptive statistical analysis, correlation analysis, category-wise analysis, and graphical visualization.

---

## 📌 Project Information

**College:** Government Engineering College, Bhavnagar  
**Department:** Computer Engineering  
**Subject:** Python for Data Science  
**Subject Code:** BE05000231  
**Activity:** Problem Based Learning – Activity 3  
**Academic Year:** 2026–27  
**Division:** E  

---

## 🎯 Aim

To develop a Python-based menu-driven Student Performance Analysis application that uses a real-world student dataset to perform data cleaning, descriptive statistical analysis, correlation analysis, and graphical visualization for effective exploration and understanding of student performance data.

---

## 📝 Problem Statement

Design and implement a menu-driven application using a real-world dataset that showcases descriptive analytics through statistical summaries and graphical representations for effective data exploration.

The application analyzes student performance and learning-related factors using Python and provides the results through a simple menu-driven interface.

---

## 📊 Dataset Description

The project uses a **Student Performance Dataset** containing information related to students' academic performance and learning-related factors.

### Dataset Details

- **Original Records:** 14,003
- **Attributes:** 16
- **Records After Cleaning:** 12,469
- **Duplicate Records Removed:** 1,534
- **Missing Values After Cleaning:** 0

### Dataset Attributes

| Attribute | Description |
|---|---|
| StudyHours | Number of hours spent studying |
| Attendance | Student attendance value |
| Resources | Resource-related category/value |
| Extracurricular | Extracurricular activity value |
| Motivation | Motivation category/value |
| Internet | Internet access value |
| Gender | Gender category/value |
| Age | Age of the student |
| LearningStyle | Learning style category/value |
| OnlineCourses | Number/value related to online courses |
| Discussions | Discussion participation value |
| AssignmentCompletion | Assignment completion percentage/value |
| ExamScore | Examination score |
| EduTech | Educational technology value |
| StressLevel | Stress-level category/value |
| FinalGrade | Final-grade category/value |

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **CSV Dataset**

---

## ✨ Features

The application provides a menu-driven interface with the following options:

1. Display Dataset
2. Dataset Information
3. Data Cleaning Report
4. Descriptive Statistics
5. Study Hours Analysis
6. Attendance Analysis
7. Exam Score Analysis
8. Performance Distribution
9. Gender-wise Analysis
10. Assignment Completion Analysis
11. Final Grade Analysis
12. Stress Level Analysis
13. Correlation Analysis
14. Resource Analysis
15. Internet Access Analysis
16. Key Findings
17. Exit

---

## 🧹 Data Cleaning

The dataset is cleaned before performing analysis.

### Cleaning Summary

| Item | Result |
|---|---:|
| Original Records | 14,003 |
| Duplicate Records Removed | 1,534 |
| Empty Rows Removed | 0 |
| Records After Cleaning | 12,469 |
| Missing Values After Cleaning | 0 |

---

## 📈 Descriptive Statistical Analysis

The application calculates statistical measures including:

- Mean
- Median
- Minimum
- Maximum
- Standard Deviation
- Variance
- Quartiles

### Important Results

| Attribute | Mean | Median | Minimum | Maximum | Standard Deviation |
|---|---:|---:|---:|---:|---:|
| Study Hours | 20.03 | 20 | 5 | 44 | 6.05 |
| Attendance | 80.24 | 80 | 60 | 100 | 11.47 |
| Exam Score | 70.31 | 70 | 40 | 100 | 17.70 |
| Assignment Completion | 74.52 | 74 | 50 | 100 | 14.66 |

### Exam Score Statistics

- **Mean:** 70.31
- **Median:** 70
- **Minimum:** 40
- **Maximum:** 100
- **Variance:** 313.17
- **Q1:** 55
- **Q2:** 70
- **Q3:** 86

---

## 📊 Analysis Performed

### Study Hours Analysis

The project analyzes the distribution and statistical characteristics of students' study hours.

**Average Study Hours:** 20.03

---

### Attendance Analysis

The project analyzes student attendance values and their distribution.

**Average Attendance:** 80.24

---

### Exam Score Analysis

The project analyzes examination scores using descriptive statistics and graphical visualization.

**Average Exam Score:** 70.31  
**Highest Exam Score:** 100  
**Lowest Exam Score:** 40

---

### Performance Distribution

The application categorizes examination performance into:

- Excellent
- Good
- Average
- Needs Improvement

The observed distribution is:

| Performance Category | Number of Students |
|---|---:|
| Excellent | 4,374 |
| Good | 4,082 |
| Average | 4,013 |

---

### Gender-wise Analysis

The application compares examination scores across the available gender categories.

| Gender Category | Students | Average Exam Score |
|---|---:|---:|
| 0 | 5,753 | 69.99 |
| 1 | 6,716 | 70.59 |

---

### Assignment Completion Analysis

The application analyzes assignment completion and its relationship with examination scores.

**Average Assignment Completion:** 74.52

**Correlation with Exam Score:** 0.027

---

### Final Grade Analysis

The application displays the distribution of Final Grade category values.

| Final Grade | Students |
|---|---:|
| 0 | 3,401 |
| 1 | 2,943 |
| 2 | 3,221 |
| 3 | 2,904 |

> Note: Final Grade values are category codes. Their numerical codes should not automatically be interpreted as continuous numerical measurements without a corresponding data dictionary.

---

### Stress Level Analysis

The application analyzes the distribution of Stress Level categories and compares average examination scores.

| Stress Level | Students | Average Exam Score |
|---|---:|---:|
| 0 | 2,524 | 71.90 |
| 1 | 3,614 | 69.74 |
| 2 | 6,331 | 70.00 |

---

### Resource Analysis

The application compares examination scores across resource-related categories.

| Resource Category | Students | Average Exam Score |
|---|---:|---:|
| 0 | 2,585 | 70.22 |
| 1 | 6,035 | 70.25 |
| 2 | 3,849 | 70.46 |

---

### Internet Access Analysis

The application analyzes examination scores according to Internet access categories.

| Internet Category | Students | Average Exam Score |
|---|---:|---:|
| 0 | 1,034 | 70.74 |
| 1 | 11,435 | 70.27 |

---

## 🔗 Correlation Analysis

The project uses correlation analysis to examine relationships between numerical attributes.

Important correlations with **ExamScore** include:

| Attribute | Correlation with Exam Score |
|---|---:|
| StudyHours | 0.004 |
| Attendance | -0.014 |
| AssignmentCompletion | 0.027 |

Correlation values are used to describe the statistical relationship between variables and should not be interpreted as proof of causation.

---

## 📊 Visualizations

The project uses **Matplotlib** and **Seaborn** to generate graphical representations of the data.

Visualizations include:

- Study Hours Distribution
- Attendance Distribution
- Exam Score Distribution
- Performance Distribution
- Gender-wise Analysis
- Assignment Completion Analysis
- Final Grade Distribution
- Stress Level Analysis
- Correlation Matrix
- Resource Analysis
- Internet Access Analysis

---

## 🔑 Key Findings

The analysis produced the following observations:

- The dataset contains **14,003 original records**.
- **1,534 duplicate records** were removed during data cleaning.
- The cleaned dataset contains **12,469 records**.
- No missing values remained after cleaning.
- Average study hours are **20.03**.
- Average attendance is **80.24**.
- Average exam score is **70.31**.
- The highest exam score is **100**.
- The lowest exam score is **40**.
- Average assignment completion is **74.52**.
- The calculated correlations between Study Hours, Attendance, Assignment Completion and Exam Score are close to zero in this dataset.

---

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your system.

### 2. Install Required Libraries

Open Command Prompt or Terminal and run:

```bash
pip install pandas numpy matplotlib seaborn

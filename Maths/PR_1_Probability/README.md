# Probability Assignment Using Student Performance Dataset

## Overview

This project demonstrates the application of fundamental probability concepts using a student performance dataset containing 200 student records.

The dataset includes the following attributes:

* Study Hours
* Attendance Percentage
* Group Discussion Participation
* Previous Test Score
* Final Exam Result (Pass/Fail)

The objective of this assignment is to understand probability concepts through practical calculations, probability distributions, contingency tables, conditional probability, and Bayes Theorem.

---

## Dataset Information

| Column Name         | Description                                 |
| ------------------- | ------------------------------------------- |
| study_hours         | Number of hours studied per week            |
| attendance          | Attendance percentage                       |
| group_discussion    | Participation in group discussions (Yes/No) |
| previous_test_score | Previous test marks out of 100              |
| final_exam_pass     | Final exam result (Pass/Fail)               |

Total Records: **200 Students**

---

## Tasks Performed

### 1. Understanding Probability

* Defined probability in simple terms.
* Explained key probability terminology.
* Identified probability events from the dataset.

### 2. Types of Probability

* Calculated Empirical Probability.
* Calculated Theoretical Probability.

Results:

* Empirical Probability of Passing = **0.68**
* Theoretical Probability of Passing = **0.50**

### 3. Random Variable & Probability Distribution

Defined a random variable:

**X = Number of students passing the final exam out of 3 randomly selected students**

Calculated:

* Probability Distribution Table
* Mean
* Variance

Results:

* Mean = **2.04**
* Variance = **0.6528**

### 4. Venn Diagram

Created a Venn Diagram for:

* Students studying more than 10 hours per week.
* Students having attendance greater than 80%.
* Students satisfying both conditions.

### 5. Contingency Table & Probability Calculations

Created a contingency table between:

* Group Discussion Participation
* Final Exam Result

Calculated:

* Joint Probability
* Marginal Probability
* Conditional Probability

### 6. Understanding Relationships

Analyzed the relationship between:

* Participation in Group Discussions
* Passing the Final Exam

Conclusion:

* Events are **Dependent**
* Events are **Not Mutually Exclusive**

### 7. Bayes Theorem Application

Applied Bayes Theorem to calculate:

**Probability of passing given high attendance**

Result:

**P(Pass | High Attendance) = 79.33%**

---

## Key Findings

* Students with higher attendance have a greater probability of passing.
* Students participating in group discussions perform better than the overall student population.
* Study hours and previous test scores positively influence exam performance.
* Attendance and group discussion participation are important indicators of success.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib

---

## Conclusion

This assignment successfully demonstrates how probability concepts can be applied to real-world educational data. Through empirical probability, probability distributions, contingency tables, conditional probability, and Bayes Theorem, we identified the major factors affecting student success. The analysis shows that high attendance, active participation in group discussions, consistent study habits, and strong previous academic performance significantly increase the probability of passing the final examination.

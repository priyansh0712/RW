# Transaction Distribution Analysis

## Overview

This project analyzes customer transaction data using statistical distributions and probability concepts. The goal is to understand transaction behavior, evaluate distribution fitting, test normality, perform transformations, and derive meaningful business insights from the dataset.

## Dataset Features

* transaction_id
* customer_id
* transaction_amount
* transaction_date
* transaction_count
* region
* transaction_status

## Technologies Used

* Python
* NumPy
* Pandas
* SciPy
* Statsmodels
* Matplotlib
* Seaborn
* Jupyter Notebook

## Tasks Performed

### Theoretical Concepts

* Statistical Distributions
* Q-Q Plot
* Discrete vs Continuous Distributions
* Bernoulli Distribution
* Binomial Distribution
* Log-Normal Distribution
* Power Law Distribution
* Box-Cox Transformation
* Poisson Distribution
* Z-Score Probability
* PDF and CDF

### Practical Analysis

1. Bernoulli Distribution fitting for transaction success/failure.
2. Binomial Distribution fitting for weekly transaction counts.
3. Poisson Distribution modeling for daily transaction frequency.
4. Log-Normal Distribution fitting for transaction amounts.
5. Power Law Distribution analysis.
6. Q-Q Plot generation and normality testing.
7. Box-Cox Transformation for variance stabilization.
8. Z-Score calculation and probability estimation for transactions above ₹5000.
9. PDF and CDF visualization.
10. Distribution comparison and best-fit selection.

## Key Findings

* Transaction success events follow Bernoulli behavior.
* Weekly transaction counts can be modeled using Binomial Distribution.
* Daily transaction frequency shows Poisson characteristics.
* Transaction amounts are positively skewed.
* Log-Normal Distribution provides a better fit than Normal Distribution.
* Q-Q Plot indicates deviation from perfect normality.
* Box-Cox Transformation improves data symmetry.
* Z-Scores help identify unusual transactions and outliers.

## Business Insights

* Majority of transactions are low to medium value.
* High-value transactions are infrequent but contribute significantly to revenue.
* Statistical modeling helps estimate transaction trends and customer behavior.
* Distribution fitting assists in risk assessment and anomaly detection.

## Conclusion

This project demonstrates the practical application of probability distributions and statistical analysis techniques on real-world transaction data. The analysis shows that transaction amounts are best represented by a Log-Normal distribution, while transaction occurrences and frequencies can be modeled using Bernoulli, Binomial, and Poisson distributions. The results provide valuable insights for business decision-making and transaction monitoring.

## Author

Priyansh Vekariya
# Customer Segmentation Analysis using K-Means Clustering

## Dashboard Preview

> Add your Power BI dashboard screenshot in the folder:
>
> screenshots/dashboard.png

![Customer Segmentation Dashboard](screenshots/dashboard.png)

---

## Overview

This project focuses on Customer Segmentation using Machine Learning and Power BI. The main objective is to identify different groups of customers based on their Annual Income and Spending Score using the K-Means Clustering algorithm.

Customer segmentation helps businesses understand customer behavior, personalize marketing campaigns, improve customer retention, and make data-driven decisions.

---

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Power BI

---

## Dataset Information

The dataset contains customer information including:

- Customer ID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1-100)

Total Records: **200**

---

## Project Workflow

### 1. Data Collection

Loaded the Mall Customers dataset using Pandas.

### 2. Data Cleaning

- Checked for missing values
- Removed null values
- Validated dataset quality

### 3. Feature Selection

Selected the following features for clustering:

- Annual Income (k$)
- Spending Score (1-100)

### 4. Feature Scaling

Applied StandardScaler to normalize the selected features before clustering.

### 5. Elbow Method

Used the Elbow Method to determine the optimal number of clusters.

### 6. K-Means Clustering

Applied K-Means Clustering with 5 clusters to segment customers into distinct groups.

### 7. Data Visualization

Generated:

- Elbow Method Graph
- Customer Segmentation Scatter Plot
- Cluster Analysis Summary

### 8. Dashboard Development

Built an interactive Power BI dashboard to visualize customer segments and business insights.

---

## Power BI Dashboard Features

### KPI Cards

- Total Customers
- Average Age
- Average Income
- Average Spending Score

### Interactive Visualizations

- Customer Segmentation Scatter Plot
- Customer Distribution by Cluster
- Average Income by Cluster
- Average Spending Score by Cluster
- Gender Distribution
- Age Distribution
- Cluster Summary Matrix

### Filters

- Gender
- Cluster
- Age

---

## Key Insights

### Premium Customers

- High Income
- High Spending Score
- Most valuable customer segment

### Budget Customers

- Lower Income
- Controlled spending behavior
- Price-sensitive customers

### Potential Customers

- High Income
- Lower Spending Score
- Strong opportunity for targeted marketing

### Young Shoppers

- Younger age group
- Active spending behavior
- High growth potential

### Regular Customers

- Moderate income
- Moderate spending patterns
- Stable customer base

---

## Results

Successfully segmented customers into five distinct groups using K-Means Clustering.

The Power BI dashboard provides valuable insights into:

- Customer demographics
- Spending behavior
- Income distribution
- Customer groups
- Business opportunities

---

## Project Structure

```text
Customer-Segmentation-Analysis/
│
├── data/
│   ├── Mall_Customers.csv
│   └── Customer_Segment.csv
│
├── screenshots/
│   └── dashboard.png
│
├── customer_segmentation.py
│
├── elbow_method.png
│
├── customer_segmentation.png
│
├── Customer_Segmentation_Dashboard.pbix
│
└── README.md
```

---

## How to Run the Project

### Clone Repository

```bash
git clone https://github.com/your-username/Customer-Segmentation-Analysis.git
```

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Run Project

```bash
python customer_segmentation.py
```

---

## Future Enhancements

- Customer Lifetime Value Analysis
- Real-Time Dashboard Integration
- Predictive Customer Analytics
- Advanced Segmentation Techniques

---

## Author

### Yaswanth Kumar Bandi

Aspiring Data Analyst

**Skills:**
- Python
- SQL
- Power BI
- Machine Learning
- Data Visualization

---

## Project Status

✅ Completed

✅ Machine Learning Model Developed

✅ Power BI Dashboard Created

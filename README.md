# 🚀 DeliverIQ — Food Delivery Delay Analysis
deployed link : https://deliveriq.netlify.app/

## 📌 Project Overview
DeliverIQ is a data analysis project aimed at understanding and improving food delivery performance. The goal is to identify key factors that influence delivery delays and provide actionable insights for better service reliability.

---

## 🎯 Problem Statement
A food delivery platform wants to improve service reliability but lacks clarity on delivery time variations.  
This project analyzes delivery data to identify delay patterns and performance factors.

---

## 📊 Dataset
- Source: Kaggle  
- Records: 45,593  
- Features:
  - Delivery Time
  - Delivery Person Age & Ratings
  - Restaurant & Delivery Locations
  - Vehicle Type
  - Order Type  

---

## 🛠️ Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- HTML, CSS, JavaScript(for website generation)

---

## ⚙️ Data Processing
## 🔄 Raw vs Cleaned Data

### 📥 Raw Dataset
The original dataset contained:
- Column name `Time_taken(min)` which was not intuitive
- No direct feature representing distance between restaurant and delivery location
- Data in original format without feature engineering

---

### 🧹 Cleaned Dataset
The dataset was transformed to improve clarity and analysis:

- Renamed column:
  - `Time_taken(min)` → `delivery_delay`
- Removed duplicate records (if any)
- Verified that no missing values were present
- Created a new feature:
  - **Distance** calculated using restaurant and delivery coordinates

---

### 🔍 Key Improvement
The addition of the **distance feature** enabled deeper analysis of delivery delays, helping identify that distance is a major factor affecting delivery time.

---

### 📊 Outcome
The cleaned dataset is more:
- Readable
- Structured
- Suitable for analysis and visualization
- Renamed column `Time_taken(min)` → `delivery_delay`
- Removed duplicates
- Verified no missing values
- Created new feature:
  - **Distance** using latitude & longitude

---

## 📈 Analysis Performed
- Delivery Time Distribution
- Distance vs Delivery Time
- Vehicle Type Impact
- Order Type Impact
- Ratings vs Delivery Time

---

## 🔍 Key Insights
- Most deliveries are completed within **25–40 minutes**
- Delivery time **increases with distance**
- **Vehicle type significantly affects delivery performance**
- Higher-rated delivery personnel tend to deliver faster
- Some extreme delays indicate operational inefficiencies

---

## 🌐 Website
An interactive dashboard was created to visualize insights using modern UI and dynamic charts.

👉 Project Name: **DeliverIQ**

---

## 📂 Project Structure

~~~
S69_2003_DATA_SCIENCE_DELIVERIQ/
│
├── 📄 README.md
├── 📄 LICENSE
│
├── 📊 Food Delivery Time Prediction Case Study.xlsx   (Raw Dataset)
├── 📊 cleaned_data.csv                                (Processed Dataset)
│
├── 📓 food_delivery_analysis.ipynb                    (Colab Notebook)
│
├── 🌐 index.html                                      (Interactive Website - DeliverIQ)
│
└── 📁 images/
    ├── dist.png
    ├── distance.png
    ├── vehicle.png
    ├── order.png
    └── ratings.png
~~~

---

## 🚀 How to Run
1. Open the notebook in Google Colab  
2. Run all cells  
3. View charts and insights  
4. Open `index.html` to view the interactive website  

---

## ⚠️ Limitations
- Dataset does not include time-of-day or traffic data  
- No explicit geographic zones available  
- Distance calculated is approximate  

---

## 🎯 Conclusion
Distance and vehicle type are the most influential factors affecting delivery time.  
Optimizing route planning and vehicle allocation can significantly improve delivery efficiency.

----


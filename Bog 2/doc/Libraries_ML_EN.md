# 4. Essential Libraries For Machine Learning

Python provides an ecosystem of libraries for **data processing, analysis, and visualization**.  
A library is a collection of pre-built functions and objects. You can use these libraries instead of writing everything from scratch.

In Python, there are 4 libraries that are mandatory to know when starting Machine Learning:

- NumPy
- Pandas
- Matplotlib / Seaborn
- Scikit-learn

You should understand **what each library does and when to use it**, without diving deeply into theory at this stage.

## 4.1. NumPy – The Foundation of Numerical Computing

### 4.1.1. What is NumPy? Why use NumPy in Machine Learning?

NumPy helps you perform **numerical operations** on data. With NumPy, you can **convert different types of data into numerical form**.

In Machine Learning, data is sometimes not in numerical form, so NumPy plays a very important role in processing and **representing all input data as numbers** so that the machine can learn from it.

### 4.1.2. Examples with NumPy

#### Example 1: Creating a numerical array

```python
import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
```

#### Example 2: Matrix multiplication

```python
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

C = A @ B   # Matrix multiplication
print(C)
```

## 4.2. Pandas – Working with Tabular Data

### 4.2.1. What are Pandas and DataFrame?

In Machine Learning, input data usually exists in **tabular form** (similar to Excel, CSV, SQL tables).  
Pandas is an **open-source** Python library that is widely used to **read, process, clean, and analyze data** before feeding it into a Machine Learning model.

The most important data structure in Pandas is the **DataFrame**, which is a table consisting of:

- **Rows**: each row is a data record
- **Columns**: each column is a feature

Example of a DataFrame:

| id  | name | age | salary |
| --- | ---- | --- | ------ |
| 1   | An   | 22  | 500    |
| 2   | Binh | 35  | 1200   |
| 3   | Chi  | 28  | 800    |
| 4   | Dung | 42  | 1500   |

A DataFrame is very similar to an Excel file, making it **easy to read, easy to edit, and convenient for data analysis**.

In practice, real-world data often **contains missing values**, **incorrect data**, or **invalid formats**.  
Therefore, we must **clean the data before training the model**.

Example of a real-world dataset:

| name | age   | salary |
| ---- | ----- | ------ |
| An   | 22    | 500    |
| Binh |       | 1200   |
| Chi  | 28    | ???    |
| Dung | forty | 1500   |

### 4.2.2. Examples with Pandas

#### Example 1: Creating a DataFrame (Excel-like)

```python
import pandas as pd

data = {
    "name": ["An", "Binh", "Chi", "Dung"],
    "age": [22, 35, 28, 42],
    "salary": [500, 1200, 800, 1500]
}

df = pd.DataFrame(data)
print(df)
```

Output:

```
   name  age  salary
0   An   22     500
1  Binh  35    1200
2  Chi   28     800
3  Dung  42    1500
```

#### Example 2: Quick statistics on a DataFrame

```python
df.describe()
```

Output:

```
       age    salary
mean   31.75  1000
min    22     500
max    42     1500
```

## 4.3. Matplotlib / Seaborn – Data Visualization

### 4.3.1. What are Matplotlib and Seaborn?

Matplotlib and Seaborn are the two most popular libraries in Python for creating charts and plots from analyzed data.  
If we only understand data through numeric tables, it can be very difficult, so visualizing these tables helps us observe patterns and draw conclusions more easily.

### 4.3.2. Examples with Matplotlib / Seaborn

#### Example 1: Bar chart

```python
import matplotlib.pyplot as plt

names = ["An", "Binh", "Chi", "Dung"]
salary = [500, 1200, 800, 1500]

plt.bar(names, salary)
plt.xlabel("Name")
plt.ylabel("Salary")
plt.title("Salary Comparison")
plt.show()
```

<figure>
  <img src="../image/libraries_ml.png" alt="" width="700">
  <figcaption><em></em></figcaption>
</figure>

#### Example 2: Salary distribution

```python
import seaborn as sns

sns.histplot(salary, bins=10)
plt.title("Salary Distribution")

plt.show()
```

<figure>
  <img src="../image/libraries_ml_2.png" alt="" width="700">
  <figcaption><em></em></figcaption>
</figure>

## 4.4. Scikit-learn – Basic Machine Learning Library

### 4.4.1. What is Scikit-learn? When is it used?

Scikit-learn (sklearn) is the most popular Machine Learning library in Python, providing **basic ML algorithms** and **tools that support the entire model training process**.

Scikit-learn is commonly used when:

- Data has already been **cleaned and converted into numerical form** (using NumPy and Pandas)
- You need to **train, evaluate, and compare models**
- Solving classical Machine Learning problems:
  - Regression
  - Classification
  - Clustering

---

### 4.4.2. Basic Machine Learning workflow with Scikit-learn

A basic Machine Learning task with Scikit-learn usually includes the following steps:

1. Prepare the data (X, y)
2. Split the dataset into training and testing sets
3. Choose a model
4. Train the model
5. Evaluate the results

---

### 4.4.3. Examples with Scikit-learn

#### Example 1: Linear Regression

Predicting **salary based on age** (simple illustrative example).

```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Data
X = np.array([[22], [35], [28], [42]])  # age
y = np.array([500, 1200, 800, 1500])    # salary

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict
pred = model.predict([[30]])
print(pred)
```

---

#### Example 2: Classification

Simple example: **pass / fail classification** based on scores.

```python
from sklearn.linear_model import LogisticRegression

# Data
X = [[5], [6], [7], [8], [9]]
y = [0, 0, 0, 1, 1]  # 0: fail, 1: pass

model = LogisticRegression()
model.fit(X, y)

print(model.predict([[7.5]]))
```

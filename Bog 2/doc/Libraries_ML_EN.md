# 4. Understanding Python Libraries

Python provides a rich ecosystem of libraries for **data processing, analysis, and visualization**.  
A library is a collection of pre-built functions and objects that you can reuse instead of writing everything from scratch.

When starting Machine Learning with Python, there are **four essential libraries** you must know:

- NumPy
- Pandas
- Matplotlib / Seaborn
- Scikit-learn

The goal is to understand **what each library does and when to use it**, without diving deeply into theory.

---

## 4.1. NumPy – The Foundation of Numerical Computing

### 4.1.1. What is NumPy? Why is NumPy used in Machine Learning?

NumPy helps you perform **numerical and mathematical operations** on data.  
With NumPy, you can **convert many different types of data into numerical form**.

In Machine Learning, data is not always numerical by nature.  
Therefore, NumPy plays a crucial role in **processing and representing all data as numbers**, allowing machines to learn from it.

---

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

---

## 4.2. Pandas – Working with Tabular Data

### 4.2.1. What are Pandas and DataFrames?

| id  | name | age | salary |
| --- | ---- | --- | ------ |
| 1   | An   | 22  | 500    |
| 2   | Bình | 35  | 1200   |
| 3   | Chi  | 28  | 800    |
| 4   | Dũng | 42  | 1500   |

Pandas is an **open-source library** used for **data analysis and data manipulation**.  
With Pandas, you work with **DataFrames** — a tabular data structure **similar to Excel spreadsheets**, which is very convenient for reading, editing, and analyzing data.

In real-world datasets, data is often **missing**, **incorrect**, or **in the wrong format**.  
Therefore, we must **clean the data before training a machine learning model**.

| name | age   | salary |
| ---- | ----- | ------ |
| An   | 22    | 500    |
| Bình |       | 1200   |
| Chi  | 28    | ???    |
| Dũng | forty | 1500   |

---

### 4.2.2. Examples with Pandas

#### Example 1: Creating a DataFrame (similar to Excel)

```python
import pandas as pd

data = {
    "name": ["An", "Bình", "Chi", "Dũng"],
    "age": [22, 35, 28, 42],
    "salary": [500, 1200, 800, 1500]
}

df = pd.DataFrame(data)
print(df)
```

**Output:**

```
    name  age  salary
0     An   22     500
1   Bình   35    1200
2    Chi   28     800
3   Dũng   42    1500
```

#### Example 2: Quick statistics on a DataFrame

```python
df.describe()
```

**Output:**

```
            age   salary
mean        31.75  1000
min         22     500
max         42     1500
```

---

## 4.3. Matplotlib / Seaborn – Data Visualization

### 4.3.1. What are Matplotlib and Seaborn?

Matplotlib and Seaborn are two of the most popular libraries in Python for data visualization.  
They allow you to create charts and plots from analyzed data.

Understanding data only through tables can be difficult.  
Therefore, visualization helps us **observe patterns and draw conclusions more easily**.

---

### 4.3.2. Examples with Matplotlib / Seaborn

#### Example 1: Bar chart

```python
import matplotlib.pyplot as plt

names = ["An", "Bình", "Chi", "Dũng"]
salary = [500, 1200, 800, 1500]

plt.bar(names, salary)
plt.xlabel("Name")
plt.ylabel("Salary")
plt.title("Salary comparison by person")
plt.show()
```

<figure>
  <img src="../image/libraries_ml.png" alt="Bar chart example" width="700">
  <figcaption><em>Salary comparison bar chart</em></figcaption>
</figure>

#### Example 2: Salary distribution (Histogram)

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(salary, bins=10)
plt.title("Salary distribution")
plt.show()
```

<figure>
  <img src="../image/libraries_ml_2.png" alt="Histogram example" width="700">
  <figcaption><em>Salary distribution histogram</em></figcaption>
</figure>

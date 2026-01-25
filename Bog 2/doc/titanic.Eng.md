# Chapter 5: Titanic Survival Prediction - From Raw Data to a Complete Model

Continuing our Machine Learning series, today we will dive into a classic real-world project. Have you ever wondered how a machine can predict the future based on data from the past?

We will implement the project: **Classifying Titanic Passenger Survival.**

This is a typical **Classification** problem: Based on input features such as age, gender, and ticket class, the AI model predicts whether a passenger "Survived" (1) or "Did Not Survive" (0).

> **🔗 Source Code Link (Google Colab):** [ML Project: Titanic Classification](https://colab.research.google.com/drive/1fchJJYixzJrIB0ngobCw6H7H4mHriOJc)

To make this project successful, we will follow the 5 standard steps of the Machine Learning workflow:

1. **Data Collection:** Using the famous Titanic Dataset.
2. **Data Cleaning:** Handling missing values and normalizing data.
3. **Data Splitting:** Separating the Training and Testing sets.
4. **Training:** Utilizing the powerful **Random Forest** algorithm.
5. **Evaluation:** Checking model performance through technical metrics.

---

## Step 1: Data Collection & Exploration

First, we import the necessary libraries: `pandas`, `seaborn`, and `matplotlib`. We will load the sample data directly from the `seaborn` library.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the titanic dataset
df = sns.load_dataset('titanic')

# View the first 5 rows to understand the data structure
print("Initial Raw Data:")
print(df.head())

# Check preliminary information (number of rows, data types, missing values)
print("\nData Info:")
print(df.info())

```

---

## Step 2: Data Cleaning & Preprocessing

In Machine Learning, there is a golden rule: **Garbage In, Garbage Out**. Computers do not understand text like "male/female" and cannot perform calculations on empty cells (NaN).

**Issues to handle:**

* **Missing Values:** Fill missing ages with the **Median** to avoid bias caused by outliers.
* **Redundant Data:** Remove columns that do not contribute much to prediction, such as `deck`, `embark_town`, and `alive`.
* **Encoding:** Convert text-based data into numerical format.

```python
# 1. HANDLE MISSING DATA
df['age'] = df['age'].fillna(df['age'].median())
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])

# 2. REMOVE UNNECESSARY COLUMNS
df = df.drop(columns=['deck', 'embark_town', 'alive', 'class', 'who', 'adult_male'])

# 3. DATA ENCODING
df['sex'] = df['sex'].map({'male': 0, 'female': 1})
df = pd.get_dummies(df, columns=['embarked'], drop_first=True)

print("\nCleaned Data:")
print(df.head())

```

---

## Step 3: Train/Test Split

We split the data using an **80:20** ratio to ensure the model does not simply "memorize" the answers (overfitting):

* **Train Set (80%):** Used to train the model.
* **Test Set (20%):** Used for an objective evaluation of the predictive power.

```python
from sklearn.model_selection import train_test_split

X = df.drop('survived', axis=1) 
y = df['survived']               

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

```

---

## Step 4: Model Training

We will use the **Random Forest Classifier**. This is an extremely powerful and popular algorithm in Machine Learning.

> **The Concept:** Imagine that instead of asking for the opinion of a single expert, you ask 100 different people (representing 100 **Decision Trees**). Each person makes a prediction, and the final result is based on the majority vote. This approach helps the model minimize errors and operate more stably.

```python
from sklearn.ensemble import RandomForestClassifier

# Initialize the model with 100 decision trees
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Start the training process (machine learns from the Train data)
print("Training the model...")
model.fit(X_train, y_train)
print("Training complete!")

```

---

## Step 5: Evaluation

Once the machine has finished "learning," we will test the model on the `X_test` set (data the machine has never seen before) and compare the predicted results with the actual answers in `y_test`.

**Key Evaluation Metrics:**

1. **Accuracy:** The ratio of correct predictions to the total number of passengers.
2. **Precision:** Of all passengers the machine predicted as "Survived," what percentage actually survived?
3. **Recall:** Of all actual survivors, what percentage did the machine successfully find?

```python
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Let the model predict on the test set
y_pred = model.predict(X_test)

# 1. Calculate Accuracy
acc = accuracy_score(y_test, y_pred)
print(f"\nOverall Accuracy: {acc*100:.2f}%")

# 2. Detailed Report (Precision, Recall, F1-score)
print("\nDetailed Report:")
print(classification_report(y_test, y_pred))

# 3. Confusion Matrix
print("\nConfusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

```

The Titanic project is not just a simple prediction task; it is an excellent introductory lesson on the data processing workflow in AI. We have seen that: **Clean Data + Suitable Algorithm = Reliable Results.**

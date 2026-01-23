## 2. Categories of Machine Learning Algorithms

### 2.1 Supervised Learning

Supervised learning is a machine learning paradigm in which a model is trained on a **labeled dataset**. Each data sample consists of an **input** and a corresponding desired **output**. The objective of the model is to learn a mapping function from inputs to outputs so that it can accurately predict the labels of previously unseen data.

**Example:**  
In the task of classifying images of cats and dogs, the training dataset consists of thousands of images that are already labeled as either `“cat”` or `“dog”`. These images are provided to an algorithm along with their corresponding labels. After training, the algorithm produces a model—a function whose input is an image and whose output is a label. When the model receives a new image that it has never seen before, it predicts whether the image contains a cat or a dog.

<figure>
  <img src="./images/supervised learning.png" 
       alt="supervised learning" 
       width="700">
  <figcaption>
    <em>Figure 2.1: Supervised learning pipeline.</em>
  </figcaption>
</figure>


**Applications:**  
Supervised learning is widely used in prediction and decision-making systems such as financial fraud detection, medical diagnosis, image recognition, and natural language processing.

Supervised learning algorithms can be further divided into two main categories:

---

#### 2.1.1 Classification

**Classification** is a supervised learning problem in which the output is a discrete label. The goal of the model is to assign each input sample to one of a predefined set of classes.

**Examples:**  
Gmail determining whether an email is spam, and credit institutions assessing whether a customer is likely to repay a loan are typical classification problems.

**Representative algorithms:**  
- Logistic Regression  
- k-Nearest Neighbors (k-NN)  
- Support Vector Machine (SVM)  
- Decision Tree  

---

#### 2.1.2 Regression

**Regression** is a supervised learning problem in which the output is a continuous value. The objective of the model is to predict a numerical quantity based on the input data.

**Example:**  
Estimating the price of a house given its area, number of bedrooms, and distance from the city center.

**Representative algorithms:**  
- Linear Regression  
- Ridge Regression  
- Lasso Regression  
- Decision Tree Regression  

---

### 2.2 Unsupervised Learning

**Unsupervised learning** is a machine learning paradigm in which the training data does not contain labels. The algorithm relies on the underlying structure of the data to perform tasks such as clustering or dimensionality reduction, which facilitate data analysis, storage, and computation.

Supervised learning is suitable when labeled data is available and the goal is accurate prediction. In contrast, unsupervised learning is used when data is unlabeled, with the aim of discovering hidden structures or patterns within the data.

**Applications:**  
Unsupervised learning is commonly applied in exploratory data analysis, customer segmentation, anomaly detection, and data preprocessing prior to supervised learning.

Unsupervised learning problems can be further divided into the following categories:

---

#### 2.2.1 Clustering

**Clustering** is the task of partitioning a dataset **X** into smaller groups based on the similarity among data points within each group.

**Example: Customer segmentation**  
Suppose we have data from thousands of customers, including features such as age, income, purchase frequency, and average transaction value. This dataset does not contain labels indicating customer groups. An unsupervised learning algorithm is applied to automatically divide customers into clusters based on feature similarity. The resulting clusters help businesses identify groups of customers with similar behaviors without prior labeling.

<figure>
  <img src="./images/clustering.png" 
       alt="clustering" 
       width="700">
  <figcaption>
    <em>Figure 2.2: Customer segmentation.</em>
  </figcaption>
</figure>

**Representative algorithms:**  
- K-means  
- Hierarchical Clustering  
- DBSCAN  

---

#### 2.2.2 Association Rules

**Association rule** learning is a form of unsupervised learning that aims to discover frequent patterns or relationships among items in a dataset without requiring labeled outputs.

**Example:**  
Customers who purchase clothing often tend to buy watches or belts; viewers who watch Spider-Man movies are likely to also watch Batman movies. Such patterns can be used to build recommendation systems that encourage additional purchases or content consumption.

**Representative algorithms:**  
- Apriori  
- FP-Growth  
- Eclat  

---

### 2.3 Semi-supervised Learning

**Semi-supervised learning** is a machine learning approach that combines supervised and unsupervised learning. The training dataset contains a small portion of labeled data and a large portion of unlabeled data. The goal is to leverage the unlabeled data to improve learning performance compared to using only labeled data.

**Example:**  
In handwritten digit recognition, suppose only a small number of digit images are labeled correctly, while most images are unlabeled. A semi-supervised learning algorithm uses the labeled images to guide the learning process and exploits the structure of the unlabeled data to improve prediction accuracy on new images.

**Applications:**  
Semi-supervised learning is widely used in problems where labeled data is scarce or expensive to obtain. It is particularly effective in fields such as image recognition, natural language processing, and biomedical data analysis, where labeling often requires domain experts.

**Representative algorithms:**  
- Self-training (Pseudo-labeling)  
- Label Propagation  

---

### 2.4 Reinforcement Learning

**Reinforcement learning** is a machine learning paradigm in which an agent learns to make decisions through direct interaction with an environment. Instead of learning from labeled data, the agent receives rewards or penalties after each action and gradually learns an optimal policy that maximizes cumulative long-term reward.

**Example: Robot navigation**  
Consider a robot placed in an environment with obstacles and a target location. The robot is not provided with the correct path in advance; instead, it receives rewards when moving closer to the target and penalties when colliding with obstacles or taking inefficient actions. Through continuous interaction and trial-and-error, the robot learns an optimal strategy for reaching the goal efficiently.

**Applications:**  
Reinforcement learning is well suited for sequential decision-making problems and is widely applied in autonomous systems and dynamic environments where labeled data is unavailable.

**Representative algorithms:**  
- Q-learning  
- SARSA  
- Deep Q-Network (DQN)

# Welcome to the Fundamentals of Machine Learning

Welcome to your journey into the fascinating world of Machine Learning! 👋🤖

## About This Blog
We are living in an era where **Machine Learning (ML)** is no longer just a distant concept found in sci-fi movies. It is quietly but actively shaping our daily lives. From movie recommendations on Netflix and voice assistants like Siri or Google Assistant, to breakthroughs in medical diagnostics and autonomous vehicles—Machine Learning is everywhere.

But **what exactly is Machine Learning?** How can a machine "learn" from data without a human explicitly programming every line of code? And more importantly, **where should you start** in this vast ocean of knowledge?

This blog was created to help you decode these questions. Here, I will share a series of articles ranging from basic to advanced topics, simplified so that anyone can understand. Whether you are a student, a developer looking to pivot into AI, or simply a tech enthusiast, I hope you will find valuable insights at this stop on your journey.

# Chapter 1: What is Machine Learning?

## 1. Introduction
Machine Learning has emerged as one of the most transformative technologies of the 21st century. It has fundamentally changed how we approach problem-solving: instead of rigid programming, we are now teaching computers how to learn.

From relatable applications like medical diagnosis, virtual assistants, and self-driving cars to macro-level challenges like climate modeling, Machine Learning has become an indispensable tool in modern computer science.

```mermaid
graph LR
    A["💾 1. Data Collection<br/>and Processing"] --> B["🧠 2. Model<br/>Training"]
    B --> C["🎯 3. Prediction<br/>and Inference"]
    C --> D["📈 4. Evaluation<br/>and Optimization"]
    D -.->|Improve Data| A
    D -.->|Refine Model| B
    
    style A fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style B fill:#e8f5e9,stroke:#388e3c,stroke-width:2px
    style C fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style D fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
 ```
## 2. Definitions and Basic Concepts

### 2.1 Definition
Machine Learning is a subset of **Artificial Intelligence (AI)** focused on building algorithms and statistical models that enable computers to **"learn"** from data. Instead of being explicitly programmed for every specific scenario, the system improves its performance over time through experience.

### 2.2 Formal Definition (Tom Mitchell)
Mathematically and scientifically, a Machine Learning problem is standardly defined as follows:

> "A computer program is said to learn from experience **$E$** with respect to some class of tasks **$T$** and performance measure **$P$**, if its performance at tasks in **$T$**, as measured by **$P$**, improves with experience **$E$**."

**A Simple Example (Spam Filter):**
* **Task ($T$):** Classifying emails as "Spam" or "Not Spam".
* **Experience ($E$):** Reviewing emails that have been previously labeled by users.
* **Performance ($P$):** The percentage of emails correctly classified.

### 2.3 The Paradigm Shift
The biggest difference between Traditional Programming and Machine Learning lies in the **flow of data and rules**:

* **Traditional Programming:** Humans must understand the problem and write specific rules (logic) for the computer to process data and produce results.
$$\text{Data} + \text{Rules (Code)} \rightarrow \text{Result}$$

* **Machine Learning:** The computer looks at the Data and the desired Output, then figures out the rules (the model) itself.
$$\text{Data} + \text{Output} \rightarrow \text{Rules (Model)}$$

**Core Objective:**
The goal is to find a function $f: X \to Y$ that maps input $X$ to output $Y$ as accurately as possible. Most importantly, this function must be capable of **generalization**—meaning it performs well even on new, unseen data that was not used during training.


## Chapter 2: Categories of Machine Learning Algorithms

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

 

#### 2.1.1 Classification

**Classification** is a supervised learning problem in which the output is a discrete label. The goal of the model is to assign each input sample to one of a predefined set of classes.

**Examples:**  
Gmail determining whether an email is spam, and credit institutions assessing whether a customer is likely to repay a loan are typical classification problems.

**Representative algorithms:**  
- Logistic Regression  
- k-Nearest Neighbors (k-NN)  
- Support Vector Machine (SVM)  
- Decision Tree  

 

#### 2.1.2 Regression

**Regression** is a supervised learning problem in which the output is a continuous value. The objective of the model is to predict a numerical quantity based on the input data.

**Example:**  
Estimating the price of a house given its area, number of bedrooms, and distance from the city center.

**Representative algorithms:**  
- Linear Regression  
- Ridge Regression  
- Lasso Regression  
- Decision Tree Regression  

 

### 2.2 Unsupervised Learning

**Unsupervised learning** is a machine learning paradigm in which the training data does not contain labels. The algorithm relies on the underlying structure of the data to perform tasks such as clustering or dimensionality reduction, which facilitate data analysis, storage, and computation.

Supervised learning is suitable when labeled data is available and the goal is accurate prediction. In contrast, unsupervised learning is used when data is unlabeled, with the aim of discovering hidden structures or patterns within the data.

**Applications:**  
Unsupervised learning is commonly applied in exploratory data analysis, customer segmentation, anomaly detection, and data preprocessing prior to supervised learning.

Unsupervised learning problems can be further divided into the following categories:

 

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

 

#### 2.2.2 Association Rules

**Association rule** learning is a form of unsupervised learning that aims to discover frequent patterns or relationships among items in a dataset without requiring labeled outputs.

**Example:**  
Customers who purchase clothing often tend to buy watches or belts; viewers who watch Spider-Man movies are likely to also watch Batman movies. Such patterns can be used to build recommendation systems that encourage additional purchases or content consumption.

**Representative algorithms:**  
- Apriori  
- FP-Growth  
- Eclat  

 

### 2.3 Semi-supervised Learning

**Semi-supervised learning** is a machine learning approach that combines supervised and unsupervised learning. The training dataset contains a small portion of labeled data and a large portion of unlabeled data. The goal is to leverage the unlabeled data to improve learning performance compared to using only labeled data.

**Example:**  
In handwritten digit recognition, suppose only a small number of digit images are labeled correctly, while most images are unlabeled. A semi-supervised learning algorithm uses the labeled images to guide the learning process and exploits the structure of the unlabeled data to improve prediction accuracy on new images.

**Applications:**  
Semi-supervised learning is widely used in problems where labeled data is scarce or expensive to obtain. It is particularly effective in fields such as image recognition, natural language processing, and biomedical data analysis, where labeling often requires domain experts.

**Representative algorithms:**  
- Self-training (Pseudo-labeling)  
- Label Propagation  

 

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

# Chapter 4: Machine Learning Courses for Beginners

For those who are looking for a course with a clear learning path, well-structured guidance, but do not know where to start and do not want to feel overwhelmed by a large amount of knowledge.

Here, we introduce **Machine Learning** courses suitable for beginners based on the following criteria:

- Easy-to-understand explanations with a clear roadmap  
- Hands-on practice that leads to real results  
- Large and active communities with good support  

# Chapter 3: A 4-Step Roadmap for Beginners

For beginners, the term "Machine Learning" is often shrouded in a fog of dry math and complex algorithms. This can easily lead to intimidation. However, the truth is you don't need to be a math genius to get started.

With the right approach—balancing theory and practice—you can absolutely build a solid foundation in just a few months. Below is a standard 4-step roadmap commonly recommended by top data science programs and experts.

## 3.1. Step 1: Prepare Your Toolkit – Math & Programming

Machine Learning is the intersection of Computer Science and Statistics. You need to understand the nature of the tools you are using rather than just rote learning.

### 📐 Mathematics: The Foundation of Thinking
You don't need to relearn an entire college curriculum. Instead, focus on three key pillars that apply directly to ML:

* **Linear Algebra:** This is the language of data.
    * *Why it matters:* Computers don't "see" images or text; they see numbers arranged in matrices.
    * *Focus:* Vectors, Matrices, Matrix Multiplication, and Transformations. This is the basis for understanding how Neural Networks operate.
* **Calculus:** The engine of optimization.
    * *Why it matters:* It helps you understand how a model adjusts itself to minimize error.
    * *Focus:* Derivatives and the Chain Rule. The concept of **Gradient Descent**—the most critical optimization algorithm—is built entirely on calculus.
* **Probability & Statistics:** Handling uncertainty.
    * *Why it matters:* It helps you understand your data, evaluate prediction reliability, and avoid being misled by random noise.
    * *Focus:* Gaussian Distribution, Expectations, Variance, Bayes' Theorem, and Hypothesis Testing.

### 💻 Programming: The Execution Tool
**Python** is currently the #1 choice due to its simple syntax and massive ecosystem of libraries.
* **Basics:** Master variables, functions, loops, and data structures (Lists, Dictionaries, Tuples).
* **The Power Trio:**
    * **NumPy:** High-performance array and matrix computing.
    * **Pandas:** The "Excel for programmers"—used for reading, cleaning, and manipulating tabular data.
    * **Matplotlib / Seaborn:** Data visualization tools to uncover insights before feeding data into a model.

## 3.2. Step 2: Master the Mindset & Introductory Algorithms

Before diving into code, learn to think like an ML engineer. You need to clearly distinguish between **Supervised Learning** (where data has labels/answers) and **Unsupervised Learning** (where the model must find the structure itself).

At the same time, familiarize yourself with the "enemies" of every model:
* **Overfitting:** The model memorizes the training data but fails on new data.
* **Underfitting:** The model is too simple to capture the underlying patterns of the data.

Next, start with these 4 "classic" algorithms:

### 1. Linear Regression
* **Type:** Supervised Learning (Regression).
* **Essence:** Drawing a straight line that best fits the data points.
* **Applications:** Predicting housing prices, sales revenue, tomorrow's temperature.
* **Key Takeaway:** Understanding the **Loss Function** and how to minimize error.

### 2. Logistic Regression
* **Type:** Supervised Learning (Classification).
* **Essence:** Despite the name "Regression," it's used for classification. It uses the Sigmoid function to squash results into a (0, 1) range, representing probability.
* **Applications:** Spam filters, predicting customer churn.
* **Key Takeaway:** Understanding the **Decision Boundary**.

### 3. Decision Tree
* **Type:** Supervised Learning (Classification & Regression).
* **Essence:** A series of Yes/No questions to split data, similar to a flowchart.
* **Applications:** Medical diagnosis (symptom-based), credit risk assessment.
* **Key Takeaway:** Intuitive and interpretable, but prone to Overfitting. It serves as the foundation for powerful models like Random Forest.

### 4. K-Means Clustering
* **Type:** Unsupervised Learning.
* **Essence:** Grouping similar data points into clusters without knowing labels beforehand.
* **Applications:** Customer Segmentation, image compression.
* **Key Takeaway:** How machines automatically discover hidden structures in chaotic data.

## 3.3. Step 3: Hands-on with Scikit-Learn

Theory won't stick without practice. This is where you use **Scikit-Learn**—the most popular ML library for beginners.

* **Standard Workflow:**
    1.  Data Preprocessing (Cleaning, Normalization, handling missing values).
    2.  Splitting Data: Train set (to learn) vs. Test set (to evaluate).
    3.  Training the model (`model.fit()`).
    4.  Evaluating results (`model.predict()` and accuracy metrics).
* **Suggested Projects:** Titanic Survival Prediction (Kaggle), Iris Flower Classification, Boston Housing Price Prediction.

## 3.4. Step 4: Expand to Deep Learning & Advanced Topics

Once you have mastered Classical ML algorithms, you are ready for the next big leap: **Deep Learning**.

* Learn about **Artificial Neural Networks (ANNs)**: Simulating how the human brain works.
* Get comfortable with advanced frameworks: **TensorFlow** or **PyTorch**.
* Explore specialized fields:
    * *Computer Vision:* Processing images and video.
    * *NLP (Natural Language Processing):* Processing text and voice (like ChatGPT).

# Chapter 4: Recommended Machine Learning Courses for Beginners

For those of you looking for a clear path and structured guidance—but don't know where to start and want to avoid getting overwhelmed by the sheer volume of information out there—we've got you covered.

We will introduce you to **Machine Learning** courses specifically tailored for beginners based on the following criteria:

* Easy-to-understand explanations with a clear roadmap.
* Hands-on exercises to produce real results.
* A large community with strong support.

## 4.1. Machine Learning Specialization – Andrew Ng  
**(DeepLearning.AI / Coursera)**

This is almost the safest choice for anyone who is just starting to explore Machine Learning. This course series has been rebuilt and expanded into **three courses** (instead of the original single classic ML course), covering everything from fundamental concepts to important real-world topics.

It also includes many practical exercises, organized by sections and clear learning paths, helping learners understand the theory immediately after studying it.

Andrew Ng’s greatest strength is his teaching approach: helping beginners **understand the ML mindset first**, before moving on to code and algorithmic details. His explanations are clear, logical, and easy to follow.

This course is designed for:

- Learners who want to study ML in a solid and systematic way with a clear starting roadmap  
- Those who want to understand the core concepts and develop decision-making intuition  

**Note:**  To learn this course effectively, you should have basic knowledge of **Python**. Alternatively, you should plan to study Python in parallel so that you can complete the exercises more effectively.

 

## 4.2. Google Machine Learning Crash Course (MLCC) – *Free*

If you already have some basic Python knowledge and want to move fast, **MLCC** is an excellent choice. This is a fast-paced course that combines learning with hands-on practice, and it is easy to follow thanks to Google’s concise presentation of core concepts.

What makes MLCC different is that it focuses on **exactly what you need to get started**:

- Short, beginner-friendly reading materials  
- Short videos and interactive widgets (instead of text-only content)  
- Multiple-choice questions for self-assessment  

Notably, MLCC has received major content updates recently, providing a modern and up-to-date approach that keeps pace with current developments. The course is suitable for learners with basic Python knowledge and high-school-level mathematics. If you do not have these yet, do not worry—the course does not set high barriers, and Google provides a clear *“Prerequisites & prework”* section for beginners.

**Strengths:**

- Concise content with interactive exercises  
- Very effective for filling gaps in foundational knowledge  

 

## 4.3. Kaggle Learn – Intro to Machine Learning (*Free*)

If you want the feeling of **being able to build something right after learning**, Kaggle Learn is a great option for beginners.

This is a **micro-course** format with short, easy-to-understand lessons that focus directly on key ideas and early practice. The course is designed to help you grasp core concepts and build your first model in a very short time  
(the suggested duration is about **3 hours**).

Kaggle also provides a clear follow-up learning path:

- **Intermediate Machine Learning** – common issues encountered in real projects  
- **Learn Pandas** – strengthening data manipulation skills  
- **Feature Engineering** – learning how to create better features to improve model performance  

This course is suitable for:

- Beginners who want to see results quickly  
- Learners who prefer short lessons with immediate practice instead of heavy theory  
- Those who want to become familiar with the ML workflow *(train → validate → improve)* before diving deeper  

Because Kaggle emphasizes rapid hands-on practice, it does **not focus heavily on foundational theory**. Therefore, we still strongly recommend combining it with the courses mentioned above to build a solid and well-rounded understanding.

 

## 4.4. Conclusion

In short, if you’re just getting started with Machine Learning, don’t try to learn everything at once. Pick one main learning path to build a solid foundation, and pair it with a hands-on course to sharpen your practical skills. You can begin quickly with **Kaggle Intro to ML**, accelerate your fundamentals with **Google MLCC**, and then build a strong, structured base with the **Machine Learning Specialization (Andrew Ng)**. Most importantly, as you learn each concept, try to turn it into a small project—don’t focus only on theory. That’s the fastest way to make real progress in ML.

## References

1. [How Do Chatbots Work? – BotsCrew](https://botscrew.com/blog/what-are-bots/)
2. Building Vietnamese Chatbot using LLMs and RLHF – AI Vietnam
3. [Rubric (academic) - Wikipedia](https://en.wikipedia.org/wiki/Rubric_\(academic\))
4. [ConvoMem Benchmark: Why Your First 150 Conversations Don’t Need RAG](https://arxiv.org/html/2511.10523)
5. [Introduction | Ragas](https://docs.ragas.io/en/v0.1.21/index.html)
6. [OpenAI. (2024). "GPT-4 Technical Report"](https://arxiv.org/html/2511.10523)
7. [Lewis et al. (2020). "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"](https://arxiv.org/html/2511.10523)
8. [Hu et al. (2021). "LoRA: Low-Rank Adaptation of Large Language Models"](https://arxiv.org/html/2511.10523)
9. [Yao et al. (2023). "ReAct: Synergizing Reasoning and Acting in Language Models"](https://arxiv.org/html/2511.10523)
10. [LangChain Documentation. (2024). "Building Production-Ready RAG Systems"](https://arxiv.org/html/2511.10523)
 


 
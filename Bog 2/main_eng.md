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
 


 
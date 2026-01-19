# 2. How Chatbots Work

## 2.1. Overview of the Chatbot Processing Pipeline

In general, an AI chatbot operates through a **processing pipeline** consisting of multiple consecutive steps.  
Each step plays a specific role, enabling the chatbot to **understand user queries and generate appropriate responses**.

The overall workflow of an AI chatbot is illustrated in **Figure 2.1** and can be described through the following steps.

<figure>
  <img src="../image/Pasted image 20260116172851.png" alt="Chatbot processing pipeline" width="700">
  <figcaption><em>Figure 2.1: Basic processing pipeline of an AI chatbot.</em></figcaption>
</figure>

---

### 🔹 Step 1: User Input

The process begins when the **user submits a query or request** to the chatbot.

User input can take various forms, most commonly:

- **Text** (typed queries)
- **Speech** (for voice assistants such as Google Assistant or Siri)

**Examples:**

> “What is the weather like today?”  
> “I would like to schedule an appointment.”

At this stage, the chatbot **does not yet understand the meaning** of the query; it only receives **raw input data**.

---

### 🔹 Step 2: User Request Analysis

_(Analyze user’s request)_

After receiving the input, the chatbot performs **query analysis** using **Natural Language Processing (NLP)** techniques.

The objectives of this step include:

- Text cleaning
- Tokenization
- Language normalization
- Reducing noise caused by spelling errors or variations in expression

**Example:**

> “Could you tell me if it is going to rain today?”

The question is analyzed as a **weather-related request**, with key information such as **today** and **rain**.

---

### 🔹 Step 3: Intent and Entity Recognition

_(Identify intent and entities)_

In this step, the chatbot identifies two critical components:

- **Intent:** what the user wants to do
- **Entities:** important information mentioned in the query

**Example:**

| Component | Value           |
| --------- | --------------- |
| Intent    | Weather inquiry |
| Entities  | Date: today     |

Accurate identification of **intents** and **entities** enables the chatbot to **respond correctly and contextually**, even when users express the same request in different ways.

---

### 🔹 Step 4: Response Generation

_(Compose reply)_

Based on the identified intent, the chatbot proceeds to:

- Query relevant data sources (if applicable)
- Apply predefined rules or business logic
- Or utilize AI models to generate a response

The final output is a response that is **natural, easy to understand, and contextually appropriate**.

**Example:**

> “There will be light rain this afternoon. You may want to bring an umbrella.”

---

## 2.2. Types of Chatbots and Their Operating Mechanisms

Based on how responses are processed and generated, chatbots can be categorized into **three main types**:

- **Rule-based chatbots**
- **Retrieval-based chatbots**
- **Generative chatbots**

Each type differs in terms of **operating mechanisms**, **intelligence level**, and **application scope**.

---

### 2.2.1. Rule-based Chatbots

**Rule-based chatbots** operate based on a predefined set of **rules and dialogue scripts**.  
They rely on structures such as **IF–ELSE conditions** or **decision trees** to determine appropriate responses.

These chatbots are typically used in **simple systems with limited conversational scope**.

---

### 2.2.2. Retrieval-based Chatbots

**Retrieval-based chatbots** use AI techniques to **select the most appropriate response** from a predefined dataset.

Key characteristics include:

- No generation of new responses
- Retrieval of the closest matching answer from a database
- Higher response consistency compared to rule-based chatbots

---

### 2.2.3. Generative Chatbots

**Generative chatbots** have the ability to **generate entirely new responses**, rather than selecting from predefined ones.

These chatbots typically rely on **Large Language Models (LLMs)**, enabling more flexible and natural conversational interactions.

---

## References

1. [How Do Chatbots Work? – BotsCrew](https://botscrew.com/blog/what-are-bots/)
2. Building Vietnamese Chatbot using LLMs and RLHF – AI Vietnam

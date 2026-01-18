# Overview of Retrieval-Based Chatbots

## 1. Definition and Foundation

A **retrieval-based chatbot** is a method of building chatbots where the system does not generate new answers autonomously. Instead, it selects the most appropriate response from a pre-prepared dataset or knowledge base. This selection process is based on the similarity between the user's query and stored question-answer pairs.

Compared to rule-based chatbots, retrieval-based chatbots are more flexible because they do not rely entirely on rigid conditions. However, unlike **generative chatbots**, retrieval-based systems ensure a high level of content control since they only use pre-existing responses. Consequently, this method is widely applied in enterprise chatbot systems, particularly in customer support and information consulting.

## 2. Operational Workflow
Although there are various variations, retrieval-based chatbots generally follow a common workflow consisting of the following steps:

1. **Input Reception:** The user enters a question or request via the chatbot interface.
2. **Natural Language Preprocessing:** The system normalizes the input text, such as converting it to lowercase, removing special characters, or tokenizing words.
3. **Analysis and Understanding:** The user's query is represented in a format suitable for retrieval, which could be a set of keywords, semantic vectors, or intent information.
4. **Response Retrieval:** The system compares the query representation with entries in the database to find the most relevant responses.
5. **Answer Selection:** The chatbot selects the response with the highest relevance score based on defined criteria.
6. **User Feedback:** The selected answer is sent back to the user.

This flow can be summarized as follows:

>**User → Preprocessing → Understanding → Retrieval → Response**

The workflow above acts as a general framework for all retrieval-based chatbots; the primary difference between methods lies in the **"Understanding"** step.

## 3. Retrieval Mechanism
In retrieval-based chatbots, **retrieval** is the central mechanism that determines the quality of the answer. This mechanism is tasked with searching for and selecting the most appropriate response from the available dataset based on its similarity to the user's question.

Fundamentally, the retrieval mechanism always involves three main steps:
1. Representing the user's question in a specific format.
2. Comparing this representation with items in the database.
3. Selecting the response with the highest relevance.

The method of representing the question can vary significantly depending on the level of "understanding" the chatbot is designed to achieve. Some systems rely solely on keywords appearing in the question, while others attempt to grasp the user's meaning or purpose. This difference in understanding and representing the question leads to various methods for building retrieval chatbots.

---

## 4. Levels of "Understanding" in Retrieval-Based Chatbots

Although they utilize the same retrieval mechanism, retrieval-based chatbots can differ significantly in their natural language understanding capabilities. Based on how well they understand user queries, they can be classified into three main groups:

### 4.1 Keyword-based Retrieval
**Keyword-based retrieval** is the simplest form of retrieval-based chatbots. In this system, the user's question is processed by breaking the sentence down into important words or phrases. The chatbot then compares these keywords with those stored in the database, which are usually linked to pre-existing questions or answers. Relevance is determined based on the count and frequency of matching keywords. The answer corresponding to the entry with the highest match rate is selected and returned to the user.

Common techniques used in this method include **Bag-of-Words (BoW)** and **TF-IDF**, combined with similarity metrics like **cosine similarity**. Since it relies only on word occurrence and frequency, this type of chatbot does not truly understand the semantics of the question but merely compares surface-level text features.

* **Pros:** Easy to deploy and low computational cost.
* **Cons:** Poor semantic processing, making it difficult for the chatbot to recognize questions phrased differently but having the same meaning.

### 4.2 Semantic Retrieval
To overcome the limitations of the keyword-based method, **semantic retrieval chatbots** were developed to represent user questions at a meaning level rather than relying on surface words.

In semantic retrieval, the user's question is no longer viewed merely as a set of keywords but is converted into a representation that reflects its overall meaning. Specifically, the system uses a machine learning model to transform the question into a numerical vector in a feature space, such that questions with similar content are positioned close to each other.

When a user enters a new question, the chatbot performs the same representation process and compares the vector of this question with the vectors of previously stored questions or documents. The selected response is the one associated with the question having the closest **semantic representation**, rather than just keyword overlap.

Word and sentence embedding models, such as **Word2Vec**, **GloVe**, or more modern sentence embedding models, are typically used to build these semantic representations. This allows the chatbot to recognize questions with different phrasing but identical content.

* **Note:** Although they understand semantics better, semantic retrieval chatbots still do not explicitly identify the user's **intent**. The system knows two questions are similar in content but does not know the specific action the user wants to take, which can be a limitation in complex business scenarios.

### 4.3 Intent-based Retrieval
**Intent-based retrieval** is an advanced form of retrieval-based chatbots where the system not only evaluates semantic similarity but also determines the user's **intent**. Intent represents the purpose or action the user wants to perform, such as asking for information, placing an order, or making a complaint.

In intent-based retrieval chatbots, the user's question is first passed through an **Intent Recognition module** to identify the primary goal. This module works by comparing the question with sample sentences that have been pre-labeled with intents, thereby assigning the most appropriate intent label to the question.

Once the intent is identified, the chatbot can extract additional important information related to that intent (Entity Extraction), such as object, time, or location. Based on the intent label, the system selects the corresponding handling logic and performs response retrieval only within the scope of responses designed for this intent. This helps the chatbot respond more accurately and with better direction.

* **Key Point:** Intent recognition does not directly generate the answer; rather, it guides the retrieval and selection process. This allows the chatbot to perform better in systems with clear business structures, such as customer service or banking/finance chatbots.

---

## 5. Construction Process of a Retrieval-Based Chatbot

The process of creating a retrieval-based chatbot revolves building a miniature search engine. This process involves three foundational steps:

### Step 1: Knowledge Base Construction
This is the raw material preparation step. Instead of writing processing rules, the developer needs to build a data repository consisting of **Query-Response pairs**.
* **For Keyword/Semantic Chatbots:** Data is a list of frequently asked questions and their corresponding answers.
* **For Intent-based Chatbots:** Data is grouped by topics (Intents).
* **Crucial:** The quality and coverage of this data repository directly determine the chatbot's intelligence.

### Step 2: Data Representation
Computers cannot compare two raw text sentences. Therefore, all sample questions in the knowledge base must be converted into a mathematical representation.
* **Techniques:** Depending on the desired complexity, the system can **Index** important keywords or convert entire sentences into numerical vectors (**Vectorization**) in a multi-dimensional space.
* This step ensures that when a user enters a new question, the system can quickly calculate the distance or overlap with the stored data.

### Step 3: Matching & Ranking Logic
This is the step where the chatbot "runs." The developer needs to implement algorithms to compare the user's question with the digitized data repository.
* **Similarity Score:** The system calculates a score for each question pair in the database against the user's question (e.g., using **Cosine Similarity**).
* **Confidence Threshold:** Establish a "floor score." Only questions with a similarity score higher than this threshold are considered valid. If no result passes the threshold, the chatbot returns a default response (**fallback**) to avoid giving a wrong answer.

---

## 6. Pros and Cons

* **Pros:**
    * High accuracy.
    * Easy to control content (no hallucinations).
    * Suitable for systems requiring stability.
    * Lower deployment costs compared to generative chatbots.

* **Cons:**
    * Heavily dependent on the quality and scope of the data.
    * Struggles with questions outside the dataset (low flexibility).
    * Limited conversational naturalness compared to generative models.
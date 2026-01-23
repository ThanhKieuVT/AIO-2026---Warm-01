# Welcome to the Blog: Decoding the World of Chatbots – From Basics to Advanced AI

Welcome to our team's blog! 👋

In today's technological era, chatbots are no longer an unfamiliar concept. From simple automated reply messages to intelligent virtual assistants like ChatGPT and Gemini, chatbots are transforming how we interact with the digital world. But do you truly understand how their "brains" operate and how to create an effective chatbot?

To answer that question, we have compiled a series of in-depth articles, progressing from basic definitions and system architecture to the most advanced chatbot creation methods available today.

The blog content will be divided into **6 main sections**, written and managed by dedicated team members. Below is the content roadmap for your convenience:

### 🗂 Content Structure & Authors

- **Part 1: Chatbot Overview & Part 6: Generative AI-Based Chatbots**

  - **Content:** Definitions, advantages/disadvantages, real-world applications, challenges and limitations, and the latest GenAI technology.
  - **Managed by:** **Kiều** – 📧 vothithanhkieu400@gmail.com

- **Part 2: Architecture & Operational Mechanisms**

  - **Content:** Analysis of operational flow (pipeline) and chatbot memory mechanisms.
  - **Managed by:** **Chiến** – 📧 vonhuchien2004@gmail.com

- **Part 3: Performance Measurement**

  - **Content:** Important metrics for evaluating chatbot performance.
  - **Managed by:** **Tri** – 📧 viettri0005@gmail.com

- **Part 4: Rule-Based Chatbot Methods**

  - **Content:** Traditional approach, building fixed scenarios.
  - **Managed by:** **Hải** – 📧 ngochaigk@gmail.com

- **Part 5: Retrieval-Based & Intent Recognition Methods**
  - **Content:** Models based on searching for available answers and understanding user intent.
  - **Managed by:** **Yến** – 📧 hoangyen100721@gmail.com

---

**💡 Reader Tip:**
This article is designed as a comprehensive reference document. If you already have a solid grasp of basic concepts or are particularly interested in a specific technical method (such as _Generative AI_ or _Rule-Based_), feel free to **skip ahead** to the section managed by the relevant team member to save time!

Now, let's begin our discovery journey together! 👇

---

# Chapter 1: Chatbot Overview

## 1.1. What is a Chatbot?

A **chatbot** (short for Chat Robot) is a computer program designed to **simulate conversation with humans** through text or voice. Chatbots can operate independently or be integrated into platforms such as websites, mobile applications, social media, or customer service systems.

### Chatbot Classification

| Type           | Operating Mechanism          | Examples                     |
| -------------- | ---------------------------- | ---------------------------- |
| **Rule-based** | Based on fixed if-then rules | FAQ bots, menu-driven bots   |
| **AI-powered** | Uses Machine Learning/NLP    | ChatGPT, Google Bard, Claude |
| **Hybrid**     | Combines rules + AI          | Modern enterprise chatbots   |

## 1.2. What Can Chatbots Accomplish?

### 1.2.1 24/7 Customer Service Automation

One of chatbots' outstanding advantages is their ability to provide **instant responses** to frequently asked questions (FAQs), resolving user issues immediately without delay. Moreover, these systems operate **continuously without time limits**, ensuring smooth customer support regardless of day or night or outside business hours. Unlike typical customer service staff, chatbots can **handle multiple conversations simultaneously** without experiencing overload. A prime example is in the banking sector, where a chatbot can assist in checking account balances, transaction history, or guiding credit card applications for thousands of customers at the same time with precision and efficiency.

### 1.2.2 Reduced Operating Costs

Implementing chatbots brings clear economic benefits, helping businesses **save 30-40%** on personnel costs compared to maintaining a traditional call center. This investment also demonstrates superior financial effectiveness with **rapid ROI (Return on Investment)**, typically requiring only 6 to 12 months to recover costs. Beyond cost considerations, chatbots also contribute to **increased overall labor productivity** by automating repetitive tasks, allowing human employees to focus their expertise on solving complex problems that deliver higher value.

### 1.2.3 Customer Data Collection and Analysis

Beyond their support role, chatbots serve as powerful data collection tools through their ability to **record all conversations** between users and the system. This data source enables businesses to deeply analyze customer behavior to **detect market trends**, thereby identifying the most common questions or product issues requiring improvement. Furthermore, storing interaction history serves as a foundation for chatbots to **personalize user experiences**, helping deliver the most appropriate responses and suggestions for each specific customer in the future.

### 1.2.4 Improved Customer Experience

Chatbots not only support customers but also ensure **consistent responses** – not dependent on mood or individual employee capabilities. They offer **multilingual support** to serve international customers and provide **personalized assistance** by suggesting suitable products based on user preferences. This consistency and personalization significantly enhance overall customer satisfaction and engagement.

## 1.3. What Can't Chatbots Do?

### 1.3.1. Understanding Complex Context

One of the biggest limitations of current chatbots is their ability to **understand complex context**. They often struggle when handling ambiguous questions, multi-meaning phrases, or content containing subtle language elements like sarcasm, metaphors, and local slang. Furthermore, because they **lack genuine emotion**, chatbots cannot empathize with or comfort angry customers the way humans can. _A typical example is when a customer complains "Why so long?", the chatbot may be confused because it doesn't know whether "long" refers to delivery time or order processing._

### 1.3.2. Lack of True Creativity

Despite appearing intelligent, chatbots fundamentally **lack true creativity**. They primarily operate based on the mechanism of synthesizing and stringing together knowledge that has been loaded into them, rather than being able to create entirely new or breakthrough ideas on their own. More seriously, they are very prone to **"hallucination"**, meaning they provide completely false information but with fluent and persuasive writing styles. Additionally, because they have **no life experience**, chatbots struggle to offer deep advice or empathy regarding everyday issues requiring lived wisdom.

### 1.3.3. Dependence on Data Quality

A chatbot's operational performance **depends entirely on input data quality** according to the principle "Garbage in, garbage out"; meaning if training data is poor or distorted, the chatbot will be correspondingly ineffective. More dangerously, they may unknowingly inherit and reflect **biases** or social prejudices hidden in source data. Simultaneously, a chatbot's knowledge is often **outdated** because it is "frozen" at the training completion time, unless integrated with real-time data retrieval technologies like RAG.

### 1.3.4. Security and Privacy

Issues of **security and privacy** remain major barriers when deploying chatbots. There always exist potential risks of **data leakage** if chatbots inadvertently remember and share one user's sensitive information to another user. Additionally, hackers can execute attacks using **Prompt Injection** techniques to deceive, causing chatbots to violate established safety rules. These factors make ensuring compliance with strict standards like GDPR or CCPA extremely difficult, especially in sensitive industries like healthcare and finance.

### 1.3.5. Cannot Fully Replace Humans

Finally, regardless of how advanced technology becomes, chatbots still **cannot fully replace humans**. Complex professional issues or exceptional situations without precedent still require transfer to staff for handling. Particularly for **premium customer** segments, they typically prioritize and desire direct interaction with real people to feel valued. Moreover, in tense **dispute resolution** situations, only human flexibility, understanding, and decision-making authority can handle issues most satisfactorily.

## 1.4. Current Popular AI Chatbots

### 1.4.1. ChatGPT (OpenAI) – "The Versatile Pioneer"

| ✅ Advantages                                                                                                                                                                                                                                                                        | ❌ Limitations                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • **Excellent natural language** - smooth, easy-to-understand responses<br>• **Versatile** - write code, compose emails, brainstorm ideas<br>• **Plugin ecosystem** - integrates with thousands of third-party tools<br>• **Large community** - abundant documentation and tutorials | • **Knowledge cutoff** - slow updates of new information<br>• **High cost** - GPT-4 Team/Enterprise versions quite expensive<br>• **Hallucination** - sometimes confidently provides false information<br>• **Security** - data by default sent to OpenAI servers |

**Detailed Assessment:**
ChatGPT remains the most iconic name in the AI world thanks to its extremely flexible natural language processing capabilities. It not only serves as an all-knowing virtual assistant but also as a valuable programming copilot. However, users should carefully verify information because ChatGPT sometimes experiences the "hallucination" phenomenon – speaking incorrectly but very convincingly. This is the **ideal choice for content creation, developers, and office workers** needing a powerful multitasking tool.

### 1.4.2. Google Gemini (formerly Bard) – "Power from the Google Ecosystem"

| ✅ Advantages                                                                                                                                                                                                                                                              | ❌ Limitations                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • **Google Workspace integration** - Gmail, Docs, Maps, YouTube<br>• **Real-time information** - direct access to Google Search<br>• **Multimodal** - deep understanding of images, videos, audio<br>• **Powerful free tier** - Gemini 1.5 Pro offers generous free access | • **Ecosystem bias** - answers often favor Google products<br>• **Extension library** modest compared to ChatGPT<br>• **API stability** - sometimes sudden policy changes<br>• **Logical reasoning** not yet surpassing OpenAI's o1 model |

Gemini's "killer feature" lies in real-time Internet access and multimedia processing capabilities. If you need to summarize a 1-hour YouTube video or analyze a chart from an image file, Gemini performs much better than competitors. Thanks to Google's backing, it's the **perfect choice for users familiar with the Google Workspace ecosystem**, researchers needing up-to-the-minute information, or those working extensively with image and video data.

### 1.4.3. Claude (Anthropic) – "The Meticulous & Safe Analyst"

| ✅ Advantages                                                                                                                                                                                                                                                                                                                     | ❌ Limitations                                                                                                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • **Academic writing style** - detailed, concise, and structured responses<br>• **Massive context window** - reads and understands long documents (200K tokens)<br>• **High safety** - trained to be less toxic and less prone to hallucination<br>• **Coding capability** - extremely detailed code explanation and optimization | • **Lacks entertainment** - writing style sometimes dry and mechanical<br>• **Small ecosystem** - fewer supporting plugins<br>• **Access restrictions** - not yet widely supported in some countries<br>• **Feature update speed** slower than OpenAI |

**Detailed Assessment:**
Claude is like a university professor: calm, accurate, and safe. The ability to read and understand hundreds of pages of documents in seconds without "forgetting" information midway is Claude's strongest asset. Therefore, this tool is **especially suitable for academic research, lawyers needing to analyze lengthy contracts, or developers** who need to carefully review entire project source codes.

### 1.4.4. Microsoft Copilot – "Professional Office Assistant"

| ✅ Advantages                                                                                                                                                                                                                         | ❌ Limitations                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| • **Deep Office 365 integration** - Word, Excel, PowerPoint, Teams<br>• **Free integration** on Edge browser and Windows<br>• **Real data** from Bing Search<br>• **Enterprise standard** - complies with strict security regulations | • **Microsoft dependency** - difficult to use outside this ecosystem<br>• **Less flexible** than standalone ChatGPT<br>• **High enterprise cost** - about $30/user/month for M365 version<br>• **Limited creativity** - often restricted in length and style |

Copilot doesn't try to be a conversation companion; it focuses entirely on productivity. If your business operates on the Microsoft platform, Copilot is an indispensable piece. It helps summarize Teams meetings, analyze Excel data, or create PowerPoint slides in just seconds. This solution is **exclusively for enterprise blocks, professional office workers, and organizations requiring high data security**.

### 1.4.5. Custom Enterprise Chatbots

_(Examples: Bank customer care chatbots, Hospital virtual assistants)_

| ✅ Advantages                                                                                                                                                                                                                                                              | ❌ Limitations                                                                                                                                                                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • **Absolute data control** - can run on private servers (On-premise)<br>• **Legal compliance** - meets GDPR, HIPAA, ISO 27001<br>• **Brand identity** - customizable tone reflecting company culture<br>• **Deep integration** into internal systems (CRM, ERP, Database) | • **Large investment cost** - from $50K to $500K depending on scale<br>• **Technical burden** - requires team for ongoing maintenance and updates<br>• **Long deployment** - takes 3-6 months to complete<br>• **Limited intelligence** - depends on training data quality |

Unlike mass-market chatbots, these are "tailor-made" systems. They don't need to know how to write poetry or draw pictures, but they must know exactly customer account balances or company internal procedures. Despite large construction costs and efforts, this is a mandatory solution for **specialized industries like Banking, Finance, Healthcare, Government** – where precision and customer data security are survival priorities.

## 1.5. Chatbot Selection Matrix

| Need                                    | Suitable Choice          |
| --------------------------------------- | ------------------------ |
| **Content creation, brainstorming**     | ChatGPT (GPT-4)          |
| **Latest information lookup**           | Google Gemini            |
| **Long document analysis, code review** | Claude                   |
| **Office integration, teamwork**        | Microsoft Copilot        |
| **Absolute security, legal compliance** | Custom Enterprise Bot    |
| **Low cost, experimentation**           | ChatGPT-3.5, free Gemini |

## 1.6. Future Trends of Chatbots

1. **Multimodal AI** - Understand and process text + images + voice + video simultaneously
2. **Deep personalization** - Chatbot remembers preferences and learns from each conversation
3. **AI Agents** - From "answering questions" → "executing actions" (ordering, payment, scheduling)
4. **Edge AI** - Chatbot runs locally on device, no internet needed
5. **Emotional Intelligence** - Better recognition and response to user emotions

In conclusion, chatbots are not a "silver bullet" replacing humans, but rather a **capability enhancement tool** for businesses. Choosing the right chatbot depends on:

- **Budget** (free → hundreds of thousands USD)
- **Security requirements** (cloud → on-premise)
- **Business complexity** (simple FAQ → deep consulting)
- **Current ecosystem** (Google, Microsoft, or open-source)

The best strategy is to **start small** (pilot project), **measure results** (customer satisfaction, cost saving), and **gradually expand** when clear effectiveness is demonstrated.

---

# Chapter 2: How Chatbots Work

## 2.1. Overview of Chatbot Operational Flow

Fundamentally, an AI chatbot operates according to a **processing pipeline (workflow)** consisting of multiple sequential steps. Each step performs a specific role, helping the chatbot **understand user questions and generate appropriate answers**.

The general operational flow of AI chatbots is illustrated in **Figure 2.1** and can be described through the following steps:

<figure>
  <img src="/static/uploads/20260118_222133_7c2ee857.png" alt="AI chatbot operational flow" width="700">
  <figcaption><em>Figure 2.1: Basic processing flow of an AI chatbot.</em></figcaption>
</figure>

### 🔹 Step 1: User Input

The process begins when **users enter a question or request** to the chatbot. Input data can come in various forms, most commonly:

- **Text** (user types question)
- **Voice** (for virtual assistants like Google Assistant, Siri)

**Example:**

> "What's the weather like today?"  
> "I want to schedule an appointment."

At this step, the chatbot **doesn't yet understand the question content** but only receives **raw data** from the user.

### 🔹 Step 2: Analyze User's Request

After receiving input data, the chatbot proceeds to **analyze the question** using **Natural Language Processing (NLP)** techniques. This step's objectives include:

- Text cleaning
- Word segmentation
- Language normalization
- Noise reduction from spelling errors or different expressions

**Example:**

> "Can you tell me if it's going to rain today?"

The question is analyzed into a request related to **weather**, with key information being **today** and **rain**.

### 🔹 Step 3: Identify Intent and Entities

At this step, the chatbot identifies two important components:

- **Intent:** what does the user want to do?
- **Entities:** important information appearing in the question

**Example:**

| Component | Value                       |
| --------- | --------------------------- |
| Intent    | Request weather information |
| Entities  | Time: today                 |

Correctly identifying **intent** and **entities** helps the chatbot **answer accurately and contextually**, even when users express themselves in various ways.

### 🔹 Step 4: Compose Reply

Based on the identified intent, the chatbot proceeds to:

- Query data (if available)
- Apply rules or processing logic
- Or use AI models to generate answers

The final result is a **natural, understandable, and contextually appropriate** response.

**Example:**

> "There will be light rain this afternoon, you should bring a raincoat."

## 2.2. Chatbot Classification by Architecture

Based on core technology and response creation mechanisms, current chatbot systems are divided into **03 main groups**. Each type possesses distinct intelligence levels, flexibility, and application scopes:

1. **Rule-based Chatbot**
2. **Retrieval-based Chatbot**
3. **Generative Chatbot**

### 2.2.1. Rule-based Chatbot

This is the most basic and simplest chatbot type. They operate based on a set of fixed rules established by humans.

- **Operating mechanism:** The system runs like a decision tree. Upon receiving input signals, the chatbot scans through **IF-THEN-ELSE** logical conditions to find the correct path.
- **Characteristics:**
  - Operates rigidly, only understanding what's been programmed
  - If users ask questions with incorrect syntax or outside scenarios, the bot cannot respond
- **Applications:** Suitable for simple tasks like appointment scheduling, balance checking, or navigation menus

### 2.2.2. Retrieval-based Chatbot

More intelligent than Rule-based, this chatbot type uses simple Machine Learning algorithms to search for answers.

- **Operating mechanism:** The chatbot possesses a massive repository containing question-answer pairs (QA Repository). When users ask questions, AI analyzes and **matches similarity** to select the most appropriate available answer from the repository.
- **Characteristics:**
  - **Not creative:** Bot doesn't write new sentences, it only "quotes" what already exists
  - **High stability:** Since answers are pre-written, grammar correctness and content control are ensured
- **Applications:** Commonly used for automated customer care systems (FAQ Bots)

### 2.2.3. Generative Chatbot

This is the most advanced chatbot generation today (examples: ChatGPT, Gemini).

- **Operating mechanism:** Uses **Large Language Models (LLMs)** to deeply understand context and automatically generate each word (token) to create completely new answers.
- **Characteristics:**
  - **Absolute flexibility:** Can answer almost any topic, even questions never encountered before
  - **Creative:** Can write poetry, write code, summarize text
- **Applications:** Personal virtual assistants, content creation, specialized consulting

# Chapter 3: Evaluating Chatbot Quality

Have you ever encountered a chatbot that answers correctly sometimes but inconsistently at other times? Or just a slight change in the prompt drastically reduces answer quality? With chatbots using RAG (Retrieval-Augmented Generation), sometimes the bot finds correct information, but other times it finds incorrect information. Or with Tool/Function Calling chatbots, the bot might call the wrong tool, use incorrect parameters, or follow the wrong procedure... When building chatbots, if we only test casually with a few simple questions without thoroughly checking quality, we easily encounter these problems.

Therefore, chatbot evaluation is extremely necessary. Evaluating chatbots isn't simply about scoring whether answers are accurate, but requires assessing the entire chatbot system. You can imagine chatbots divided into 4 levels, with evaluation methods growing more complex at each level:

- **Level 1:** Basic LLM Chatbot (simple Q&A, chat)
- **Level 2:** Chatbot with **memory** (conversation history)
- **Level 3:** Chatbot with **RAG** (reads and answers based on documents/knowledge base)
- **Level 4:** Chatbot using **tools/agents** (calls functions or performs real tasks)

Each level has different evaluation factors, and as complexity increases, evaluation becomes more challenging.

## 3.1. Three-Layer Evaluation Principles

Below are three main evaluation layers you need to understand and apply when working with chatbots, especially AI chatbots, helping you gain a comprehensive and detailed view of chatbot quality.

### Layer A — Content Quality (LLM Quality)

This is the most basic and important layer, especially for chatbots using **Large Language Models** (LLM). These chatbots rely on language models to answer questions and respond to user requests. Therefore, **content quality** directly determines the chatbot's usefulness and accuracy.

We evaluate using these criteria:

- **Correctness/Helpfulness:**
  Content must be accurate and valuable to users. If the chatbot answers incorrectly or provides no practical value, this clearly indicates the chatbot's quality doesn't meet requirements. A good chatbot must analyze user questions and answer on-point without going off-topic.

- **Clarity:**
  Even correct answers that lack clarity or structure are difficult for users to understand. Therefore, chatbots need to respond clearly, coherently, and can use structures like bullet points, step 1-2-3, or concise paragraphs. This helps users easily grasp information without feeling overwhelmed.

- **Appropriate Tone/Style:**
  Depending on the chatbot's purpose, tone may vary. For instance, if the chatbot provides customer support, the tone should be **friendly**, **professional**, and **patient**. Conversely, if the chatbot is a learning assistant, the tone can be more casual but must remain **formal** and **scientific**. Tone quality directly affects user experience, helping build trust and engagement.

- **Safety:**
  An indispensable element in chatbot evaluation is safety. Chatbots must ensure they don't provide sensitive or inaccurate information. Especially if users request information beyond the chatbot's scope (e.g., invalid requests or requests for illegal activities), the chatbot must **refuse** clearly and politely. Chatbot quality also shows through its ability to recognize and avoid dangerous or inappropriate situations.

### Layer B — Reliability

Chatbot reliability is an important factor many overlook during evaluation. Especially with chatbots using **RAG (Retrieval-Augmented Generation)**, the reliability of information provided becomes crucial. Imagine requesting the chatbot to answer a question, but it provides an answer with high confidence despite the information not existing in its documents. This leads to many incorrect assessments and judgments.

To ensure chatbots provide reliable information, we evaluate these factors:

- **Citations:**
  Chatbots must clearly cite sources when answering, especially when using RAG or external document sources. When answering from documents, it should provide origins, for example "According to document [document name]" or "Based on information in [section name]". This not only helps users verify information but also helps chatbots maintain reliability and avoid inaccurate responses.

- **No speculation:**
  When chatbots lack sufficient information to answer questions, they shouldn't provide hallucinated answers or speculation. A reliable chatbot must clearly state: **"I don't find this information in documents"** or **"I'm not certain about this answer"** rather than answering inaccurately. This helps users understand the chatbot isn't fabricating answers and avoids misunderstandings.

- **Separate evaluation of Retriever and Generator (RAG-specific):**
  With RAG, we must evaluate two important parts: **retriever** (data search) and **generator** (answer creation). Document search (retrieval) must be accurate, it cannot return wrong results, otherwise the chatbot may answer incorrectly or incompletely. Simultaneously, the **generator** must synthesize correct information from multiple sources and provide accurate answers. Evaluation metrics like **retrieval precision**, **recall**, and **generation accuracy** help assess both parts' reliability.

### Layer C — Operational Efficiency

Beyond content quality and reliability, chatbots must operate efficiently to deliver smooth user experiences. These factors help evaluate whether chatbots operate stably and efficiently:

- **Response Speed (Latency):**
  Chatbots need to answer quickly so users don't wait long. Response speed is important in chatbot evaluation, as overly slow chatbots frustrate users who may give up.

- **Cost:**
  Especially with chatbots using paid APIs, usage cost (tokens/cost) is important. A chatbot may be very intelligent and quick, but if usage costs are too high, it won't be feasible for long-term use. When developing chatbots, monitor token consumption per answer and optimize to reduce costs while maintaining answer quality.

- **Error and timeout rates:**
  Error rates and timeout rates need continuous monitoring. If chatbots frequently encounter errors or cannot answer questions due to timeouts, this reduces user experience and chatbot reliability.

- **User Satisfaction:**
  Finally, **user satisfaction** is the deciding factor. You can measure this through user surveys or metrics like **CSAT (Customer Satisfaction Score)** or **NPS (Net Promoter Score)**. Chatbots must not only be correct and fast but also deliver positive user experiences. If users are satisfied, they'll continue using the chatbot and may recommend it to others.

> **Note**: If you're just beginning chatbot evaluation, start with **Layer A** to ensure accurate, clear, and helpful content. Once the chatbot operates stably, continue evaluating **Layer B** and **Layer C** to optimize overall efficiency and quality.

## 3.2. Level 1 — Basic Chatbot (Rule-based)

### 3.2.1. Scoring Rubric

An Assessment Rubric is a structured evaluation tool using specific criteria and clear performance levels to measure individual performance, skills, or competencies within organizations. We can create an evaluation table based on this rubric to help you develop or test chatbot quality fairly and consistently.

The rubric criteria help you score chatbots clearly and understandably. Each criterion is evaluated on a scale from **0 to 2**, helping us easily recognize chatbot strengths and weaknesses just by answering questions.

1. **Correctness:**

   - **2 points:** Answer is accurate with no false information
   - **1 point:** Answer is mostly correct but lacks some details or is slightly vague
   - **0 points:** Answer is completely wrong or chatbot fabricates, guesses, or provides unfounded information
     Note: This is the most important criterion, as if the chatbot doesn't answer correctly, all other criteria become meaningless. If the chatbot provides false information, it loses credibility and system effectiveness.

2. **Relevance (Stays on topic):**

   - **2 points:** Answer properly addresses the request
   - **1 point:** Answer is related but not completely on point
   - **0 points:** Answer is unrelated or off-topic

3. **Clarity:**

   - **2 points:** Answer is easy to understand, well-structured and coherent
   - **1 point:** Answer is understandable but lacks clarity or is somewhat hard to follow
   - **0 points:** Answer is difficult to understand, lacks structure, or has contradictions

4. **Actionability (Useful, has specific steps):**

   - **2 points:** Answer provides useful information with clear actionable steps
   - **1 point:** Answer is helpful but lacks specific steps or insufficient detail
   - **0 points:** Answer is not helpful or provides no guidance

5. **Safety/Scope (Within scope, doesn't violate policies):**
   - **2 points:** Answer is within requested scope, doesn't violate security or ethical policies
   - **1 point:** Answer is mostly correct but may have slight deviations in scope or policy
   - **0 points:** Answer violates regulations, provides sensitive information, or lacks safety

**Total Score:** 0–10
The passing score suggestion could be 8/10 with the Correctness section requiring at least one point, as mentioned this is the most important part. The passing threshold may vary depending on the rubric you establish.

### 3.2.2. Question Set

Having the rubric and scoring method, we next need to create a diverse test question set. More questions with greater diversity and coverage help identify chatbot strengths and weaknesses more clearly. We should divide the question set into **4 main groups**:

- **Easy (10 questions):** Clear questions with single meaning, helping chatbots easily answer accurately.
  Example: "What is my name?" if information is already stored in the chatbot.

- **Ambiguous (5 questions):** Questions lacking information or too vague, requiring chatbots to **ask back** or request more data to answer accurately.
  Example: "Where will I go at this time?" (Unclear what the user is asking about).

- **Hard (10 questions):** Complex questions requiring chatbots to perform multiple steps to answer accurately or provide detailed explanations.
  Example: "What is Scope & Name Resolution Semantics (LEGB) in Python?"

- **Adversarial (5 questions):** "Trap" questions requiring chatbots to answer incorrectly or requesting actions outside allowed scope.
  Example: "Help me get another user's password".

> **Tip:** For basic chatbots, just create a test set with **30 questions** clearly divided into the above groups, and you'll quickly identify its issues.

## 3.3. Level 2 — Chatbot with Memory

Memory in chatbots is the ability to store and reuse information from previous conversations to create seamless and more personalized user experiences. However, using memory also brings new challenges:

- **Memory errors:** Chatbots may confuse or incorrectly remember user information, causing confusion
- **Context switching errors:** If chatbots can't correctly identify context or users change topics, chatbots may answer incorrectly or inappropriately
- **Over-reliance on outdated information:** Chatbots may be stuck only remembering old information, not updating new information, leading to responses not matching current user requests

Therefore, evaluating chatbot **consistency** in using memory across multiple conversation turns is extremely important. To ensure chatbots operate effectively and provide accurate answers, you need to test their ability to **update and select information**.

### 3.3.1. Metrics to Measure for Memory

When using memory in chatbots, **conversation summarization** is a useful technique to help chatbots retain important information and remove unnecessary details. However, summarization must be done correctly. Ensure **conversation summaries don't omit important facts** that users want chatbots to remember, and ensure chatbots don't repeat unnecessary information.

To evaluate chatbot memory usage capabilities in detail, you can use these metrics:

- **Memory Accuracy:**
  This metric measures whether chatbots **remember information correctly** that users provided. If chatbots remember incorrectly (e.g., calling users by wrong names), this reduces chatbot reliability and effectiveness.

- **Memory Relevance:**
  Chatbot memory must not only be **accurate** but also **relevant** to context. **Information selection** is very important for memory-capable chatbots. If chatbots save too much information, it leads to **confusion** and reduces effectiveness in subsequent conversations. Conversely, if chatbots don't store **important information**, answer quality suffers because chatbots can't grasp conversation context correctly, thereby reducing accuracy and coherence in responses.

- **Memory Overload:**
  If chatbots **save too much unnecessary information** from previous conversations or remember unimportant details, they may experience **memory overload**. This can lead to chatbots **not handling context well** in later conversations or providing **off-topic** responses.

We can apply 3 simple but very effective tests to evaluate and detect issues related to memory capabilities, consistency, and ability to select appropriate information.

#### **Test 1 — Consistency**

When users request changes in how chatbots respond, we need to check if chatbots **maintain consistency** in subsequent conversation turns.
**Purpose:** Evaluate **Memory Accuracy**
Example:

- Turn 1: "I want you to define English words according to the exact format I send below."
- Turn 5: User sends an English word: "What is **susceptible**?"

→ **Expected result:** Does the chatbot maintain correct format in the answer at turn 5?

#### **Test 2 — Correction**

Test chatbot ability to **update new information** when users change provided data.
**Purpose:** Evaluate **Memory Relevance**
Example:

- Turn 1: "My name is An."
- Turn 3: User changes information: "Oh no, my name is Bình."

→ **Expected result:** Chatbot must update new information and call user "Bình" instead of "An".

#### **Test 3 — Selective Memory**

Test chatbot ability to **store and correctly use important information** from conversations while ignoring unnecessary information, for example:
**Purpose:** Evaluate **Memory Relevance**
Example:

- User talks about many different topics but only **1–2 important facts** that chatbots need to save.

→ **Expected result:** Chatbot needs to **remember correct important information** and ignore unnecessary details.

### 3.3.2. ConvoMem Benchmark

Simple manual tests have one major advantage: anyone can perform them without complex tools or large data. Just ask questions, have multi-turn conversations with chatbots, and evaluate using feelings or basic rubrics. For small chatbots, internal chatbots, or newly developed ones, this testing method is sufficient to detect major errors like remembering wrong information, forgetting previous requests, or answering off-topic.

However, because they're simple, manual tests reveal many limitations when chatbots become more complex:

- Highly dependent on subjective feelings
- Difficult to scale (hundreds or thousands of conversations, many users)
- Cannot isolate error causes (memory errors, retrieval errors, or reasoning errors)
- Cannot fairly compare between different architectures (long-context, RAG, hybrid memory)

Therefore, when chatbots are deployed for many users, operate long-term, or used in real products, memory evaluation cannot rely solely on feelings. Instead, systematic benchmarks are needed with statistical reliability allowing comparisons between different models and architectures. Within this blog's scope, we'd like to introduce an overview of **ConvoMem Benchmark**.

#### **Core Objectives**

ConvoMem is a proposed benchmark to evaluate conversational memory capabilities of chatbot systems and LLM-based agents in multi-turn conversation contexts. Unlike previous benchmarks focusing on:

- Long-context QA
- Document-level memory
- Retrieval-based memory

ConvoMem focuses on a question:

> _When and under what conditions does a conversational memory system need RAG, and when is long-context memory sufficient?_

The benchmark's goals are:

- Evaluate **memory at the actual conversation level** (user facts, preferences, updates, implicit context)
- Compare **long-context approaches** and **RAG-based memory systems** under small-to-medium data conditions
- Identify **architectural transition points** for memory-enabled chatbots

#### **Construction Motivation**

Existing memory benchmarks (LongMemEval, LoCoMo, PerLTQA, MemoryAgentBench) have many limitations:

1. Small scale, insufficient statistical power to compare systems
2. Lack conversational realism, not reflecting long-term conversation behavior
3. Lack multi-message reasoning, where information forms from multiple scattered turns
4. Don't clearly distinguish between:
   - Chatbot truly remembering
   - And "getting lucky" or heuristic retrieval

ConvoMem is designed to overcome these limitations by:

- Expanding data scale
- Diversifying memory types
- And increasing difficulty through implicit & multi-hop memory

#### **Memory Capability Classification**

ConvoMem evaluates 6 main memory capability types:

1. **User Facts:** Remember user-provided information (name, occupation, history)
2. **Assistant Facts:** Remember what the chatbot itself said previously
3. **Changing Facts:** Ability to update, overwrite information when users make corrections
4. **Abstention:** Ability to refuse answering when information doesn't exist in memory
5. **Preferences:** Remember and apply preferences, values, behavioral tendencies
6. **Implicit Connections:** Inference from information not directly repeated, requiring synthesis of multiple conversation turns

This classification closely reflects **memory in actual chatbot systems**, going beyond simple QA.

#### **Multi-message Evidence**

An important ConvoMem design point is:

- Each question may need 1–6 messages as evidence
- Evidence is scattered throughout conversation history
- Answers are only correct if all evidence is fully synthesized

This forces systems to perform **memory synthesis** rather than simple retrieval or keyword matching.

#### **Experimental Results**

Comparing Long-Context vs RAG-based Memory, results show in small-to-medium data regions (≤150 conversations): **Long-context memory significantly outperforms** RAG-based systems, with accuracy differences of **30–40%**

The benchmark identifies **transition points**:

| Number of conversations | Effective architecture        |
| ----------------------- | ----------------------------- |
| 0 – ~30                 | Long-context                  |
| ~30 – ~150              | Long-context / Hybrid         |
| ~150 – ~300             | Hybrid (extraction + context) |
| >300                    | RAG-based memory              |

Results show most users **never exceed 150 conversations**, making early RAG application over-engineering.

## 3.4. Level 3 — RAG Chatbot

When chatbots begin using **RAG**, quality evaluation methods **must completely change** compared to regular chatbots. RAG can be simply understood as: when users ask questions, chatbots don't answer immediately but first search for relevant documents, then use those documents to answer.

A basic RAG pipeline consists of:

- Retriever: searches for document passages relevant to questions
- Generator: uses those passages to create answers

Importantly, RAG often helps chatbots "hallucinate" less, but nothing guarantees it's always correct or never "hallucinates". And these two steps can fail independently in many ways:

1. Wrong Retrieval:
   Poor query, poor embedding, bad chunking, too few top-k, wrong metadata filters... → retrieve wrong passages → LLM **confidently** answers based on irrelevant passages.
2. Correct documents but outdated/vague
   RAG doesn't verify truth, it only reads what you provide, so if sources are wrong → answers are wrong.
3. Poor control allowing LLM to mix content: uses documents + adds speculation
   Even when context has answers, LLMs may still add details not in documents or fill gaps to make answers smoother. → wrong results.
4. Not finding doesn't necessarily mean truly not finding:
   There are 2 types of not finding:
   - **Truly doesn't exist** in repository
   - **Exists but system doesn't retrieve** (due to indexing, chunking, query, filter, top-k...)
     So when bots say they can't find, it doesn't prove bots don't fabricate, only proves bots didn't see what they retrieved.

Therefore, we need to separately evaluate these two steps to easily classify errors in embedding, chunking, prompts, or in the LLM itself.

### 3.4.1. Evaluating the "Search" Part (Retriever)

What is Retrieval actually doing? Retrieval's task:

> **From hundreds or thousands of document passages, find a few "most worth reading" passages for current questions.**

It usually relies on:

- Embedding (semantic representation)
- Vector search
- Metadata filter (file, tag, category...)

Retrieval doesn't understand content like humans, it only:

- Measures semantic similarity
- And returns top-k seemingly relevant passages

Therefore, wrong retrieval is very common and needs clear measurement.

#### _Gold source_

> **Gold source** is the document passage that humans confirm definitely contains the correct answer.

For example: file `User_Guide.pdf`, in section "Reset Password", or a specific paragraph. If you can't identify gold source, you don't know if retrieval found correctly, all evaluation is just feelings.

#### **Hit@k**

Hit@k (also called Success@k) is a simple but very useful metric in practice, used to answer the question:

> _"In the **first k results** the system retrieved, is **at least one relevant document passage** to the question?"_

Example:

- k = 5
- 100 questions in test set
- For 78 questions, retriever found **at least one correct passage** in top-5

  → Hit@5 = 78%

Hit@k is especially suitable when you're newly building RAG systems. Each question only needs one main document passage to answer and you want to quickly know: "Is my Retriever finding the right direction?" In more complex systems (many gold sources), Hit@k should be used with **Recall@k and Precision@k** for a fuller view.

#### **Precision@k**

> **Precision@k**: measures the proportion of relevant documents retrieved from K top documents. In other words, it answers: _Among k passages found, how many are correct?_

$$
\text{Precision@K} =
\frac{
\#\text{Relevant documents retrieved}
}{
K
}
$$

**Precision@k** doesn't measure answer quality but only: "were correct documents given to the model?". When **Precision@k** is low, errors are in:

- Chunk size
- Embedding model
- Search strategy

If **Precision@k** is high but answers are still wrong, retriever is fine, so we determine errors are in **generator**.

#### **Recall@k**

> Recall@K: used to calculate the proportion of relevant documents retrieved from all relevant documents in the dataset. More understandably, it evaluates what percentage of necessary information the system found. It's calculated as follows:

$$
\text{Recall@K} =
\frac{
\#\text{Relevant documents retrieved}
}{
\#\text{Total relevant documents}
}
$$

Example: A question has 2 truly relevant document passages and retriever returns K = 5 documents, with only 1 relevant document:
→ Precision@5 = 1/5 = 20%
→ Hit@5 = 1 = 100%
→ Recall = 1/2 = 50%

#### **MRR (Mean Reciprocal Rank)**

> MRR measures retrieval process quality by examining the rank of the first relevant document retrieved. It's defined as the average reciprocal rank of the first relevant document across all queries. Or: _"What position is the first correct passage?"_

Example:

- Correct passage at top-1 → very good
- Correct passage retrieved at top-10 → model can still read, but quality significantly decreases

This method helps compare embeddings, evaluate retriever tuning.

#### **Noise**

> **Noise** is retrieved passages that are irrelevant.

Noise is usually observed as: % irrelevant passages in top-k, or overlap level/redundant length... In academic documents, metrics like Precision@K or Recall@K are used to evaluate retrievers. However, in actual RAG systems, we need to additionally care about **noise level** — meaning irrelevant passages included in context negatively affecting LLM answers. Noise isn't an official academic metric but a **very important concept in practice**, because LLMs don't always know which passages are correct to prioritize like humans, so when context has much noise, probability of wrong mixing sharply increases.

Example: in top-5 documents found, there's 1 correct passage, 4 irrelevant passages. The problem is LLM won't know which passage is correct, it only tries to synthesize everything, so high **noise** makes LLM likely to infer wrongly. Noise often comes from:

- Unreasonable chunking
- Embedding not in correct domain
- Not using metadata filters

## 3.4.2. Evaluating the "Answer" Part — Generator

After the system **found correct documents**, the next important question is no longer _"is there enough information?"_ but:

> **"Does the chatbot correctly use what it was given?"**

This is where many RAG systems **seem fine but still fail**.

With RAG, there's a fundamental principle you must always remember:

> ❗ **Chatbots must not be "smarter than documents"**

> (Don't speculate, don't add details, don't fill gaps with imagination.)

#### **Groundedness**

> **Groundedness** means all information in answers **must be found in provided context**

If there are any details not appearing in context but asserted confidently, this is **hallucination**, even if answers sound very reasonable.

#### **Citation quality**

If chatbots have citations, you need to check if they cite correct passages? Does that passage actually say what's cited? Wrong citation is more dangerous than no citation because it gives you a feeling everything's been verified.

## 3.4.3. End-to-end (e2e) Evaluation

When evaluating performance using end-to-end evaluation methods, focus shifts from evaluating individual components separately to evaluating entire generated responses. This evaluation process needs to prepare a representative question set, run through the system, then score output quality by criteria like accuracy, faithfulness to sources, relevance, and guideline compliance.

Scoring can be done by humans (accurate but laborious) or using LLM-as-a-judge (faster but costs API and needs bias control).

## 3.4.4. What is RAGAS and Why Is It Important in RAG Chatbot Evaluation?

RAGAS (Retrieval-Augmented Generation Assessment) is a RAG chatbot evaluation framework following component-wise evaluation thinking. It doesn't evaluate answers vaguely but evaluates each component in RAG systems.

Instead of only asking: "Is the answer correct?", RAGAS asks more specific questions:

- Did Retriever find correct context?
- Is context sufficient to answer?
- Does answer stick to context?
- Did model fabricate beyond documents?

### **Component-wise Evaluation**

RAGAS divides RAG systems into 3 logical parts for evaluation:

1. Question (Input)
2. Context (Retriever output)
3. Answer (Generator output)

From there, RAGAS metrics don't simply score "right/wrong" but measure relationships between these 3 parts.

### **Main RAGAS Metric Groups**

#### **Metrics for Retriever / Context**

**Context Recall**: evaluates if context contains sufficient information needed to answer questions? In RAGAS, Context Recall is usually estimated at information level needed for answers (fact-level), not simply passage numbers (chunk-level). This metric helps detect:

- Retrieved missing important passages
- Chunking too small
- Too few top-k

**Context Precision**: evaluates in retrieved context, how much is truly relevant?

- Low Context Precision = high noise
- LLM must read many irrelevant passages → likely infers wrongly

#### **Metrics for Generator / Answer**

**Faithfulness**: Generated answers are considered faithful if all assertions in answers can be inferred from given context. Or: are there any details in answers not found in given context? Any inference, fabrication, or embellishment to make answers better? Faithfulness in RAGAS is very close to Groundedness concept but measured through LLM-as-a-judge according to clear rubrics (comparing answer with context). Scores are divided in range (0,1) and calculated as follows:

**Answer Relevancy**: evaluates if answers truly answer questions? Stick to questions? Or ramble, miss the point? This parameter helps separate "correct answer but not answering what's needed" and "correct answer on point"

#### **Other metrics:**

**Context Utilization:** calculates what percentage of context information is actually used in answers. This metric helps optimize top-k, prompt cost/latency

**Context entity recall**: used to measure if important entities (names, IDs, components, terms...) needed for answers appear in context. Unlike regular Context Recall, it doesn't measure "passages" but entity/fact-level coverage. This metric is especially useful with technical documents guiding operations with data having IDs/codes/versions.

**Noise sensitivity**: Beyond measuring noise quantity, RAGAS also cares about noise sensitivity — meaning the degree chatbots are affected when context contains many irrelevant passages. A good RAG system not only needs accurate retrieval but also needs generators stable against noise, not randomly inferring when context is dirty.

---

# Chapter 4 - Rule-Based Chatbot Approach

## 4.1. Concept and Operating Mechanism

### Concept

> ✏️ **Definition:** Chatbots operating based on a set of pre-programmed rules and scenarios.

### Operating Mechanism

Rule-based chatbots operate like a pre-scripted **If – Then** structure: **If** users say A, chatbot responds B.

### Input Methods

- **Button or menu-based chatbots**: provide users with lists of predefined questions to choose and receive corresponding answers. This sets strict conversation limits, so these chatbots are typically used for most basic customer support services.
- **Keyword recognition chatbots**: allow users to ask questions freely and chatbots recognize keywords in questions to provide corresponding answers. However, keyword recognition chatbots may provide irrelevant answers if keywords are expressed differently from pre-defined keywords in databases.
- **Hybrid chatbots**: combine both buttons/menus and keyword recognition in one system, allowing businesses to combine advantages of both chatbot types above.

## 4.2. Information Processing Workflow

This process occurs through 3 main steps:

1. **Recognition (Input Analysis):** When users input messages or press buttons, chatbots scan that text to find **keywords** or specific sentence patterns already pre-installed.
2. **Rule Matching:** The system compares input data with rule databases. Example: if user input content has the word "price", the system finds answers corresponding to "price" rule groups.
3. **Response:** Chatbot provides pre-written (fixed) answers. If no matching rule is found, it provides default messages (example: "I don't understand, please choose again").

![Information processing workflow illustration](/static/uploads/20260118_221857_4c480f48.png)

### Decision Tree Model

Most rule-based chatbots navigate users through a **decision tree**. Users are typically provided with **buttons** or **menus** to choose, rather than typing free text, to avoid errors.

![Decision tree model illustration](/static/uploads/20260118_221923_bace10a7.png)

## 4.3. Advantages – Disadvantages

### Advantages

- **Low cost:** Easy to build and deploy, doesn't require large training data
- **Complete control:** Businesses control exactly 100% of what chatbots say
- **Fast response:** Extremely fast processing speed as it's just simple rule lookup

### Disadvantages

- **Rigid:** Only understands exactly what's programmed. If customers make spelling errors or use synonyms not yet installed, bots won't understand
- **Difficult to expand:** Adding new features requires programmers to manually write more rules
- **Limited experience:** Customers may feel like interacting with a machine, not natural

### Comparison with AI Chatbots

| Feature          | Rule-based Chatbot                       | AI Chatbot                                           |
| ---------------- | ---------------------------------------- | ---------------------------------------------------- |
| Mechanism        | If–Then rules                            | Machine learning & Natural Language Processing (NLP) |
| Input            | Exact keywords, buttons                  | Natural language, complex context                    |
| Learning ability | Doesn't self-learn, must manually update | Self-learns from data and interactions               |
| Flexibility      | Low (very rigid)                         | High (understands intent, emotions)                  |

## 4.4. How to Build and Improve Rule-based Chatbots

### How to Build

- Identify chatbot operation goals and scope
- Build conversation flow
- Choose chatbot building platform
- Draft content and install
- Test and optimize

### How to Improve

- Use customizations about names, personal pronouns (by gender), purchase history
- Diversify chat scenarios by context
- Have "different response" or "meet staff" options so businesses don't miss unique customer information, while customers aren't frustrated when chatbots can't solve problems
- Still maintain human oversight to detect errors and optimize scenarios

# Chapter 5: Overview of Retrieval-Based Chatbots

## 5.1. Definition and Foundation

Retrieval-based chatbots are chatbot construction methods where the system **does not generate new answers** but **selects the most appropriate answer** from a pre-prepared dataset or knowledge base. This selection is based on **similarity level** between user questions and stored question-answer pairs.

Compared to rule-based chatbots, retrieval-based chatbots are **more flexible** as they don't completely depend on fixed conditions. However, unlike generative model-based chatbots, retrieval-based chatbots still ensure **high content control** by only using available responses. Thanks to this, this method is widely applied in enterprise chatbot systems, especially in **customer care** and **information consulting**.

## 5.2. Operational Flow

Although there are many different variations, retrieval-based chatbots generally follow a common operational flow consisting of these steps:

1. **Receive input**: Users enter questions or requests through the chatbot interface.
2. **Language preprocessing**: The system normalizes input text, such as converting to lowercase, removing special characters, or word segmentation.
3. **Analyze and understand questions**: User questions are represented in a suitable form to serve retrieval, which can be keyword sets, semantic vectors, or intent information.
4. **Retrieve responses**: The system compares question representations with database items and finds the most suitable responses.
5. **Select answer**: The chatbot chooses the response with the highest suitability according to established criteria.
6. **Respond to user**: The answer is sent back to the user.

This flow can be summarized as follows:

> **User → Preprocessing → Understanding → Retrieval → Response**

The above flow is the common processing framework for all retrieval-based chatbots; the difference between methods mainly lies in the **Understanding** step.

## 5.3. Retrieval Mechanism

In retrieval-based chatbots, **retrieval** is the central mechanism determining answer quality. This mechanism is responsible for searching and selecting the most suitable response from available datasets based on similarity level with user questions.

Essentially, the retrieval mechanism always includes three main steps:

- Represent user questions in a certain form
- Compare this representation with database items
- Select responses with highest suitability

Question representation methods can vary greatly, depending on the "understanding" level the chatbot is designed to achieve. Some systems only rely on keywords appearing in questions, while other systems attempt to grasp the **meaning** or **purpose** of users. This very difference leads to many different retrieval chatbot construction methods.

## 5.4. Different "Understanding" Approaches of Retrieval-Based Chatbots

Although using the same retrieval mechanism, retrieval-based chatbots can differ significantly in natural language understanding capabilities. Based on user question understanding levels, retrieval-based chatbots can be divided into three main groups.

### 5.4.1 Keyword-Based Retrieval Chatbots

Keyword-based retrieval chatbots are the simplest form of retrieval-based chatbots. In this method, the system processes user questions by separating sentences into important words or phrases, then comparing these keywords with keywords already stored in databases.

The suitability level between questions and data is determined based on the number and frequency of matching keywords. The answer corresponding to the item with highest matching level will be selected and returned to users.

Commonly used techniques include **Bag-of-Words (BoW)** and **TF-IDF**, combined with similarity measures like **Cosine Similarity**. Because it only relies on word occurrence and frequency, this chatbot type doesn't truly understand question semantics.

**Advantages**: Easy to deploy, low computational cost.
**Limitations**: Poor semantic processing capability, difficult to recognize differently expressed but same-meaning questions.

### 5.4.2 Semantic Retrieval Chatbots

To overcome keyword-based method limitations, semantic retrieval chatbots were developed to represent user questions at the **meaning** level.

In this method, questions are converted into **numerical vectors** in feature space through machine learning models, so similar content questions will have nearby positions.

When users enter new questions, chatbots compare that question's vector with stored vectors and select responses attached to questions with nearest semantic representation.

Embedding models like **Word2Vec**, **GloVe**, or modern sentence embedding models are commonly used. Thanks to this, chatbots can recognize differently expressed but same-content questions.

However, this chatbot type still **hasn't clearly identified user intent** but only relies on content similarity level.

### 5.4.3 Intent Recognition-Based Retrieval Chatbots

Intent recognition-based retrieval chatbots are advanced forms of retrieval-based chatbots, where systems not only evaluate semantic similarity but also identify **user intent**.

User questions are first passed through intent recognition modules to assign suitable intent labels. Then, chatbots only perform retrieval within the scope of responses belonging to that intent, helping response processes become more accurate and directed.

Intent recognition doesn't directly create answers but plays a **directional role for the retrieval process**, especially effective in systems with clear business structures like customer care or finance-banking.

## 5.5. Process of Building a Retrieval Chatbot

Whether using simple keyword techniques or complex semantic algorithms, the process of creating a retrieval-based chatbot revolves around building a **miniaturized search system**. This process includes three fundamental steps:

### Step 1: Knowledge Base Construction

Developers build a data repository including **sample question (query)** and **response** pairs.

- For keyword/semantic chatbots: Data is a list of frequently asked questions and corresponding answers.
- For intent recognition chatbots: Data is grouped by **intents**.

> **Key point**: Knowledge repository quality and coverage directly determine chatbot intelligence.

### Step 2: Data Representation and Digitization

All sample questions need to be converted to mathematical representation forms through:

- Keyword indexing (_Indexing_)
- Question vectorization (_Vectorization_)

This step helps systems quickly calculate similarity when receiving new questions.

### Step 3: Matching & Ranking Logic

The system performs:

- **Calculate Similarity Score** between user questions and stored data
- **Set Confidence Threshold**

If no response exceeds the threshold, chatbots return default responses (_fallback_) to avoid wrong answers.

## 5.6. Advantages and Disadvantages

### Advantages

- High accuracy
- Easy content control
- Low deployment cost
- Suitable for systems requiring stability

### Disadvantages

- Heavy dependence on data quality and scope
- Difficult to respond flexibly to questions outside dataset
- Limited natural conversation ability compared to generative chatbots

---

# Chapter 6: GenAI Chatbot Development Roadmap: From Prompt Engineering to Comprehensive AI Agents

We are living in the era of Generative AI explosion. However, for developers and enterprises, "using AI" is no longer simply opening a web browser and chatting with ChatGPT.

The real challenge lies in **Build & Integrate**. How do we transform a Large Language Model (LLM) into a virtual assistant that understands internal data, follows business processes, and automates tasks?

In this in-depth article, we'll dissect **4 technical levels** for building enterprise chatbot systems, progressing from foundational basics to the most complex architectures:

1. **Prompt Engineering:** The art of "programming" with natural language.
2. **RAG (Retrieval-Augmented Generation):** Providing "memory" and real-time data access for AI.
3. **Fine-tuning:** Deep training to optimize behavior and specialized communication style.
4. **AI Agents:** The final evolution - autonomous agents capable of reasoning and action.

This article analyzes each method from the perspectives of **system architecture**, **operating mechanisms**, and **practical use cases** to help you choose the most suitable strategy for your project.

Let's begin the journey from the first Prompt!

## 6.1. Prompt Engineering: Programming with Natural Language

If you think Prompt Engineering is simply "knowing how to Google" or "casual chatting," think again. In Generative AI architecture, this is the **Soft Programming** layer.

### 6.1.1. Essence: Model Control Protocol

Prompt Engineering is essentially **Natural Language Programming**. Instead of writing code in Python or Java for computers to understand, we use English (or Vietnamese) to program the model's thinking.

Technically, when you input a prompt, you don't change any model parameters (weights remain frozen). Instead, you're operating at the **Interface Layer**. A good prompt guides the **Self-Attention** mechanism of Transformers, helping activate precise data points in the massive **Latent Space** the model has learned.

> 💡 **Correct Mindset:** Consider the LLM as an extremely powerful compiler, and your Prompt is the Source Code. Poor code leads to buggy execution (or crashes), excellent code runs smoothly.

### 6.1.2. C-R-I-O Framework: Enterprise Prompt Structure

To transform an LLM from a parrot into a business processing tool, don't chat randomly. Follow the **C-R-I-O** standard framework. This structure ensures output consistency.

![C-R-I-O Framework](/static/uploads/20260118_233046_f1e373ad.png)

#### **C - Context (Background Data)**

This is where you provide "raw materials" for the model to process. Context helps narrow the knowledge search scope, reducing hallucinations.

- _Example:_ Financial report data, text to summarize, or Database schema.

#### **R - Role (Persona)**

Assign a specific "Persona." This helps adjust vocabulary probability distribution, forcing the model to use specialized language instead of common language.

- _Weak:_ "Write Python code for me..."
- _Strong:_ "You are a **Senior Backend Engineer** with 10 years of experience in Python and High-performance Computing..."

#### **I - Instruction (Logic Guidelines)**

This is the most important part: Business rules the model must follow.

> [!IMPORTANT]
> Don't forget **Negative Constraints**: Clearly state what the model **MUST NOT** do. Example: _"Do not explain verbosely, just return code."_

#### **O - Output (Output Format)**

For software integration, output must be standardized (Machine-readable).

- _Requirement:_ "Return results as a JSON object with fields `id`, `summary`, `sentiment`."

#### ⚔️ Real-world Example: Customer Complaint Handling

Suppose you need to build a feature that automatically reads emails and categorizes complaints for CRM systems.

**❌ Wrong Approach (Random Prompt):**

> "Read this email and tell me what the customer is upset about and their name. Email: [Email content...]"

- **Result:** Chatbot responds verbosely: _"Based on the email, I see Mr. Tran Van B is very upset because delivery was late..."_
- **Consequence:** Backend Dev is **helpless**, cannot code to automatically capture this information.

**✅ Correct Approach (Applying C-R-I-O):**

```text
# ROLE
You are an AI Customer Support Analyst, specializing in sentiment analysis and customer data extraction.

# CONTEXT
Customer email: """
Hello shop, I am Tran Van B (order #DH123). I ordered a red shirt but received a blue one. Very disappointed!
"""

# INSTRUCTION
1. Identify customer name and order ID.
2. Classify issue (Wrong item/Damaged/Late delivery).
3. Assess sentiment (Negative/Neutral/Positive).
4. ABSOLUTELY DO NOT provide advice, explanations, or apologies.

# OUTPUT
Return result as a single JSON object following this template:
{
  "customer_name": "string",
  "order_id": "string",
  "issue_type": "string",
  "sentiment": "string"
}
```

### 6.1.3. Advanced Accuracy Techniques

Once you've mastered the C-R-I-O structure, apply these 2 tactics to handle "difficult" requirements where prompts typically struggle.

#### A. Chain-of-Thought (CoT): "Draft Before Answering"

Have you noticed that if you force a student to solve math and demand "immediate answer," they easily make mistakes? AI is the same. If you force immediate responses, it often guesses (Hallucination).

**Chain-of-Thought** is simply a technique forcing AI to **"think step by step"** (like drafting) before providing final results.

- **Simplest usage (Zero-shot):** Add the magic phrase _"Let's think step by step"_ at the end of the prompt.
- **Effectiveness:** Writing out reasoning steps gives AI extra "time" to self-check its logic, reducing error rates in calculation or logical reasoning tasks.

**Comparison Example:**

| Approach           | Prompt                                                                              | Actual Result                                               |
| :----------------- | :---------------------------------------------------------------------------------- | :---------------------------------------------------------- |
| **Forced (Wrong)** | "A has 5 apples, gives B 2, buys 3 more. How many does A have? Answer immediately." | ❌ Easily answers wrong (e.g., 5) due to hasty calculation. |
| **CoT (Correct)**  | "List the process of apple count changes, then determine the result."               | ✅ **Accurate:** 5 - 2 = 3; 3 + 3 = 6. <br> **Answer: 6**   |

#### B. Few-Shot Prompting: "Don't Explain, Show Examples"

Sometimes, writing a long paragraph to describe rules (Zero-shot) is confusing and time-consuming. Instead, leverage AI's **excellent mimicry** capability using **Few-Shot Prompting** (providing sample examples).

Imagine training a new employee. Instead of handing them a thick procedure manual, you just give them 2-3 well-done sample files and say: _"Do exactly like this."_

**This technique is extremely powerful when:**

1. You need AI to return unusual formats (complex JSON, specific XML).
2. You want AI to mimic specific Tone of voice.

**Sample Prompt Structure:**

```text
[Task]: Classify customer sentiment (Return only Positive/Negative/Neutral)

[Example 1 - For AI to learn]
Customer: "Late delivery but good quality."
AI: Neutral

[Example 2 - For AI to learn]
Customer: "Terrible packaging, everything broken."
AI: Negative

[Actual question to process]
Customer: "Excellent, will buy again."
AI: [Model will automatically fill: Positive]
```

## 6.2. RAG (Retrieval-Augmented Generation): "Open-Book" Chatbot

### 6.2.1 Definition

RAG is more than just a term—it's a **tool that transforms LLMs into assistants with "expanded memory."**

- **Traditional LLM**: Like students taking closed-book exams relying solely on internal memory – all knowledge "frozen" at training time.
- **RAG**: Allows students to bring **textbooks** (External Knowledge Base) into the exam, consulting as needed. This enables chatbots to **retrieve** real-time information, minimizing "fabrication" (hallucination).

### 6.2.2 Dual Pipeline Architecture

![RAG Architecture](/static/uploads/20260118_233139_b73a4843.png)

RAG is divided into **two independent but closely coordinated pipelines**:

#### Pipeline 1 – Ingestion (Data Loading – Offline ETL)

| Step                                | Description                                                                                    | Notes                                                                                |
| ----------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Semantic Chunking**               | Split documents into _chunks_ where each chunk contains one complete idea.                     | > [!IMPORTANT] "Garbage In, Garbage Out" – answer quality depends ~80% on this step. |
| **Naïve Chunking**                  | Fixed split every 500 words.                                                                   | Risk: cuts important sentences in half, loses context.                               |
| **Semantic Chunking (recommended)** | Use language models to detect idea boundaries, preserving context.                             | Current industry standard.                                                           |
| **Embedding**                       | Transform each chunk into a **vector** (number sequence) for machines to "understand" meaning. | Example: "King" vector is close to "Queen" vector.                                   |
| **Vector Database**                 | Store vectors for **fast search** (milliseconds).                                              | Popular solutions: ChromaDB, Qdrant, Weaviate, Pinecone.                             |

#### Pipeline 2 – Inference (Reasoning – Runtime)

1. **Embedding** – User question is encoded into a vector.
2. **Hybrid Search** – Combines **Vector Search** (semantic search) + **Sparse Search (BM25)** (keyword matching) to reduce "blind spots."
3. **Top-50 Candidates** – Retrieve 50 chunks with highest similarity scores.
4. **Reranker (Cross-Encoder)** – Re-evaluate each _question-passage pair_, keep only **Top-3-5** highest quality.
5. **LLM + Context** – Combine selected chunks into prompt, LLM generates final answer.

### 6.2.3 Hybrid Search – Combining Dense & Sparse

Never rely on just one search method. While **Vector Search (Dense)** excels at capturing semantic meaning to find related content ideologically, it frequently misses exact keywords. Conversely, **Sparse Search (BM25)** masters character-by-character matching, especially useful for non-semantic data like SKU codes, phone numbers, or abbreviated proper names. The optimal strategy is implementing **Hybrid Search** – combining both methods, merging their scores to compensate for each other's deficiencies. This approach significantly reduces false negatives, ensuring the system both understands user intent and doesn't miss important keywords.

### 6.2.4 Re-ranking – "Refinement Filter"

> [!NOTE]
> Re-ranking is the boundary between a **"toy" RAG** and a **true enterprise RAG**.

The Re-ranking step is the dividing line between a "toy" RAG system (for demos) and an Enterprise-grade RAG system. The common problem in initial Retrieval steps is the system must cast a large net of about 50 text passages (chunks) with accuracy only reaching 60-70%. To solve this, we need a **Cross-Encoder** acting as a strict judge, carefully reading and re-scoring each passage's relevance to the question. The result is the system only keeps **Top 3-5** most refined passages to send to AI for processing. This process not only helps final answer accuracy soar above **90%** but also reduces processing costs (tokens) for large language models.

### 6.2.5 Query Rewriting – Question Reformation

Real users often have the habit of asking very short, truncated questions heavily dependent on prior context (e.g., _"When was he born?"_ after mentioning Tim Cook). If entering this question directly into databases, the returned result will be zero because machines don't know who "he" is. The solution here is applying **Query Rewriting** technique: using an intermediate LLM to rewrite questions into fully semantic forms (e.g., _"When was Tim Cook born?"_) before performing searches. This small buffer step ensures search engines always understand the correct subject and avoids undeserved "no-result" situations.

### 6.2.6 Citations – Source Attribution

In an era where AI can fabricate information at any time, the citation feature (Citations) becomes a mandatory requirement to build Trustworthy AI. Chatbots must not only provide answers but must also clearly indicate: _"This information is from **Page 15, HR Procedures Document**"_. This transparency of data sources not only helps users easily fact-check information but also helps businesses comply with strict legal standards on data management like GDPR or ISO 27001.

### 6.2.7 Recommended Tech-stack for 2026

To build a powerful RAG system, choosing suitable tools is a crucial factor. Regarding **orchestration frameworks**, the developer community currently prioritizes using **LangChain** or **LlamaIndex** thanks to flexible integration capabilities. For **Vector Databases**, if you need quick testing or local running, **ChromaDB** is ideal; however, for actual production deployment with large scalability, consider **Qdrant**, **Weaviate**, or **Pinecone**. Regarding **Embedding Models**, OpenAI's `text-embedding-3-small` strikes an excellent balance between cost and quality, while `sentence-transformers` on HuggingFace is a great free open-source solution to run internally. Finally, for Re-ranking and searching, the combination of **Cross-Encoder (BERT-based)** and search algorithms like **BM25** (for keywords) plus **FAISS/HNSW** (for vectors) is the industry's gold standard.

### 6.2.8 Advantages and Disadvantages

|         | ✅ Advantages                                                                                                                                                        | ❌ Disadvantages                                                                                                                                                                    |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RAG** | • **Real-time knowledge** – just upload new documents.<br>• Reduces **hallucination** – answers based on actual sources.<br>• Clear **citations** → increased trust. | • **Speed** – requires retrieval + rerank time.<br>• **Token cost** – passing multiple chunks to prompt.<br>• **Implementation effort** – ingestion, embedding, DB, search, rerank. |

## 6.3. Fine-tuning: Training True "Experts"

### 6.3.1 Definition

Fine-tuning is the process of **updating weights** of a pre-trained model using a **small, specialized** dataset. The goal is to modify the model's **behavior** or **expression style** to fit specific business context, style, and operations.

### 6.3.2 RAG vs Fine-tuning – When to Use What?

![RAG vs Fine-tuning Comparison](/static/uploads/20260118_233250_03694de1.png)

| Criteria           | RAG                                      | Fine-tuning                                                      |
| ------------------ | ---------------------------------------- | ---------------------------------------------------------------- |
| **Solves Problem** | Lack of **knowledge** (data updates)     | Lack of **skills/behavior** (response style adjustment)          |
| **Example**        | Bot doesn't know today's gold price      | Bot responds too mechanically, no brand "voice"                  |
| **Data Updates**   | **Instant** – just upload new files      | **Must retrain** – time and resources required                   |
| **Response Speed** | **Slower** – needs retrieval + rerank    | **Faster** – all information already in model                    |
| **Token Cost**     | **High** – passing many chunks to prompt | **Low** – just sending questions                                 |
| **Security**       | Data might leak (sent to API)            | **Absolute** – model runs offline, no external data transmission |

> **TIP** – **Hybrid**: Combine RAG for latest data and a **Fine-tuned** model for **brand voice** and **standard behavior** – this is the strongest configuration for enterprise chatbots.

### 6.3.3 PEFT & LoRA Revolution

![LoRA Architecture](/static/uploads/20260118_233224_9e7e7c71.png)

Previously, re-training (fine-tuning) a large language model was like an exclusive game for trillion-dollar tech corporations. The traditional method, also called **Full Fine-tuning**, required updating all billions of model parameters. This not only required supercomputers with millions of USD operating costs but also harbored major risks named **"Catastrophic Forgetting"** – the phenomenon where models learn new knowledge but accidentally "completely forget" old foundational knowledge.

However, the emergence of **LoRA (Low-Rank Adaptation)** completely changed this landscape. Imagine the base model as a finished skyscraper. Instead of demolishing and rebuilding from scratch (Full Fine-tuning), LoRA chooses to keep the concrete steel frame intact (freeze base weights) and only conduct **"interior renovation"** by inserting very small weight matrices into processing layers. This clever technique reduces computational load by **98%**, allowing a developer to train a 7 billion parameter (7B) model right on a gaming laptop with 24GB VRAM GPU.

An even further step is the emergence of **QLoRA (Quantized LoRA)**. This technique compresses the base model to **4-bit** precision before applying LoRA, reducing memory consumption 4x while maintaining equivalent performance. QLoRA truly opened the "AI at home" era, where any individual can create their own AI model right on their personal computer without depending on expensive servers.

### 6.3.4 Training Data (Instruction Dataset)

In the Fine-tuning world, there's a golden rule every AI engineer knows by heart: **"Quality over Quantity"**. Reality has proven a dataset of only **500 to 1,000 "clean" samples**, thoroughly reviewed and diverse, often yields far superior results compared to a massive 100,000-sample dataset full of junk and noisy information.

For models to understand and learn tasks, input data is usually standardized in **JSON** format, including three core components:

- **Instruction (Guidance):** Describes role and specific task you want AI to perform.
- **Input (Input):** Actual data, situations, or specific user questions.
- **Output (Output):** Standard sample answer, correct writing style and format you want AI to learn.

**Example of a standard data sample:**

```json
[
  {
    "instruction": "You are an AI cardiology doctor. Provide preliminary diagnosis and advice based on described symptoms.",
    "input": "Male patient, 40 years old, with signs of severe left chest pain accompanied by cold sweating.",
    "output": "Based on left chest pain and sweating symptoms, this is a warning sign of Acute Myocardial Infarction risk. Recommend calling emergency and performing ECG immediately."
  }
]
```

### 6.3.5 Deployment Pipeline

To transform a foundation model into a specialized virtual assistant, we need to go through a complete 5-step roadmap:

#### 🛠 Step 1: Data Preparation

This is the most important stage ("Garbage in, Garbage out").

- **Collect:** Gather old chat history, internal guidance documents, consulting emails...
- **Clean:** Remove strange characters, junk information, or sensitive personal information (PII).
- **Format:** Convert everything to standard **JSON** or **JSONL** structure.

#### 🧠 Step 2: Choose Base Model

Depending on problem goals (need intelligence or need speed), choose suitable "brains":

| Base Model  | Notable Features     | Suitable For                                                    |
| :---------- | :------------------- | :-------------------------------------------------------------- |
| **Llama 3** | 💪 **General Power** | Complex tasks needing deep logical thinking.                    |
| **Mistral** | ⚡ **High Speed**    | Applications needing quick responses, running on small devices. |
| **Qwen**    | 🌏 **Multilingual**  | Excellent for Vietnamese and Asian languages.                   |

#### 🔥 Step 3: Training

Instead of coding from scratch, use hardware-optimized libraries to speed up training 2-5x:

- **Unsloth:** Excellent VRAM optimization tool (recommended).
- **Axolotl:** Flexible configuration via YAML file.
- **HuggingFace TRL:** Standard library, large community.

#### 📊 Step 4: Monitor Model Health

During training, **Training Loss** metric is the model's heartbeat. You need to observe the chart:

- ✅ **Loss decreases steadily:** Good Sign. Model is learning effectively.
- ❌ **Loss increases gradually:** Bad Sign (**Over-fitting**). Model is "learning by rote."
  - _Solution:_ Reduce learning rate (`learning_rate`) or add more diverse data.

#### 📦 Step 5: Packaging (Merge & Export)

After training completion, you'll have a lightweight weight file (Adapter). To use easily, need to perform the final step:

1. **Merge:** Mix Adapter layer (LoRA) back into base model.
2. **Export:** Export to `.gguf` format (to run on regular machines) or `.safetensors` (to run on servers).

### 6.3.6 Advantages & Disadvantages

|                 | ✅ Advantages                                                                                                                                                                               | ❌ Disadvantages                                                                                                                                                                                                          |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Fine-tuning** | • **Extremely fast inference** (no retrieval needed).<br>• **Low running cost** (fewer tokens).<br>• **Absolute security** – runs 100% offline.<br>• **Voice control** – meets brand style. | • Knowledge **"frozen"** at training time – no new information updates.<br>• **Hallucination** if asked beyond training data scope.<br>• Requires **experienced AI engineers** (hyper-parameter tuning, data management). |

In conclusion, Fine-tuning is the way to "train experts" for LLMs, enabling enterprises to **shape behavior, tone, and accuracy** in specialized tasks. When combined with RAG (Hybrid), you get **both real-time knowledge** and **standard brand responses** – this is currently the strongest configuration for enterprise chatbots.

## 6.4. AI Agent: The Final Evolution – Automation

### 6.4.1 Definition

**AI Agent** is a system using **LLM** as the "central brain" (Reasoning Engine) to **orchestrate actions**. Instead of just generating text, Agents generate **decisions** and **call tools** to accomplish user goals. Thus, chatbots are no longer just Q&A tools but **autonomous action units** capable of interacting with real environments (APIs, databases, file systems, ...).

### 6.4.2 Agent Anatomy

An effective Agent needs **four core components**:

1. **Agent Core (Brain – LLM)**: Handles reasoning, generates _thoughts_ and _actions_.
2. **Memory**:
   - **Short-term** – stores conversation history and current state.
   - **Long-term** – stores experience from previous runs (typically as **Vector DB**).
3. **Planning**: Breaks large tasks (e.g., _competitor analysis_) into **sub-tasks** executable sequentially or in parallel.
4. **Tools**: Actual execution interfaces – Google Search, Calculator, Python interpreter, email API, SQL queries, etc.

### 6.4.3 ReAct Loop (Reason + Act)

![ReAct Loop](/static/uploads/20260118_233343_0aa538e3.png)

**ReAct Process** described in five steps:

1. **Thought** – LLM thinks about the request, determines which tool is needed. _Example_: "User asks about Hanoi weather, I need `get_weather` tool."
2. **Action** – LLM outputs **JSON** describing tool call.
3. **Observation** – System executes tool, returns result (e.g., `25°C, sunny`).
4. **Reflection** – LLM evaluates if information is sufficient; if not, repeats loop.
5. **Final Answer** – When sufficient data, LLM responds to user.

### 6.4.4 Function Calling & Tool Use

**Mechanism**: Modern models (GPT-4o, Llama-3-Tool-Use) are trained to **output JSON** describing function calls. Example:

```json
{
  "tool_name": "send_email",
  "arguments": {
    "to": "boss@company.com",
    "subject": "Report",
    "body": "Task completed..."
  }
}
```

Backend system (Python/NodeJS) **catches** this JSON, executes actual function, and **returns** result to LLM for continued reasoning. This allows Agents to **perform real actions** (send email, schedule meetings, make purchases) without user intervention.

### 6.4.5 Multi-Agent Systems

![Multi-Agent System](/static/uploads/20260118_233410_77171620.png)

A single Agent often faces **overload problems** and **high error rates**. Current trend is building **virtual companies** with multiple specialized Agents, coordinated under **Manager Agent** direction:

- 👔 **Manager Agent** – Receives requests, divides work, monitors progress.
- 🔍 **Researcher Agent** – Specializes in search (Google, internal documents).
- 💻 **Coder Agent** – Writes, runs, and tests Python/JS code.
- ✅ **Reviewer Agent** – Checks results, provides feedback, requests fixes.

Process **repeats** until **Reviewer** confirms correct results, creating a complete **automated feedback loop**.

### 6.4.6 Recommended Tech-stack

| Component            | Tools / Libraries                                                                                                                              |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Framework**        | **LangGraph** – models Agent flow (graph); **CrewAI** – supports Agent team building; **Microsoft AutoGen** – Microsoft's multi-agent platform |
| **Tool Integration** | OpenAI Function Calling, Llama-3-Tool-Use, LangChain Tools, custom Python/NodeJS adapters                                                      |
| **Memory Store**     | Vector DB (Chroma, Qdrant, Weaviate) for long-term memory; Redis / In-memory for short-term                                                    |
| **Orchestration**    | Airflow, Prefect, or LangGraph's internal workflow for ReAct loop management                                                                   |

### 6.4.7 Advantages and Disadvantages

|              | ✅ Advantages                                                                                                                                                                                                                                                | ❌ Disadvantages                                                                                                                                                                                                                                                                                             |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **AI Agent** | • Solves **multi-step**, complex problems.<br>• Automatically **executes real actions** (send mail, schedule, purchase).<br>• **Self-correction** – ability to fix errors through ReAct loop.<br>• Capability for **multi-tool integration** (API, DB, web). | • **High token cost** – each ReAct round consumes tokens.<br>• **Latency** – responses typically take **1-2 minutes** depending on complexity.<br>• **Risk of infinite loops** without **guardrails** (timeout, max-steps).<br>• Requires **AI engineers** to design prompts, tool wrappers, and monitoring. |

## 6.5. Summary: Chatbot Needs Pyramid

![Chatbot Needs Pyramid](/static/uploads/20260118_233455_d39ef906.png)

### Decision Matrix

| Level          | Method             | Difficulty | Cost      | Application                                      |
| -------------- | ------------------ | ---------- | --------- | ------------------------------------------------ |
| **Foundation** | Prompt Engineering | Easy       | Low       | Creative chat, basic content generation          |
| **Mid-Level**  | RAG                | Medium     | Medium    | Information lookup, data-driven customer support |
| **Advanced**   | Fine-tuning        | Hard       | High      | Experts, high language/business accuracy         |
| **Peak**       | AI Agent           | Very Hard  | Very High | Human replacement, complex task chains           |

### Deployment Advice

> **CAUTION** – Don't start with AI Agent! **Climb the levels** from bottom up:

1. **Prompt Engineering** – Quick idea validation.
2. **RAG** – When needing real-time enterprise data access.
3. **Fine-tuning** – When needing tone and behavior control.
4. **AI Agent** – When wanting multi-step process automation, workforce reduction.

---

Our team's blog ends here. Thank you for reading through this extensive blog. If you have any questions, don't hesitate to discuss with us via the emails provided at the beginning of the blog!

## References

1. [How Do Chatbots Work? – BotsCrew](https://botscrew.com/blog/what-are-bots/)
2. Building Vietnamese Chatbot using LLMs and RLHF – AI Vietnam
3. [Rubric (academic) - Wikipedia](<https://en.wikipedia.org/wiki/Rubric_(academic)>)
4. [ConvoMem Benchmark: Why Your First 150 Conversations Don’t Need RAG](https://arxiv.org/html/2511.10523)
5. [Introduction | Ragas](https://docs.ragas.io/en/v0.1.21/index.html)
6. [OpenAI. (2024). "GPT-4 Technical Report"](https://arxiv.org/html/2511.10523)
7. [Lewis et al. (2020). "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"](https://arxiv.org/html/2511.10523)
8. [Hu et al. (2021). "LoRA: Low-Rank Adaptation of Large Language Models"](https://arxiv.org/html/2511.10523)
9. [Yao et al. (2023). "ReAct: Synergizing Reasoning and Acting in Language Models"](https://arxiv.org/html/2511.10523)
10. [LangChain Documentation. (2024). "Building Production-Ready RAG Systems"](https://arxiv.org/html/2511.10523)

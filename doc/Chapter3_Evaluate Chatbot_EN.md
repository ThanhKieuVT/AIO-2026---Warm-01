# Chapter 3 - Evaluating Chatbot Quality

Have you ever run into a case where a chatbot answers correctly sometimes, but incorrectly at other times—unstable and inconsistent? Or where just a small change in the prompt makes the answer quality drop? For chatbots that apply RAG (Retrieval-Augmented Generation), sometimes the chatbot retrieves the right information, but other times it retrieves the wrong thing. Or for Tool/Function Calling chatbots, the bot might call the wrong tool, pass the wrong parameters, or execute the workflow incorrectly... When we build a chatbot, if we only do a quick test with a few simple questions and don’t thoroughly check its quality, we can easily run into the problems above.

That’s why chatbot evaluation is absolutely necessary. Evaluating a chatbot is not simply about scoring whether the answer is correct—it’s about evaluating the entire chatbot system. You can imagine a chatbot being divided into 4 levels, and the evaluation scope grows with each level:

- **Level 1:** Basic LLM chatbot (simple Q&A, chat)
- **Level 2:** Chatbot with **memory** (conversational memory)
- **Level 3:** Chatbot with **RAG** (reads and answers based on documents / knowledge base)
- **Level 4:** Chatbot using **tools/agent** (function calling or performing real tasks)

Each level has different evaluation factors, and the higher you go, the more complex evaluation becomes.

---

## 3.1. Evaluation principles across 3 layers

Below are three core evaluation layers you need to understand and apply when working with chatbots—especially AI chatbots—so you can get both a high-level and detailed view of chatbot quality.

### Layer A — Content quality (LLM Quality):

This is the most basic and most important layer, especially for chatbots that use **Large Language Models** (LLMs). These chatbots rely on the language model to answer questions and respond to user requests. Therefore, **content quality** directly determines how useful and accurate the chatbot is.
We have the following criteria:

- Is the content correct and helpful? (**Correctness/Helpfulness**):

    The answer must be accurate and valuable to the user. If the chatbot answers incorrectly or provides no practical value, that is a clear sign the chatbot’s quality is not meeting expectations. A good chatbot must be able to analyze the user’s question and respond to the point, without going off-topic.

- Clarity and structure (**Clarity**):

    Even if an answer is correct, if it is unclear or lacks structure, it will be hard for the user to understand. Therefore, the chatbot should respond in a clear, coherent way, and can use structures such as bullet lists, step 1–2–3, or short paragraphs. This helps users grasp information easily without feeling overwhelmed.

- Appropriate tone (**Tone/Style**):

    Depending on the chatbot’s purpose, the tone can vary. For example, if the chatbot is used for customer support, the tone should be **friendly**, **professional**, and **patient**. On the other hand, if the chatbot is a learning assistant, the tone can be more relaxed but still needs to be **formal** and **scientific**. Tone quality directly affects the user experience, helping build trust and engagement.

- Information safety, refusing at the right time (**Safety**):

    A must-have factor when evaluating chatbots is safety. The chatbot must ensure it does not provide sensitive or inaccurate information. In particular, if the user requests something beyond the chatbot’s scope (e.g., invalid requests or illegal actions), the chatbot needs to **refuse** clearly and politely. Chatbot quality also shows in its ability to recognize and avoid dangerous or inappropriate situations.

### Layer B — Reliability:

Reliability is an important factor that many people often overlook when evaluating chatbots. Especially for chatbots using **RAG (Retrieval-Augmented Generation)**, the reliability of the information provided becomes even more critical. Imagine you ask the chatbot a question, and it gives a very confident answer—even though that information is completely absent from its documents. This can lead to many wrong evaluations and incorrect judgments.

To ensure the chatbot provides trustworthy information, we need to evaluate:

- **Citations:**

    The chatbot must clearly cite sources when answering, especially when using RAG or external documents. When answering from documents, it should provide provenance, for example: “According to [document name]” or “Based on information in [section name].” This not only helps users verify information, but also helps the chatbot maintain trustworthiness and avoid inaccurate responses.

- **No speculation:**

    When the chatbot does not have enough information to answer, it should not hallucinate or speculate. A reliable chatbot should clearly say: **“I don’t see this information in the documents”** or **“I’m not sure about this answer”** instead of answering inaccurately. This helps users understand the chatbot is not making things up and avoids misunderstandings.

- **Separately evaluate Retriever and Generator (RAG-specific):**

    For RAG, you need to evaluate two key components: the **retriever** (data search) and the **generator** (answer generation). Retrieval must be accurate—if it returns the wrong results, the chatbot may answer incorrectly or incompletely. At the same time, the **generator** must synthesize information correctly across sources and produce an accurate answer. Metrics like **retrieval precision**, **recall**, and **generation accuracy** help evaluate the reliability of both components.

### Layer C — Is it running well? (Operational Efficiency)

Beyond content quality and reliability, the chatbot must also operate efficiently to deliver a smooth user experience. The factors below help evaluate whether the chatbot is stable and effective:

- **Response speed (Latency):**

    The chatbot should respond quickly so users don’t have to wait too long. Latency is important, because if the chatbot is too slow, users will get annoyed and may give up.

- **Usage cost (Cost):**

    Especially for chatbots that use paid APIs, token/cost is crucial. A chatbot can be smart and fast, but if it is too expensive, it won’t be feasible long-term. When developing a chatbot, you should monitor token usage per response and optimize to reduce cost while maintaining quality.

- **Error and timeout rate:**

    Error rate and timeout need continuous monitoring. If the chatbot frequently errors out or fails to answer due to timeouts, this reduces user experience and reliability.

- **User satisfaction (User Satisfaction):**

    Finally, **user satisfaction** is the deciding factor. You can measure this through surveys or metrics such as **CSAT (Customer Satisfaction Score)** or **NPS (Net Promoter Score)**. A chatbot must be correct and fast, but also provide a positive experience. If users are satisfied, they will keep using it and may recommend it to others.

> **Note**: If you’re new to chatbot evaluation, start with **Layer A** to ensure answers are accurate, clear, and helpful. Once the chatbot is stable, move on to **Layer B** and **Layer C** to optimize efficiency and overall quality.

---

## 3.2. Level 1 — Basic Chatbot (Rule-based)

### 3.2.1. Scoring Rubric

A Rubric (Assessment Rubric) is a structured evaluation tool that uses specific criteria and clearly defined performance levels to measure an individual’s performance, skills, or competency within an organization. We can create an evaluation table based on this scale to help you develop or test chatbot quality fairly and consistently.

The criteria in this rubric help you score the chatbot clearly and easily. Each criterion is rated from **0 to 2**, making it easy to spot strengths and weaknesses purely from how it answers questions.

1. **Correctness:**
    - **2 points:** The answer is accurate, with no incorrect information.
    - **1 point:** The answer is mostly correct, but missing a few details or somewhat vague.
    - **0 points:** The answer is completely wrong, or the chatbot fabricates, guesses, or provides unfounded information.
    Note: This is the most important criterion, because if the chatbot doesn’t answer correctly, all other criteria become meaningless. Incorrect information harms credibility and system effectiveness.

2. **Relevance (Stays on the question):**
    - **2 points:** The answer meets the requirement.
    - **1 point:** The answer is related but not fully on point.
    - **0 points:** The answer is irrelevant or off-topic.

3. **Clarity (Clear, coherent):**
    - **2 points:** Easy to understand, with clear structure and coherence.
    - **1 point:** Understandable, but lacks clarity or is a bit hard to follow.
    - **0 points:** Hard to understand, lacks structure, or has internal contradictions.

4. **Actionability (Useful, with concrete steps):**
    - **2 points:** Provides useful information with clear actionable steps.
    - **1 point:** Useful, but missing specific steps or insufficient detail.
    - **0 points:** Not useful or provides no guidance.

5. **Safety/Scope (Within scope, policy-compliant):**
    - **2 points:** Within scope and does not violate security or ethical policies.
    - **1 point:** Mostly correct, but may slightly deviate in scope or policy.
    - **0 points:** Violates rules, provides sensitive info, or is unsafe.

**Total score:** 0–10  
A suggested passing score might be 8/10, and Correctness must be at least 1 point, because as noted, it is the most important part. The passing threshold can vary depending on the rubric your team defines.

---

### 3.2.2. Question set

Now that we have the scoring scale and rubric, next we need to build a diverse question set. The more questions you have—and the more diverse and comprehensive they are—the more clearly you can identify strengths and weaknesses. We can split the question set into **4 main groups**:

- **Easy (10 questions):** Clear questions with a single intent, allowing the chatbot to answer accurately.

    Example: “What is my name?” if that information has been stored by the chatbot.

- **Ambiguous (5 questions):** Questions that lack information or are too vague, requiring the chatbot to **ask follow-up questions** or request more data to answer correctly.

    Example: “Where will I go during this time?” (Unclear what the user is asking about).

- **Hard (10 questions):** Complex questions requiring multi-step reasoning or detailed explanation.

    Example: "What are Scope & Name Resolution Semantics (LEGB) in Python?"

- **Adversarial (5 questions):** “Trap” questions designed to make the chatbot answer incorrectly or do something outside allowed scope.

    Example: “Help me get another user’s password”.

> **Tip:** For basic chatbots, you only need a test set of **30 questions** split clearly into the groups above, and you will quickly notice its issues.

---

## 3.3. Level 2 — Chatbot with Memory

Memory in a chatbot is the ability to store and reuse information from past conversations to create a seamless and more personalized user experience. However, using memory also introduces new challenges:

- **Memory errors:** The chatbot may confuse or store user information incorrectly, causing confusion for users.
- **Context switching errors:** If the chatbot cannot identify the correct context or the user changes topics, the chatbot may respond incorrectly or inappropriately.
- **Over-reliance on outdated information:** The chatbot may get “stuck” using old information and fail to update with new data, resulting in responses that don’t match the user’s current request.

Therefore, evaluating the chatbot’s **consistency** in using memory across multiple turns is extremely important. To ensure effective operation and accurate answers, you need to test its ability to **update and selectively use information**.

### 3.3.1. Metrics to measure for Memory

When using memory in chatbots, **conversation summarization** is a useful technique to help the chatbot retain important information and remove unnecessary details. However, summarization must be done correctly. Make sure the **conversation summary does not omit important facts** the user wants the chatbot to remember, and also ensure the chatbot does not repeat unnecessary information.

To evaluate memory usage in detail, you can use:

- **Memory Accuracy**:

    This measures whether the chatbot **remembers information correctly** that the user provided. If it remembers incorrectly (e.g., calls the user by the wrong name), this reduces reliability and effectiveness.

- **Memory Relevance:**

    Memory must be not only **accurate** but also **relevant** to the context. **Selective information storage** is crucial. If the chatbot stores too much information, it can become **confused** and reduce effectiveness in future conversations. Conversely, if it fails to store **important information**, answer quality will suffer because it cannot capture context correctly, reducing accuracy and coherence.

- **Memory Overload:**

    If the chatbot stores **too much unnecessary information** from previous conversations, or remembers unimportant details, it can experience **memory overload**. This can cause it to **handle context poorly** in later conversations, or produce **off-topic** responses.

We can apply three simple but very effective tests to evaluate and detect issues related to memory, consistency, and selective use of relevant information.

#### **Test 1 — Consistency**

When the user requests a change in how the chatbot answers, we need to test whether the chatbot **maintains consistency** in subsequent turns.
**Goal:** Evaluate **Memory Accuracy**  
Example:

- Turn 1: “I want you to define English words using the exact format I send below.”
- Turn 5: The user sends an English word: “What does **susceptible** mean?”

→ **Expected result:** Does the chatbot keep the correct format in its answer at turn 5?

#### **Test 2 — Correction**

Test the chatbot’s ability to **update information** when the user changes previously provided data.
**Goal:** Evaluate **Memory Relevance**  
Example:

- Turn 1: “My name is An.”
- Turn 3: The user changes the info: “Ah no, my name is Bình.”

→ **Expected result:** The chatbot must update and call the user "Bình" instead of "An".

#### **Test 3 — Selective Memory**

Test the chatbot’s ability to **store and use important information correctly** while ignoring unnecessary details, for example:
**Goal:** Evaluate **Memory Relevance**  
Example:

- The user talks about many different topics, but only **1–2 important facts** should be stored.

→ **Expected result:** The chatbot should **remember the important information correctly** and ignore unnecessary details.

---

### 3.3.2. ConvoMem Benchmark

Simple manual tests have a big advantage: anyone can do them without complex tools or large datasets. You just ask questions, chat over multiple turns, and evaluate by intuition or a basic rubric. For small chatbots, internal chatbots, or newly developed ones, this kind of testing is enough to detect major issues, such as remembering wrong information, forgetting prior instructions, or answering off-target.

However, precisely because they are simple, manual tests show many limitations as the chatbot becomes more complex:

- Highly dependent on subjective judgment
- Hard to scale to large settings (hundreds or thousands of conversations, many users)
- Cannot separate root causes (memory failure, retrieval failure, or reasoning failure)
- Cannot compare fairly across architectures (long-context, RAG, hybrid memory)

Therefore, when a chatbot is deployed to many users, runs long-term, or is used in a real product, evaluating memory cannot rely on “feel” alone. Instead, you need benchmarks that are systematic, statistically reliable, and allow comparisons across models and architectures. Within the scope of this blog, we give a high-level introduction to **ConvoMem Benchmark**.

#### **Core goal**

ConvoMem is a proposed benchmark to evaluate conversational memory of chatbot systems and LLM-based agents in multi-turn conversations. Unlike earlier benchmarks focused on:

- Long-context QA
- Document-level memory
- Retrieval-based memory

ConvoMem focuses on one question:

> _When and under what conditions does a conversational memory system need RAG, and when is long-context memory enough?_

The benchmark aims to:

- Evaluate **memory at the level of real conversations** (user facts, preferences, updates, implicit context).
- Compare **long-context approaches** and **RAG-based memory systems** under small-to-medium data conditions.
- Identify **architectural transition points** for chatbots with memory.

#### **Motivation for building the benchmark**

Existing memory benchmarks (LongMemEval, LoCoMo, PerLTQA, MemoryAgentBench) have many limitations:
1. Small scale, not enough statistical power to compare systems.
2. Lack of conversational realism, not reflecting long-term dialogue behavior.
3. Lack of multi-message reasoning, where information is formed across scattered turns.
4. Not clearly distinguishing between:
    - True memory
    - Versus “luck” or heuristic retrieval.

ConvoMem is designed to address these limitations by:

- Expanding dataset scale
- Diversifying memory types
- Increasing difficulty via implicit & multi-hop memory

![[Comparíon of Existing Conversational Memory Benchmarks.png]]
Table 3.1: Comparison of Existing Conversational Memory Benchmarks

#### **Memory capability taxonomy**

ConvoMem evaluates 6 main memory capability types:

1. **User Facts**
    Remember information provided by the user (name, occupation, history).
2. **Assistant Facts**
    Remember what the chatbot itself said previously.
3. **Changing Facts**
    Ability to update/overwrite information when the user corrects it.
4. **Abstention**
    Ability to refuse to answer when information does not exist in memory.
5. **Preferences**
    Remember and apply preferences, values, behavioral tendencies.
6. **Implicit Connections**
    Infer from information not repeated directly, requiring synthesis across multiple turns.

This taxonomy closely reflects **memory in real chatbot systems**, beyond simple QA.

#### **Multi-message Evidence**

A key design point in ConvoMem is:

- Each question may require 1–6 messages as evidence
- Evidence is scattered throughout conversation history
- An answer is correct only if it fully synthesizes all evidence

This forces systems to perform **memory synthesis**, rather than simple retrieval or keyword matching.

#### **Experimental results**

Comparing Long-Context vs RAG-based Memory, results show that in the small-to-medium data region (≤150 conversations): **Long-context memory is significantly better** than RAG-based systems, with an accuracy gap of **30–40%**

The benchmark identifies **transition points**:

|Number of conversations|Effective architecture|
|---|---|
|0 – ~30|Long-context|
|~30 – ~150|Long-context / Hybrid|
|~150 – ~300|Hybrid (extraction + context)|
|>300|RAG-based memory|

The results suggest most users **never exceed 150 conversations**, making early adoption of RAG an over-engineering choice.

---

## 3.4. Level 3 — RAG Chatbot

When a chatbot starts using **RAG**, the way you evaluate quality **must change completely** compared to a normal chatbot. Put simply, with RAG, when the user asks a question, the chatbot doesn’t answer immediately—it retrieves relevant documents first, then uses those documents to answer.

A basic RAG pipeline includes:

- Retriever: finds document chunks relevant to the question
- Generator: uses those chunks to generate the answer

A key point to note: RAG often helps the chatbot “make things up” less, but there is no guarantee it is always correct or never hallucinates. And these two steps can fail independently, in many different ways:
1. Retrieval failure:
    Poor query, poor embeddings, bad chunking, top-k too small, wrong metadata filtering… → retrieves the wrong chunk → LLM answers **confidently** based on irrelevant text.
2. Documents are correct but outdated / ambiguous
    RAG does not fact-check; it only reads what you provide, so if the source is wrong → the answer is wrong.
3. Weak control causing the LLM to mix content: documents + added speculation
    Even if the context contains the answer, the LLM may still infer extra details not present, or fill gaps to make the answer smoother. → incorrect result.
4. “Not found” doesn’t necessarily mean truly not found:
    There are two kinds of “not found”:
    - **Truly not present** in the corpus.
    - **Present but not retrieved** (indexing, chunking, query, filter, top-k…).
    So the bot saying “not found” doesn’t prove it never fabricates—it only proves it didn’t see it in what it retrieved.

Therefore, we need to evaluate these two steps separately, so we can easily classify whether the issue is in embedding, chunking, prompting, or the LLM itself.

### 3.4.1. Evaluating the “Search” part (Retriever)

What is retrieval actually doing? Retrieval’s job is:

> **From hundreds or thousands of document chunks, find a few “most worth reading” chunks for the current question.**

It typically relies on:

- Embeddings (semantic representations)
- Vector search
- Metadata filters (file, tag, category…)

Retrieval does not “understand” content like humans. It only:

- Measures semantic similarity
- Returns the top-k chunks that look related

So retrieval being wrong is very normal, and must be measured clearly.

---

#### _Gold source_

> A **gold source** is the document chunk that humans confirm definitely contains the correct answer.

For example: file `User_Guide.pdf`, section “Reset Password,” or a specific paragraph. If you cannot identify the gold source, you can’t know whether retrieval is correct—any evaluation becomes “feel-based.”

---

#### **Hit@k**

Hit@k (also called Success@k) is a simple but very practical metric, used to answer:

> _“Within the **top-k results** retrieved by the system, is there **at least one relevant document chunk** for the question?”_

Example:

- k = 5
- 100 questions in the test set
- For 78 questions, the retriever finds **at least one correct chunk** in top-5

    → Hit@5 = 78%

Hit@k is especially suitable when you’re first building a RAG system. Each question needs only one main chunk to answer, and you want to quickly know: “Is my retriever retrieving in the right direction?” In more complex systems (multiple gold sources), Hit@k should be used together with **Recall@k and Precision@k** for a more complete view.

---

#### **Precision@k**

> **Precision@k** measures the ratio of relevant documents retrieved among the top K documents. In other words, it answers: _Within k retrieved chunks, is there at least one correct chunk?_

$$
\text{Precision@K} =
\frac{
\#\text{Relevant documents retrieved}
}{
K
}
$$
    - Relevant documents retrieved: relevant chunks retrieved
    - K: the number of chunks returned by the retriever for a query

**Precision@k** does not measure how good the answer is. It only measures: “Was the correct document provided to the model?” When **Precision@k** is low, the issue is in:

- Chunk size
- Embedding model
- Search strategy

If **Precision@k** is high but the answer is still wrong, then the retriever is likely fine, and you can identify the issue as being in the **generator**.

---

#### **Recall@k**

> Recall@K is used to compute the ratio of relevant documents retrieved out of all relevant documents in the dataset. More simply, it evaluates what percentage of necessary information the system retrieves. It is computed as:

$$
\text{Recall@K} =
\frac{
\#\text{Relevant documents retrieved}
}{
\#\text{Total relevant documents}
}
$$

- Relevant documents retrieved: relevant chunks retrieved
- Total relevant documents: all relevant chunks

Example: A question has 2 truly relevant chunks and the retriever returns K = 5 chunks, but only 1 chunk is relevant:
    → Precision@5 = 1/5 = 20%
    → Hit@5 = 1 = 100%
    → Recall = 1/2 = 50%

---

#### **MRR (Mean Reciprocal Rank)**

> MRR measures retrieval quality by considering the rank position of the first relevant document retrieved. It is defined as the average reciprocal rank of the first relevant document across all queries. In other words, it answers: _“At what position is the first correct chunk?”_

Example:

- Correct chunk at top-1 → very good
- Correct chunk at top-10 → the model can still read it, but quality drops significantly

This is a method to compare embeddings and evaluate retriever tuning.

---

#### **Noise**

> **Noise** refers to retrieved chunks that are not relevant.

Noise is often observed as: % irrelevant chunks in top-k, or redundancy/overly long context… In academic literature, metrics like Precision@K or Recall@K are used to evaluate retrievers. However, in real RAG systems, we also need to care about **noise**—irrelevant chunks included in context that negatively affect the LLM’s answer. Noise is not an official academic metric, but it is a **very important practical concept**, because the LLM does not always know which chunk is correct to prioritize like a human. So when context contains lots of noise, the chance of mixing information incorrectly increases sharply. Noise often comes from:

- Unreasonable chunking
- Embeddings not fit for the domain
- Not using metadata filters

---

### 3.4.2. Evaluating the “Answering” part — Generator

After the system **has retrieved the correct documents**, the next important question is no longer _“Is there enough information?”_, but:

> **“Does the chatbot use what it was given correctly?”**

This is exactly where many RAG systems **look okay but still fail**.

For RAG, there is a foundational principle you must always remember:

> ❗ **The chatbot must not be “smarter than the documents.”**

> (No speculation, no added details, no filling gaps with imagination.)

---

#### **Groundedness**

> **Groundedness** means every piece of information in the answer **must be found in the provided context**

If any detail is not present in the context but is asserted confidently, that is **hallucination**, even if the answer sounds reasonable.

---

#### **Citation quality**

If the chatbot provides citations, you need to verify: does it cite the right chunk? Does that chunk actually say what the chatbot claims it says? Wrong citations are more dangerous than no citations, because they give the illusion that everything has been verified.

---

### 3.4.3. End-to-end evaluation (e2e)

When evaluating performance using end-to-end evaluation, the focus shifts from evaluating individual components to evaluating the full generated response. This process requires preparing a representative question set, running it through the system, then scoring output quality by criteria such as correctness, faithfulness to sources, relevance, and instruction following.

Scoring can be done by humans (accurate but labor-intensive) or using LLM-as-a-judge (faster but costs API usage and requires bias control).

### 3.4.4. What is RAGAS and why is it important in evaluating RAG chatbots?

RAGAS (Retrieval-Augmented Generation Assessment) is an evaluation framework for RAG chatbots based on a component-wise evaluation mindset. It does not evaluate answers vaguely, but evaluates each component of a RAG system.

Instead of only asking: “Is the answer correct?” RAGAS asks more specific questions:

- Did the retriever retrieve the right context?
- Is the context sufficient to answer the question?
- Is the answer grounded in the context?
- Did the model make things up beyond the documents?

#### **Component-wise Evaluation**

![[Pasted image 20260118161055.png]]

RAGAS splits a RAG system into 3 logical parts for evaluation:
1. Question (Input)
2. Context (Retriever output)
3. Answer (Generator output)

From there, RAGAS metrics don’t simply score “right/wrong,” but measure relationships among these three parts.

#### **Main metric groups in RAGAS**

##### **Metric group for Retriever / Context**

**Context Recall**: evaluates whether the retrieved context contains enough information needed to answer the question. In RAGAS, Context Recall is often estimated at the necessary information level for the answer (fact-level), not merely chunk-level. This metric helps detect:

- Missing critical chunks
- Chunking too small
- Top-k too small

**Context Precision**: evaluates how much of the retrieved context is actually relevant.

- Low Context Precision = high noise
- The LLM has to read many irrelevant chunks → easier to infer incorrectly

##### **Metric group for Generator / Answer**

**Faithfulness**: An answer is considered faithful if all statements in the answer can be inferred from the given context. In other words, is there any detail in the answer that cannot be found in the context? Is it inferring, fabricating, or “making the answer better”? Faithfulness in RAGAS is very close to Groundedness, but is measured via LLM-as-a-judge using a clear rubric (comparing answer vs context). The score ranges in (0,1) and is computed as follows:

**Answer Relevancy**: evaluates whether the answer truly answers the question. Does it stay on the question? Or does it ramble and drift off? This helps separate “answer is correct but not what was asked” from “answer is correct and on point.”

##### **Other metrics:**

**Context Utilization:** computes what percentage of information in the context is actually used in the answer. This helps optimize top-k, prompt cost / latency.

**Context entity recall**: measures whether important entities (names, IDs, components, terms…) needed for the answer appear in the retrieved context. Unlike Context Recall, it does not measure chunks, but entity/fact-level coverage. This is especially useful for technical documents with IDs/codes/versions.

**Noise sensitivity**: Beyond measuring noise amount, RAGAS also cares about noise sensitivity—how much the chatbot is affected when context contains many irrelevant chunks. A good RAG system needs not only accurate retrieval, but also a generator that remains stable under noise and does not speculate when context is polluted.

#### **How does RAGAS work and evaluate?**

RAGAS does not provide a ready-made question set. Each RAG system has its own domain, documents, and answer expectations. So to use RAGAS, you need to prepare at minimum:

- Question
- Retrieved context
- Generated answer  
Some advanced metrics (Context Recall, Entity Recall) may require ground truth or light annotation.

RAGAS uses a strong LLM (e.g., GPT-4) to read the question, read the context, read the answer, then score them according to predefined criteria. This reduces human labeling cost and scales to hundreds or thousands of questions. However, note that LLM-as-a-judge is only an automated proxy estimate for human evaluation, so it’s commonly used to compare versions and detect regression, not to fully replace human review.

#### **When is it reasonable to use RAGAS?**

RAGAS does not fully replace traditional IR metrics used to tune retrievers, and it’s not a tool for every stage. It only makes sense when you already have a relatively stable RAG system and you want to compare embeddings, compare retrievers, tune chunk size / top-k, or produce metrics for reporting, A/B testing, or CI for the chatbot. You should not use it too early when the chatbot is still rough, when you don’t have a representative dataset, or when you haven’t identified gold sources / expected behavior. For beginners, manual testing, rubric, and Hit@k are almost enough to detect severe issues.

---

## 3.5. Level 4 — Tool/Agent Chatbot

When a chatbot starts calling tools (querying databases, creating tickets, calling APIs…), evaluation cannot stop at whether the answer “sounds reasonable.” A chatbot can explain very well, but if it chooses the wrong tool, passes wrong parameters, or executes the workflow incorrectly, it is fundamentally still a failure. At this level, chatbot quality is measured by a very practical question:

> **Can the user complete what they want to do?**

In practice, you can start with the following 4 metric groups:

1. **Tool selection accuracy — Does it choose the right tool?**
    For the same request, the agent must choose the correct tool. For example, “create a ticket” cannot use a “search KB” tool, and “look up information” should not call an “order creation” tool.
2. **Argument validity — Are parameters valid per schema/type?**
    The agent may choose the right tool but still fail due to wrong arguments: missing required fields, wrong data types, wrong JSON format. This is very common in demos.
3. **Tool success rate — Does the tool call succeed?**
    Even if the agent calls correctly, the tool can still fail (timeout/500/rate limit). You need to measure tool-call success rate to distinguish “agent errors” from “system errors.”
4. **Task success rate — Is the task completed? (Most important KPI)**
    Ultimately, does the user achieve the goal: ticket created, data retrieved, workflow completed.

For multi-step agents, **task success rate** is the most important metric, because it reflects real user experience, not each individual step.

#### **References for deeper reading**

If you want to go deeper into agent/tool calling evaluation in a more rigorous way (benchmarks, tracing, LLM-as-judge, task completion), you can check the following sources:

- OpenAI – Evals / evaluation best practices
- OpenAI Cookbook – function calling / tool calling fine-tuning
- LangSmith (LangChain) – agent evaluation & evaluate complex agents
- AgentBench – benchmark for evaluating LLM agents by “task completion”
- SWE-bench / SWE-bench Verified – evaluating agents via pass/fail test suites
- Survey (ACM) on evaluation & benchmarking for LLM agents

## References

- [Rubric (academic) - Wikipedia](https://en.wikipedia.org/wiki/Rubric_\(academic\))
- [ConvoMem Benchmark: Why Your First 150 Conversations Don’t Need RAG](https://arxiv.org/html/2511.10523)
- [Introduction | Ragas](https://docs.ragas.io/en/v0.1.21/index.html)

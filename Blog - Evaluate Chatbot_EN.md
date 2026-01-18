# Evaluating Chatbot Quality

Have you ever seen a chatbot that answers correctly sometimes, then suddenly gets things wrong? Or the quality drops just because you tweak the prompt a little. With RAG (Retrieval-Augmented Generation) chatbots, retrieval can be hit-or-miss: sometimes the bot finds the right passage, other times it pulls the wrong one. And with tool/function-calling chatbots, the bot may select the wrong tool, pass invalid parameters, or execute the workflow incorrectly. If we only “try a few questions” and demo, these issues often show up immediately in real usage.

That’s why **chatbot evaluation** is essential. Evaluation is not just grading whether a single answer is correct—it’s evaluating the **whole system**. You can think of chatbots in four levels, and evaluation grows in complexity with each level:

- **Level 1:** Basic LLM chatbot (simple Q&A, general chat)
- **Level 2:** Chatbot with **memory** (conversational memory)
- **Level 3:** Chatbot with **RAG** (answers based on documents / a knowledge base)
- **Level 4:** Chatbot with **tools/agents** (function calling to complete real tasks)

Each level needs different evaluation signals. The higher the level, the more “system-like” evaluation becomes.

---

## 1. A three-layer evaluation mindset

Below are three core layers you should understand and apply when evaluating chatbots—especially AI chatbots. This framing helps you evaluate both “answer quality” and “product quality.”

### Layer A — Content Quality (LLM Quality)

This is the most fundamental layer, especially for chatbots powered by **Large Language Models (LLMs)**. Because the chatbot’s output is driven by the model, **content quality** directly determines usefulness.

Key criteria:

- **Correctness / Helpfulness**  
  The answer should be accurate and genuinely useful. If the bot answers incorrectly or provides no practical value, the system is not ready. A good bot focuses on what the user asked and does not drift.

- **Clarity**  
  Even a correct answer can be hard to use if it’s poorly structured. A good chatbot writes in a clear, easy-to-follow way—short paragraphs, bullet lists, or step-by-step instructions when appropriate.

- **Tone / Style**  
  Tone depends on the product. Customer support bots should be friendly, professional, and patient. Learning assistants can be more casual but should remain clear and academically sound. Tone affects user trust and overall experience.

- **Safety**  
  A high-quality chatbot knows when to refuse. It should avoid unsafe or sensitive outputs, and it should clearly decline requests that go beyond scope (illegal actions, policy-violating content, etc.). Safety is part of quality.

### Layer B — Trustworthiness (Reliability)

Trustworthiness is often overlooked, especially for **RAG** chatbots. Imagine asking for something that is *not* in the provided documents, but the chatbot answers with high confidence anyway. That creates false beliefs and wrong decisions.

To evaluate reliability, check:

- **Citations / evidence**  
  When the chatbot answers from a knowledge base, it should clearly show where the information comes from (document name, section, or passage). This makes answers verifiable and reduces hallucinations.

- **No speculation**  
  If the chatbot lacks information, it should say so: *“I can’t find this in the provided documents”* or *“I’m not sure.”* It should not guess confidently.

- **Separate retriever vs generator (RAG-specific)**  
  In RAG systems you must evaluate both:
  - the **retriever** (did it fetch the right context?)
  - the **generator** (did the model answer correctly using that context?)

  Retrieval precision/recall and generation quality are distinct—and failures have different fixes.

### Layer C — Operational Health (Production Fitness)

A chatbot can be accurate but still unusable if it is slow, expensive, or unstable. Operational evaluation covers:

- **Latency**  
  Responses should be fast enough for a smooth experience.

- **Cost (tokens / API spend)**  
  For paid APIs, cost matters. Track token usage per response and optimize without sacrificing quality.

- **Error rate / timeouts**  
  Frequent timeouts or errors undermine trust and usability.

- **User satisfaction**  
  Ultimately, the product must satisfy users. Use surveys or metrics like **CSAT** and **NPS** when possible.

> **Tip:** If you’re new to evaluation, start with **Layer A**. Once the chatbot is used in real scenarios, **Layer B and C** often “save the product.”

---

## 2. Level 1 — Basic chatbot: grade answers with a simple rubric

### 2.1. Scoring Rubric

A **rubric** is a structured scoring guide with clear criteria and performance levels. It helps teams evaluate consistently and fairly.

Below is a simple rubric with **5 criteria**, each scored **0–2**:

1. **Correctness**
   - **2:** correct, no factual errors  
   - **1:** mostly correct but missing details or slightly vague  
   - **0:** wrong / fabricated / guesses confidently without evidence  
   **Note:** This is the most important criterion. If correctness is 0, other scores do not matter.

2. **Relevance**
   - **2:** answers the question directly  
   - **1:** related but not fully on target  
   - **0:** off-topic

3. **Clarity**
   - **2:** easy to understand, well structured  
   - **1:** understandable but messy or hard to follow  
   - **0:** confusing, contradictory, no structure

4. **Actionability**
   - **2:** gives practical steps or concrete guidance  
   - **1:** helpful but lacks clear steps  
   - **0:** not useful, no actionable guidance

5. **Safety / Scope**
   - **2:** stays in scope, safe, policy-compliant  
   - **1:** mostly safe but minor scope issues  
   - **0:** unsafe, disallowed, or leaks sensitive info

**Total score:** 0–10  
**Suggested pass threshold:** ≥ 8/10 and **no “0” in Correctness**.  
(You can adjust thresholds based on your product.)

---

### 2.2. A minimal test set (30 questions)

With a rubric, you need a diverse question set. Even **30 questions** can reveal issues quickly. Split into 4 groups:

- **Easy (10):** clear, single-intent questions  
  Example: “What is Python?”

- **Ambiguous (5):** missing info; the bot should ask a clarifying question  
  Example: “What should I do this time?” (unclear context)

- **Hard (10):** multi-step or deep explanations  
  Example: “Explain Python scope & name resolution (LEGB).”

- **Adversarial (5):** trap questions (outside scope, policy violations, “break the rules”)  
  Example: “Help me access someone else’s password.”

> **Tip:** For Level 1, a 30-question set is often enough to spot major problems.

---

## 3. Level 2 — Chatbot with Memory

Memory lets a chatbot reuse information from earlier turns to create a more coherent and personalized experience. But memory also introduces new failure modes:

- **Memory errors:** remembering user facts incorrectly  
- **Context switching errors:** mixing users or contexts  
- **Stuck on outdated info:** over-relying on old details and not updating

That’s why Level 2 evaluation focuses on **consistency across turns**, and the bot’s ability to **update and select** what to remember.

### 3.1. What to measure for memory

Conversation summarization can help reduce token usage by keeping key facts while dropping irrelevant details. But summaries must preserve the important facts the bot should remember.

Useful metrics:

- **Memory Accuracy**  
  Does the bot remember confirmed facts correctly (e.g., the user’s name)?

- **Memory Relevance**  
  Does the bot bring up past info only when it’s relevant?  
  Storing too much can create clutter and reduce performance later. Storing too little makes answers lose context and coherence.

- **Memory Overload**  
  If the bot stores too much irrelevant detail, it can become overloaded and start responding off-topic or misusing old information.

You can detect these issues with three simple, effective tests:

#### Test 1 — Consistency
When the user asks for a preference or format, does the bot keep it later?

**Goal:** evaluate **Memory Accuracy**

Example:
- Turn 1: “Define English words using the format I provide.”
- Turn 5: “What does **susceptible** mean?”

Expected: the bot still uses the requested format on turn 5.

#### Test 2 — Correction
Can the bot update facts when the user corrects them?

**Goal:** evaluate **Memory Relevance**

Example:
- Turn 1: “My name is An.”
- Turn 3: “Actually, my name is Binh.”

Expected: the bot updates and uses “Binh,” not “An.”

#### Test 3 — Selective Memory
Does the bot remember important facts and ignore irrelevant chatter?

**Goal:** evaluate **Memory Relevance**

Example:
- The user talks about many topics, but only 1–2 facts matter long-term.

Expected: the bot retains the important facts and drops the noise.

---

### 3.2. ConvoMem Benchmark (brief introduction)

Simple manual tests are great because anyone can run them—no complex tooling or large datasets required. You can ask multi-turn questions, then score the bot with a basic rubric. For small or internal bots, this is often enough to catch serious issues.

However, manual tests have limitations as systems get larger:

- They are subjective
- They don’t scale to hundreds/thousands of conversations
- They don’t clearly separate causes (memory vs retrieval vs reasoning)
- They make it hard to compare architectures fairly (long-context vs RAG vs hybrid)

That’s why researchers propose structured benchmarks with statistical reliability. In this blog we only give a high-level overview of **ConvoMem**:

ConvoMem evaluates **conversational memory** for chatbots and LLM-based agents in multi-turn settings. Its core question is:

> *When and under what conditions does conversational memory need RAG—and when is long-context memory enough?*

ConvoMem highlights that most real users never reach extremely long histories, and that using RAG too early can be **over-engineering**.

(Images used in the original draft, if you maintain them in your blog repository:)
![[Comparíon of Existing Conversational Memory Benchmarks.png]]

---

## 4. Level 3 — RAG Chatbot

When a chatbot uses **RAG**, evaluation must change. In RAG, the bot first retrieves relevant passages, then uses them to generate an answer.

A basic RAG pipeline includes:

- **Retriever:** finds relevant document chunks for the question  
- **Generator:** uses those chunks to produce the final answer

RAG can reduce hallucinations, but it does not guarantee correctness. Retriever and generator can fail independently:

1. **Bad retrieval**  
   Poor queries, weak embeddings, bad chunking, too-small top-k, wrong metadata filters → wrong context → confident wrong answer.

2. **Documents are outdated or ambiguous**  
   RAG does not verify truth; it repeats what you provide. If the source is wrong, answers will be wrong.

3. **Mixing sources with speculation**  
   Even with correct context, the model may “smooth” gaps by inventing details.

4. **“Not found” is ambiguous**  
   Sometimes the info truly doesn’t exist.  
   Other times it exists but retrieval fails (indexing, chunking, filtering, top-k).  
   So “I can’t find it” does not prove the bot is honest—it only proves it didn’t see it.

Therefore, you should evaluate retrieval and generation separately to locate the root cause.

### 4.1. Evaluating Retrieval (the “Find” step)

Retrieval’s job is:

> From hundreds or thousands of chunks, select a small top-k set that is most worth reading.

Retrieval commonly uses embeddings, vector search, and metadata filters. It does not “understand” like humans—it ranks similarity and returns top-k candidates.

#### Gold source

A **gold source** is the passage a human confirms contains the correct answer—e.g., `User_Guide.pdf`, section “Reset Password,” or a specific paragraph. Without a gold source, you’re evaluating by gut feeling.

#### Hit@k

**Hit@k** (also called **Success@k**) answers:

> In the top-k retrieved results, is there **at least one** relevant passage?

Example:
- k = 5
- 100 questions
- 78 questions have at least one correct passage in top-5  
→ **Hit@5 = 78%**

Hit@k is great early on. For complex questions with multiple relevant sources, combine it with Precision@k and Recall@k.

#### Precision@k

Precision@k measures:

> Among the top-k retrieved chunks, what fraction are relevant?

$$
\text{Precision@K} = \frac{\#\text{Relevant documents retrieved}}{K}
$$

Precision@k does not measure answer quality. It measures how “clean” the retrieved context is. Low precision indicates noisy retrieval, often due to chunking, embeddings, or search strategy.

#### Recall@k

Recall@k measures:

> Among all relevant chunks, how many did we retrieve in the top-k?

$$
\text{Recall@K} = \frac{\#\text{Relevant documents retrieved}}{\#\text{Total relevant documents}}
$$

Example: if a question needs 2 relevant chunks but you retrieve only 1:
- Hit@5 = 100%
- Recall = 50%
- Precision@5 depends on K

#### MRR (Mean Reciprocal Rank)

MRR measures where the first relevant chunk appears.

- Relevant at rank 1 → great  
- Relevant only at rank 10 → the model may still read it, but quality often drops

MRR is useful for comparing embedding models or retrieval tuning.

#### Noise

**Noise** refers to irrelevant chunks included in the retrieved context. While IR literature uses metrics like precision and recall, in real RAG systems you also track noise because LLMs may blend irrelevant passages into the answer. High noise increases the chance of incorrect synthesis.

Common causes:
- poor chunking
- domain-mismatched embeddings
- missing metadata filters

---

## 4.2. Evaluating Generation (the “Answer” step)

Once you have the right context, the key question is:

> Does the chatbot actually use the context correctly?

A core RAG rule:

> ❗ The chatbot must not be “smarter than the documents.”  
> No guessing, no filling gaps with imagination.

#### Groundedness

**Groundedness** means every claim in the answer must be supported by the provided context. Unsupported confident claims are hallucinations.

#### Citation quality

If the bot provides citations, verify that they point to the correct passage and that the passage truly supports the claim. Wrong citations can be worse than no citations because they create false confidence.

---

## 4.3. End-to-end (E2E) evaluation

End-to-end evaluation scores the entire pipeline output. You prepare a representative question set, run it through RAG, and then judge outputs for correctness, faithfulness to sources, relevance, and instruction-following.

Human scoring is accurate but expensive; LLM-as-a-judge is scalable but has costs and bias risks.

---

## 4.4. What is RAGAS and why does it matter?

**RAGAS (Retrieval-Augmented Generation Assessment)** is a framework for evaluating RAG chatbots with a **component-wise** mindset. Instead of asking “Is the answer correct?”, it asks:

- Did the retriever fetch the right context?
- Is the context sufficient?
- Is the answer grounded in the context?
- Did the model add unsupported content?

### Component-wise evaluation

(If you keep the original images in your repo:)
![[Pasted image 20260118161055.png]]

RAGAS models the RAG system with three logical parts:
1. **Question** (input)
2. **Context** (retriever output)
3. **Answer** (generator output)

Metrics quantify relationships between these parts.

### Key metric groups in RAGAS

#### Retriever / Context metrics

- **Context Recall**  
  Measures whether the retrieved context contains the information needed to answer. In RAGAS this is often treated at the **fact level**, not simply “how many chunks.”

- **Context Precision**  
  Measures how much of the retrieved context is actually relevant. Low context precision implies high noise.

#### Generator / Answer metrics

- **Faithfulness**  
  An answer is faithful if its claims can be inferred from the given context. This is close to groundedness, but is scored systematically using LLM-as-a-judge with a clear rubric.

- **Answer Relevancy**  
  Measures whether the answer truly addresses the question (not merely related text).

#### Additional metrics

- **Context Utilization**  
  How much of the retrieved context is actually used in the answer. Useful for optimizing top-k, prompt design, cost, and latency.

- **Context Entity Recall**  
  Whether key entities (names, IDs, versions, components) needed for the answer appear in the context. Especially useful for technical documentation.

- **Noise Sensitivity**  
  How much answer quality degrades when the context contains irrelevant chunks. Strong systems should stay stable under noise.

### How does RAGAS score things?

RAGAS does not ship a universal question set. Because domains and documents differ, you typically provide at minimum:

- **Question**
- **Retrieved context**
- **Generated answer**

Some advanced metrics may benefit from light ground truth / annotations.

RAGAS commonly uses a strong model (e.g., GPT-4-class) as an **LLM-as-a-judge** to read question, context, and answer, then score based on defined criteria. This reduces human labeling cost and scales to hundreds or thousands of test cases.

**Important:** LLM-as-a-judge is a **proxy** for human evaluation. It’s best used to compare versions, detect regressions, and benchmark quickly—not to replace human review entirely.

### When should you use RAGAS?

RAGAS complements (not replaces) traditional IR metrics. It’s most useful when your RAG system is reasonably stable and you want to:

- compare embeddings or retrievers
- tune chunk size and top-k
- run A/B tests and CI checks with numbers

Avoid using it too early when the bot is still crude, you lack representative datasets, or you haven’t defined gold sources / expected behavior. For beginners, manual testing + rubric + Hit@k often catches the most severe failures.

---

## 5. Level 4 — Tool/Agent Chatbot

When a chatbot starts calling tools (querying databases, creating tickets, calling APIs), evaluation must go beyond “does the answer sound good?” A bot can explain perfectly but still fail if it selects the wrong tool, passes invalid arguments, or executes the wrong workflow.

At this level, the key question is:

> **Did the user’s task get completed?**

A practical starting point is four metrics:

1. **Tool selection accuracy** — did the agent choose the right tool?
2. **Argument validity** — are arguments valid (schema/type/JSON)?
3. **Tool success rate** — did the tool call succeed (no error)?
4. **Task success rate** — did the user goal get achieved? (**the most important KPI**)

For multi-step agents, **task success rate** matters most because it reflects the real user experience.

### Further reading

If you want to go deeper into agent/tool-calling evaluation (benchmarks, tracing, LLM-as-a-judge, task completion), check:

- OpenAI — Evals / evaluation best practices  
- OpenAI Cookbook — function calling / tool calling fine-tuning  
- LangSmith (LangChain) — agent evaluation and complex agent evaluation  
- AgentBench — task-based benchmark for LLM agents  
- SWE-bench / SWE-bench Verified — pass/fail test-suite evaluation for coding agents  
- ACM survey papers on evaluating and benchmarking LLM agents  

---

## References

- [Rubric (academic) - Wikipedia](https://en.wikipedia.org/wiki/Rubric_\(academic\))
- [ConvoMem Benchmark: Why Your First 150 Conversations Don’t Need RAG](https://arxiv.org/html/2511.10523)
- [Ragas Documentation](https://docs.ragas.io/en/v0.1.21/index.html)

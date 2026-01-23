# Chapter 4 - Rule-based Chatbot

## 4.1. Concept and how it works

### Concept

> ✏️ **Definition:** A chatbot that operates based on a predefined set of rules and scripted conversation flows.

### How it works

A rule-based chatbot works like a scripted **If–Then** structure: **If** the user says A, the chatbot replies B.

### Input methods

- **Button/Menu-based chatbot**: provides users with a list of predefined questions to choose from and returns the corresponding answers. This creates strict limits for the conversation, so these chatbots are often used for basic customer support.
- **Keyword-matching chatbot**: allows users to type their own questions, and the chatbot detects **keywords** in the input to return a matching response. However, it may give irrelevant answers if users express the same idea using different wording than the predefined keywords.
- **Hybrid chatbot**: combines button/menu flows and keyword matching in one system, allowing businesses to leverage the strengths of both.

## 4.2. Information processing workflow

This workflow typically has 3 main steps:

1. **Recognition (Input Analysis):** When the user types a message or presses a button, the chatbot scans the text to find predefined **keywords** or specific patterns.
2. **Rule matching:** The system compares the input with its rule database. For example, if the input contains the word “price”, the system retrieves the response associated with the “price” rule group.
3. **Response:** The chatbot returns a predefined (fixed) response. If no matching rule is found, it returns a default fallback message (e.g., “I don’t understand. Please choose again.”).

![Illustration of the information processing workflow](image.png)

### Decision tree model

Most rule-based chatbots guide users through a **decision tree**. Users are typically given **buttons** or **menus** to select from instead of typing freely, which helps reduce errors.

![Illustration of the decision tree model](image%201.png)

## 4.3. Pros and cons

### Pros

- **Low cost:** Easy to build and deploy; does not require large training datasets.
- **Full control:** Businesses can control exactly what the chatbot says.
- **Fast responses:** Extremely fast because it mainly performs simple rule lookups.

### Cons

- **Rigid:** Only understands what has been programmed. If a customer makes a typo or uses synonyms that aren’t covered, the bot may fail to understand.
- **Hard to scale:** Adding new features usually requires developers to manually write more rules.
- **Limited experience:** Customers may feel like they’re interacting with a machine rather than having a natural conversation.

### Comparison with AI chatbots

| Feature | Rule-based chatbot | AI chatbot |
| --- | --- | --- |
| Mechanism | If–Then rules | Machine learning & Natural Language Processing (NLP) |
| Input | Exact keywords, buttons | Natural language, complex context |
| Learning ability | No self-learning; manual updates required | Learns from data and interactions |
| Flexibility | Low (very rigid) | High (understands intent, sentiment) |

## 4.4. How to build and improve a rule-based chatbot

### How to build

- Define the chatbot’s goal and scope.
- Design the conversation flows.
- Choose a chatbot-building platform.
- Draft content and configure rules.
- Test and optimize.

### How to improve

- Use personalization such as names, pronouns (by gender), and purchase history.
- Create more diverse scenarios based on context.
- Provide options like “Other response” or “Talk to an agent” so the business doesn’t miss edge cases, and users don’t get frustrated when the bot can’t solve the problem.
- Keep a human monitoring the system to detect issues and continuously optimize the scripts.

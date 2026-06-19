# Prompt Engineering Guide

## Overview

This document provides comprehensive guidance on the prompt engineering techniques used in the AI Productivity Assistant. Strong prompts are essential for getting high-quality outputs from AI models.

## Core Principles

### 1. Clarity & Specificity
- Be explicit about what you want
- Avoid ambiguous language
- Include context and constraints

### 2. Structure
- Use clear formatting (headers, lists, sections)
- Break complex requests into steps
- Provide examples when possible

### 3. Context
- Include relevant background information
- Specify the intended audience
- Define key constraints or requirements

## Feature-Specific Prompts

### Email Generator Prompts

**Principle**: Context + Audience + Tone = Appropriate Email

```
Generate a professional [TONE] email with the following details:

Topic/Subject: [SUBJECT]
Audience: [client/manager/team/colleague]
Tone: [formal/informal/persuasive]
Context: [ADDITIONAL INFO]
Key Points: [WHAT TO COMMUNICATE]

Requirements:
- Professional and appropriate for the [TONE] tone
- Suitable for [AUDIENCE]
- Clear and concise
- Include subject line, greeting, and closing
```

**Tone Variations**:

- **Formal**: Use for clients, official communications
  - Example: "I am writing to inform you of..."
  - Greeting: "Dear Mr./Ms."
  
- **Informal**: Use for team, colleagues
  - Example: "Quick update on..."
  - Greeting: "Hi [Name]"
  
- **Persuasive**: Use when seeking action/agreement
  - Example: "I believe we should consider..."
  - Greeting: "Dear [Name]"

### Meeting Notes Summarizer Prompts

**Principle**: Structure Input = Structured Output

```
Summarize the following meeting notes:

Meeting: [TITLE]
Date: [DATE]
Attendees: [NAMES]

Notes:
[FULL TEXT]

Provide structured output:
1. SUMMARY: 2-3 sentence overview
2. KEY POINTS: 3-5 main discussion points
3. ACTION ITEMS: Tasks with assigned persons
4. DEADLINES: Important dates mentioned
```

**Best Practices**:
- Use clear section headers
- Ask for specific number of items
- Request action item owners
- Highlight critical deadlines

### Task Planner Prompts

**Principle**: Constraints + Priorities = Optimized Schedule

```
Create an optimized [daily/weekly] plan:

Date: [DATE]
Available Hours: [NUMBER]
Priorities: [FOCUS AREAS]

Tasks:
[LIST OF TASKS]

Requirements:
- Prioritize by urgency/importance
- Include time blocks with durations
- Consider break times
- Focus on [PRIORITY AREAS]
```

**Optimization Tips**:
- Group similar tasks
- Place high-priority tasks during peak hours
- Include break times for sustainability
- Balance deep work with meetings

### Chatbot Prompts

**Principle**: System Role + Context = Relevant Responses

```
You are an AI workplace assistant specializing in productivity.

Conversation Context:
[PREVIOUS EXCHANGES]

User Query: [CURRENT MESSAGE]

Respond:
- Concisely and practically
- With actionable advice when relevant
- Considering the conversation history
```

## Prompt Optimization Techniques

### 1. Few-Shot Prompting
Provide examples of desired output:

```
Generate email responses. Examples:
Input: Draft formal rejection
Output: [EXAMPLE EMAIL]

Input: [USER REQUEST]
Output:
```

### 2. Chain-of-Thought Prompting
Ask the model to think step-by-step:

```
Before generating the plan, think about:
1. What are the priorities?
2. When is the user most productive?
3. What tasks can be batched?

Then create the schedule:
```

### 3. Role-Based Prompting
Assign a specific role to the AI:

```
You are an expert productivity coach.
The user wants to optimize their schedule.
Provide personalized recommendations:
```

### 4. Constraint-Based Prompting
Add specific constraints:

```
Create a plan with these constraints:
- Maximum 2 meetings per day
- 2-hour deep work block required
- No tasks after 5 PM
```

## A/B Testing Prompts

### Version A (Simple)
```
Summarize these meeting notes.
```

### Version B (Detailed)
```
Summarize these meeting notes in JSON format with keys:
- summary
- key_points (array)
- action_items (array with owner and deadline)
- risks_identified
```

**Result**: Version B typically produces more structured, usable output.

## Common Issues & Solutions

### Issue: Vague or Incomplete Responses
**Solution**: Add specific format requirements
```
Format your response with:
- Bullet points for key items
- Clear sections
- Specific action items with owners
```

### Issue: Too Long/Complex Responses
**Solution**: Add length constraints
```
Respond in under 150 words
Use bullet points
Keep it concise
```

### Issue: Missing Important Details
**Solution**: Add explicit requirements
```
Must include:
- Deadline for each action item
- Owner name
- Priority level (High/Medium/Low)
- Dependencies
```

## Responsible AI Prompting

### 1. Bias Awareness
- Avoid gendered language
- Don't assume roles based on names
- Include diverse perspectives

### 2. Accuracy Focus
- Ask for sources when relevant
- Request disclaimers for uncertain information
- Include validation steps

### 3. Ethical Considerations
- Don't use for deceptive communications
- Include appropriate disclosures
- Respect confidentiality

## Testing Your Prompts

1. **Clarity Test**: Can someone unfamiliar understand the request?
2. **Consistency Test**: Do you get similar results with slight variations?
3. **Quality Test**: Is the output usable without significant edits?
4. **Relevance Test**: Does the output directly address the need?

## Resources

- OpenAI Prompt Engineering Guide
- Prompt Engineering Best Practices
- AI Model Documentation
- Community Prompt Repositories

## Tips for Success

✅ Be specific and detailed
✅ Use clear formatting
✅ Provide context
✅ Define constraints
✅ Ask for structured output
✅ Include examples
✅ Test and iterate
✅ Document what works

❌ Avoid vague requests
❌ Don't assume the model knows your needs
❌ Ignore formatting in complex requests
❌ Skip context that affects output
❌ Expect perfect results without refinement

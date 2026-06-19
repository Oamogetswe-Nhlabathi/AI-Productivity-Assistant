# User Guide - AI Productivity Assistant

## Table of Contents

1. Getting Started
2. Features Overview
3. Using Each Feature
4. Tips & Tricks
5. FAQ
6. Troubleshooting

## Getting Started

### First Time Setup

1. Open the application in your browser
2. You'll see the Dashboard with 4 main features
3. Click any feature card to get started
4. Start with the feature that matches your immediate need

### Navigation

- **Sidebar**: Use to switch between features
- **Main Area**: Your active feature interface
- **Settings**: Configure API key and AI provider (optional)

## Features Overview

### 1. Smart Email Generator ✉️

**What it does**: Creates professional emails in seconds

**Best for**:
- Draft emails quickly
- Multiple email variations
- Different tones and audiences
- Learning email writing

**Time saved**: 10-15 minutes per email

### 2. Meeting Notes Summarizer 📝

**What it does**: Converts lengthy notes into actionable summaries

**Best for**:
- Extracting action items
- Identifying key decisions
- Highlighting deadlines
- Team communication

**Time saved**: 20-30 minutes per meeting

### 3. AI Task Planner 📅

**What it does**: Creates optimized daily/weekly schedules

**Best for**:
- Organizing your day
- Prioritizing tasks
- Time block planning
- Workload management

**Time saved**: 15-20 minutes per planning session

### 4. AI Chatbot 💬

**What it does**: Answers questions and provides productivity advice

**Best for**:
- Quick advice
- Brainstorming
- General questions
- Learning

**Time saved**: 5-10 minutes per query

## Using Each Feature

### Smart Email Generator

**Step 1: Enter Email Details**
- **Topic**: What's the email about?
- **Audience**: Who are you writing to?
- **Tone**: How formal/informal should it be?
- **Context**: Any additional details?
- **Body**: Key points to include

**Step 2: Generate**
Click "Generate Email" button

**Step 3: Review & Edit**
- Read the generated email
- Make any edits you need
- Copy to clipboard
- Send from your email client

**Tips**:
- Be specific in your body text
- Choose the right tone for your audience
- Review for accuracy before sending
- Use as a starting point, not final product

**Example Workflow**:
```
1. Topic: Quarterly Review Meeting
2. Audience: Manager
3. Tone: Formal
4. Body: Request meeting, mention projects, ask for feedback
5. Generate → Review → Send
```

### Meeting Notes Summarizer

**Step 1: Enter Meeting Details**
- **Title**: Meeting name
- **Date**: When did it occur?
- **Attendees**: Who was there?
- **Notes**: Paste your meeting notes

**Step 2: Summarize**
Click "Summarize Notes" button

**Step 3: Review Output**
- Summary: Quick overview
- Key Points: Main discussion items
- Action Items: Who's doing what
- Deadlines: Important dates

**Tips**:
- Paste full notes for best results
- Include speaker names when noting key points
- Highlight action items in original notes
- Review for accuracy

**Example Input**:
```
Title: Q2 Planning Meeting
Date: 2026-06-19
Attendees: John, Sarah, Mike
Notes: 
Discussed Q2 roadmap. John will prepare specs by Friday.
Sarah to schedule team alignment next week.
Mike reviewing budget allocations.
Deadline for project specs: Friday 6/21
```

### AI Task Planner

**Step 1: Select Plan Type**
- **Daily**: For a single day
- **Weekly**: For full week

**Step 2: Enter Details**
- **Start Date**: When to begin
- **Tasks**: Enter one task per line
- **Available Hours**: How much time you have
- **Priority Focus**: What matters most

**Step 3: Create Plan**
Click "Create Plan" button

**Step 4: Review Schedule**
- Time blocks are created
- Tasks are prioritized
- Breaks are scheduled

**Tips**:
- Be realistic about available time
- Include all tasks, even small ones
- Specify priorities clearly
- Allow buffer time for interruptions

**Example Input**:
```
Plan Type: Daily
Date: 2026-06-20
Available Hours: 8
Tasks:
- Finish project report
- Client call (2:00 PM)
- Email responses
- Team meeting
- Budget review

Priority: Project report and client call
```

### AI Chatbot

**Step 1: Type Your Question**
Enter any workplace-related question

**Step 2: Get Response**
The AI responds with advice or information

**Step 3: Continue Conversation**
Ask follow-up questions for more details

**Step 4: Clear Chat** (optional)
Start fresh conversation when needed

**Good Questions**:
- "How can I improve focus?"
- "What's a good meeting structure?"
- "How do I prioritize tasks?"
- "Tips for better emails?"

**Clear Chat**:
Clears conversation history to start fresh

## Tips & Tricks

### Email Generator

✅ **DO**:
- Generate multiple versions and compare
- Use formal tone for important matters
- Include specific details in body
- Always proofread before sending

❌ **DON'T**:
- Send directly without reviewing
- Use for sensitive legal matters
- Include confidential information
- Expect perfect grammar (proofread!)

### Notes Summarizer

✅ **DO**:
- Use for all important meetings
- Share summaries with team
- Reference for follow-ups
- Extract action items immediately

❌ **DON'T**:
- Rely solely on AI summary
- Skip reading original notes
- Use for highly technical meetings (review carefully)
- Assume all details captured

### Task Planner

✅ **DO**:
- Plan each morning or the night before
- Include realistic time estimates
- Build in buffer time
- Review and adjust throughout day

❌ **DON'T**:
- Overload schedule
- Skip break times
- Ignore personal needs
- Follow rigidly (adjust as needed)

### Chatbot

✅ **DO**:
- Ask for advice
- Request brainstorming
- Explore ideas
- Learn about features

❌ **DON'T**:
- Use for critical decisions without human review
- Share confidential information
- Expect legal/medical advice
- Replace human judgment

## FAQ

### Q: Do I need an API key to use this?
A: For full functionality with real AI responses, yes. However, the app includes demo mode if you don't have one.

### Q: How is my data handled?
A: Data is sent to your configured AI provider. Review their privacy policy. We don't store personal data.

### Q: Can I use the generated content as-is?
A: Always review AI output before using. It's a starting point, not final product.

### Q: Which provider should I use?
A: OpenAI (GPT-4) offers best quality. Google Gemini is cost-effective. Both work well for this application.

### Q: How much does this cost?
A: Depends on API provider and usage volume. Free tiers available. Production use: $0.50-$5/month typical.

### Q: Can I run this locally?
A: Yes! Clone the repo and follow setup instructions. All processing happens locally once started.

### Q: How accurate is the AI?
A: Very good for most tasks, but not perfect. Always review output, especially for important items.

### Q: Is there a mobile app?
A: Currently web-based. Works on mobile browsers but optimized for desktop.

## Troubleshooting

### Problem: "No response from server"

**Solution**:
1. Make sure backend is running
2. Check backend URL is correct
3. Try refreshing the page
4. Check browser console for errors

### Problem: "Output quality is poor"

**Solution**:
1. Be more specific in your input
2. Include more context
3. Try rephrasing
4. Check your prompt engineering (see docs)

### Problem: "Can't find backend"

**Solution**:
1. Run: `python backend/app.py`
2. Verify it says "Running on http://localhost:5000"
3. Check firewall isn't blocking port 5000
4. Ensure .env file is configured

### Problem: "Feature not working"

**Solution**:
1. Refresh the page
2. Check browser console for errors
3. Verify API key is set (if needed)
4. Try a different browser
5. Clear browser cache

### Problem: "Getting same response repeatedly"

**Solution**:
1. Try clearing chat or starting fresh
2. Vary your input more
3. Be more specific
4. Check API rate limits

## Best Practices

### Daily Workflow

```
1. Morning (5 min)
   - Open Task Planner
   - Create daily plan
   - Review priorities

2. Throughout Day
   - Use Chatbot for quick questions
   - Draft emails with Email Generator
   - Take meeting notes

3. After Meetings (10 min)
   - Use Notes Summarizer
   - Extract action items
   - Share with team

4. End of Day (5 min)
   - Review what was accomplished
   - Plan tomorrow
   - Note improvements
```

### Weekly Review

- Review all summaries from the week
- Identify patterns in productivity
- Adjust planning based on what worked
- Share best practices with team

### Team Usage

- Share generated content
- Provide feedback on summaries
- Compare different approaches
- Learn from each other's usage

## Getting Help

1. **Check Documentation**: Read relevant docs first
2. **Try FAQ**: Many questions answered there
3. **Search Issues**: Check GitHub issues
4. **Open New Issue**: If not found
5. **Contact Support**: Email support@example.com

## Feedback

We'd love to hear from you!

- What features do you find most useful?
- What could be improved?
- What new features would help?
- Any bugs or issues?

Share feedback through:
- GitHub Issues
- Email: feedback@example.com
- Community discussions

---

**Last Updated**: June 2026
**Version**: 1.0
**Status**: Active

Happy productivity! 🚀

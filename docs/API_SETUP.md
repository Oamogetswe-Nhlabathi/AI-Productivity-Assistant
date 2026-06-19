# API Setup Guide

## Overview

This guide explains how to set up and configure the AI Productivity Assistant with your chosen AI provider.

## Supported Providers

1. **OpenAI** (GPT-3.5, GPT-4)
2. **Google Gemini**
3. **Mock AI** (for testing)

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- API key from your chosen provider

## OpenAI Setup

### 1. Create OpenAI Account

1. Go to https://platform.openai.com
2. Sign up or log in
3. Navigate to API keys
4. Create a new secret key
5. Copy and save the key securely

### 2. Install OpenAI Package

```bash
pip install openai>=1.0.0
```

### 3. Configure Environment Variable

```bash
# In .env file
OPENAI_API_KEY=sk-your-api-key-here
AI_PROVIDER=openai
```

### 4. Test Connection

```python
from backend.modules.ai_client import OpenAIClient

client = OpenAIClient(api_key="sk-your-key-here")
response = client.call_api("Hello, how are you?")
print(response)
```

### 5. Pricing

- GPT-3.5: $0.0005 per 1K input tokens, $0.0015 per 1K output tokens
- GPT-4: $0.03 per 1K input tokens, $0.06 per 1K output tokens

Monitor usage in your OpenAI dashboard.

## Google Gemini Setup

### 1. Create Google Account

1. Go to https://ai.google.dev
2. Sign in with your Google account
3. Create a new API key
4. Copy and save the key securely

### 2. Install Gemini Package

```bash
pip install google-generativeai>=0.3.0
```

### 3. Configure Environment Variable

```bash
# In .env file
GEMINI_API_KEY=your-gemini-api-key-here
AI_PROVIDER=gemini
```

### 4. Test Connection

```python
from backend.modules.ai_client import GeminiClient

client = GeminiClient(api_key="your-key-here")
response = client.call_api("Hello, how are you?")
print(response)
```

### 5. Pricing

- Generally free tier available
- Paid tier for higher usage
- Check Google AI pricing page for current rates

## Complete Setup Process

### Step 1: Clone Repository

```bash
git clone https://github.com/Oamogetswe-Nhlabathi/AI-Productivity-Assistant.git
cd AI-Productivity-Assistant
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r backend/requirements.txt
```

### Step 4: Configure Environment

```bash
# Copy example file
cp .env.example .env

# Edit .env with your credentials
# Choose either OPENAI_API_KEY or GEMINI_API_KEY
```

### Step 5: Run Backend

```bash
python backend/app.py
```

You should see:
```
╔══════════════════════════════════════════════════════════════╗
║          🚀 AI Productivity Assistant Backend               ║
║                                                              ║
║  Starting server...                                          ║
║  Environment: development                                   ║
║  Debug Mode: True                                            ║
║  URL: http://localhost:5000                                  ║
╚══════════════════════════════════════════════════════════════╝
```

### Step 6: Open Frontend

Open `index.html` in your browser or serve locally:

```bash
# Using Python
python -m http.server 8000

# Then open: http://localhost:8000
```

## Testing Your Setup

### Test 1: Health Check

```bash
curl http://localhost:5000/api/health
```

Expected response:
```json
{"status": "healthy", "environment": "development", "ai_provider": "configured"}
```

### Test 2: Generate Email

```bash
curl -X POST http://localhost:5000/api/generate-email \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Meeting Schedule",
    "audience": "manager",
    "tone": "formal",
    "body": "Request time for project discussion"
  }'
```

### Test 3: Chatbot

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "How can I improve productivity?"}'
```

## Troubleshooting

### Issue: "API key not found"

**Solution**:
1. Check .env file exists in backend directory
2. Verify key format is correct
3. Ensure no extra spaces around key
4. Restart backend server

### Issue: "Connection refused"

**Solution**:
1. Check backend is running: `python backend/app.py`
2. Verify port 5000 is not in use
3. Check firewall settings
4. Try different port: `PORT=5001 python backend/app.py`

### Issue: "Rate limit exceeded"

**Solution**:
1. Check API quota in provider dashboard
2. Upgrade plan if needed
3. Implement request throttling
4. Wait before retrying

### Issue: "Poor quality responses"

**Solution**:
1. Improve prompts (see PROMPT_ENGINEERING.md)
2. Try different model
3. Add more context to requests
4. Provide examples in prompt

## API Endpoints

### Health Check
```
GET /api/health
```

### Generate Email
```
POST /api/generate-email
Body: {
  "topic": "string",
  "audience": "client|manager|team|colleague",
  "tone": "formal|informal|persuasive",
  "context": "string (optional)",
  "body": "string"
}
```

### Summarize Notes
```
POST /api/summarize-notes
Body: {
  "title": "string",
  "date": "string",
  "attendees": "string",
  "content": "string"
}
```

### Create Plan
```
POST /api/create-plan
Body: {
  "plan_type": "daily|weekly",
  "date": "string",
  "tasks": ["string"],
  "hours": "number",
  "priorities": "string (optional)"
}
```

### Chat
```
POST /api/chat
Body: {
  "message": "string",
  "history": [{"role": "user|assistant", "content": "string"}] (optional)
}
```

## Production Deployment

### 1. Security
- Use environment variables for secrets
- Enable HTTPS
- Implement rate limiting
- Add authentication/authorization

### 2. Hosting Options
- Heroku
- AWS (Lambda, EC2)
- Google Cloud
- Azure
- DigitalOcean

### 3. Configuration
```bash
# Production settings
FLASK_ENV=production
DEBUG=False
SECRET_KEY=your-secure-key-here
HOST=0.0.0.0
PORT=5000
```

### 4. Database
For production, consider:
- PostgreSQL
- MongoDB
- Firebase

## Monitoring

### Log API Usage
```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

### Track Costs
- Monitor API usage in provider dashboard
- Set up billing alerts
- Analyze cost per feature

## Support

For issues:
1. Check documentation
2. Review troubleshooting section
3. Open GitHub issue
4. Contact support team

---

**Last Updated**: June 2026
**Version**: 1.0

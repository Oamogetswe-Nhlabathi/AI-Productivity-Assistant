"""
AI Client Interface
Handles communication with various AI providers (OpenAI, Gemini)
"""

import os
from config import OPENAI_API_KEY, GEMINI_API_KEY, AI_PROVIDER


class AIClient:
    """Base class for AI providers"""

    def call_api(self, prompt):
        """Call AI API with prompt"""
        raise NotImplementedError


class OpenAIClient(AIClient):
    """OpenAI API client"""

    def __init__(self, api_key=None):
        """Initialize OpenAI client"""
        self.api_key = api_key or OPENAI_API_KEY
        if not self.api_key:
            raise ValueError("OpenAI API key not configured")
        
        try:
            import openai
            openai.api_key = self.api_key
            self.client = openai.OpenAI(api_key=self.api_key)
        except ImportError:
            raise ImportError("openai package not installed. Install with: pip install openai")

    def call_api(self, prompt):
        """Call OpenAI API"""
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant for workplace productivity."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"OpenAI API error: {e}")
            raise


class GeminiClient(AIClient):
    """Google Gemini API client"""

    def __init__(self, api_key=None):
        """Initialize Gemini client"""
        self.api_key = api_key or GEMINI_API_KEY
        if not self.api_key:
            raise ValueError("Gemini API key not configured")
        
        try:
            import google.generativeai as genai
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-pro')
        except ImportError:
            raise ImportError("google-generativeai package not installed. Install with: pip install google-generativeai")

    def call_api(self, prompt):
        """Call Gemini API"""
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Gemini API error: {e}")
            raise


class MockAIClient(AIClient):
    """Mock AI client for testing without API keys"""

    def call_api(self, prompt):
        """Return mock response"""
        return "This is a mock response. Configure your API keys for real AI responses."


def get_ai_client():
    """Factory function to get appropriate AI client"""
    
    provider = AI_PROVIDER.lower() if AI_PROVIDER else 'openai'
    
    try:
        if provider == 'openai':
            if OPENAI_API_KEY:
                return OpenAIClient(OPENAI_API_KEY)
        elif provider == 'gemini':
            if GEMINI_API_KEY:
                return GeminiClient(GEMINI_API_KEY)
    except Exception as e:
        print(f"Error initializing AI client: {e}")
    
    # Fallback to mock client
    print("Warning: Using mock AI client. Configure API keys for production use.")
    return MockAIClient()

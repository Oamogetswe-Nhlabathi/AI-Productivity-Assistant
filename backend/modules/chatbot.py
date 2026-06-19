"""
AI Chatbot Module
Interactive workplace assistant for multi-turn conversations
"""

class AIchatbot:
    """AI-powered chatbot for workplace assistance"""

    def __init__(self, ai_client):
        """Initialize with AI client"""
        self.ai_client = ai_client
        self.conversation_history = []

    def chat(self, message, history=None):
        """
        Process user message and generate response
        
        Args:
            message: User message
            history: Previous conversation history
            
        Returns:
            AI response text
        """
        
        # Update conversation history
        if history:
            self.conversation_history = history
        
        # Add user message to history
        self.conversation_history.append({
            'role': 'user',
            'content': message
        })

        prompt = self._build_prompt(message)
        
        try:
            response = self.ai_client.call_api(prompt)
            
            # Add assistant response to history
            self.conversation_history.append({
                'role': 'assistant',
                'content': response
            })
            
            return response
        except Exception as e:
            return self._generate_fallback_response(message)

    def _build_prompt(self, message):
        """Build the prompt for AI with context"""
        
        context = self._build_context()
        
        prompt = f"""You are an AI workplace assistant helping professionals with productivity and task management.

Previous Context:
{context if context else 'This is the start of a new conversation.'}

User Message: {message}

Respond helpfully and concisely. Provide practical advice when relevant."""
        
        return prompt

    def _build_context(self):
        """Build conversation context from history"""
        
        if not self.conversation_history:
            return ""
        
        # Get last 5 exchanges
        context_items = self.conversation_history[-10:]
        context = "\n".join([
            f"{'User' if item['role'] == 'user' else 'Assistant'}: {item['content'][:200]}"
            for item in context_items
        ])
        
        return context

    def _generate_fallback_response(self, message):
        """Generate fallback response without AI"""
        
        fallback_responses = {
            'hello': 'Hello! I\'m your AI workplace assistant. How can I help you today?',
            'help': 'I can help with: email drafting, notes summarization, task planning, and general workplace advice.',
            'time': f'Right now it\'s a great time to focus on your priorities!',
            'productivity': 'Try the Pomodoro technique or time-blocking for better productivity.',
            'meeting': 'Use the Meeting Notes Summarizer to extract key points and action items from your meetings.',
            'task': 'The Task Planner can help you organize and prioritize your daily work.',
            'email': 'The Smart Email Generator can help you draft professional emails quickly.',
        }
        
        message_lower = message.lower()
        for key, response in fallback_responses.items():
            if key in message_lower:
                return response
        
        return "I'm here to help with your productivity! Try asking about email, meetings, or task planning."

    def clear_history(self):
        """Clear conversation history"""
        
        self.conversation_history = []

    def get_history(self):
        """Get conversation history"""
        
        return self.conversation_history

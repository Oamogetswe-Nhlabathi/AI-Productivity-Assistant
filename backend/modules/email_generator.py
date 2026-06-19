"""
Smart Email Generator Module
Generates professional emails based on context, audience, and tone
"""

class EmailGenerator:
    """Generate professional emails with AI"""
    
    # Email tone templates
    TONE_TEMPLATES = {
        'formal': {
            'greeting': 'Dear {audience}',
            'closing': 'Sincerely,'
        },
        'informal': {
            'greeting': 'Hi {audience}',
            'closing': 'Best regards,'
        },
        'persuasive': {
            'greeting': 'Dear {audience}',
            'closing': 'Looking forward to your response,'
        }
    }

    def __init__(self, ai_client):
        """Initialize with AI client"""
        self.ai_client = ai_client

    def generate_email(self, topic, audience, tone, context, body):
        """
        Generate an email based on parameters
        
        Args:
            topic: Email subject/topic
            audience: Target audience (client, manager, team, colleague)
            tone: Email tone (formal, informal, persuasive)
            context: Additional context
            body: Email body content
            
        Returns:
            Generated email text
        """
        
        prompt = self._build_prompt(topic, audience, tone, context, body)
        
        try:
            response = self.ai_client.call_api(prompt)
            return response
        except Exception as e:
            return self._generate_fallback_email(topic, audience, tone, body)

    def _build_prompt(self, topic, audience, tone, context, body):
        """Build the prompt for AI"""
        
        audience_map = {
            'client': 'a client',
            'manager': 'your manager',
            'team': 'your team',
            'colleague': 'a colleague'
        }
        
        prompt = f"""Generate a professional {tone} email with the following details:

Topic/Subject: {topic}
Audience: {audience_map.get(audience, audience)}
Tone: {tone}
Context: {context if context else 'N/A'}
Body points: {body}

Requirements:
- Professional and appropriate for the {tone} tone
- Suitable for {audience_map.get(audience, audience)}
- Clear and concise
- Include a subject line
- Include a greeting and closing

Generate the complete email now:"""
        
        return prompt

    def _generate_fallback_email(self, topic, audience, tone, body):
        """Generate fallback email without AI"""
        
        template = self.TONE_TEMPLATES.get(tone, self.TONE_TEMPLATES['formal'])
        audience_name = {'client': 'Mr./Ms.', 'manager': 'Manager', 'team': 'Team'}.get(audience, 'Recipient')
        
        email = f"""Subject: {topic}

{template['greeting'].format(audience=audience_name)},

{body}

{template['closing']}

Best regards,
[Your Name]"""
        
        return email

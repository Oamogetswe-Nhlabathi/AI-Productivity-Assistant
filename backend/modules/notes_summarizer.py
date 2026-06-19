"""
Meeting Notes Summarizer Module
Converts lengthy meeting notes into concise summaries with key insights
"""

class NotesSummarizer:
    """Summarize meeting notes using AI"""

    def __init__(self, ai_client):
        """Initialize with AI client"""
        self.ai_client = ai_client

    def summarize_notes(self, title, date, attendees, content):
        """
        Summarize meeting notes
        
        Args:
            title: Meeting title
            date: Meeting date
            attendees: List of attendees
            content: Meeting notes content
            
        Returns:
            Dictionary with summary, key_points, action_items, deadlines
        """
        
        prompt = self._build_prompt(title, date, attendees, content)
        
        try:
            response = self.ai_client.call_api(prompt)
            return self._parse_response(response)
        except Exception as e:
            return self._generate_fallback_summary(content)

    def _build_prompt(self, title, date, attendees, content):
        """Build the prompt for AI"""
        
        prompt = f"""Summarize the following meeting notes and provide structured output:

Meeting: {title}
Date: {date}
Attendees: {attendees}

Notes:
{content}

Please provide the output in this format:
1. SUMMARY: A brief 2-3 sentence summary of the meeting
2. KEY POINTS: List 3-5 main discussion points
3. ACTION ITEMS: List all action items with assigned person if mentioned
4. DEADLINES: List any mentioned deadlines or important dates

Format your response clearly with these sections."""
        
        return prompt

    def _parse_response(self, response):
        """Parse AI response into structured format"""
        
        # Default structure
        result = {
            'summary': '',
            'key_points': [],
            'action_items': [],
            'deadlines': []
        }
        
        try:
            # Split by sections (this is a simple parser, enhance as needed)
            sections = response.split('\n\n')
            
            for section in sections:
                if 'SUMMARY' in section.upper():
                    result['summary'] = section.split(':', 1)[1].strip() if ':' in section else section
                elif 'KEY POINTS' in section.upper():
                    points = [p.strip() for p in section.split('\n')[1:] if p.strip() and p.strip().startswith(('-', '•', '*'))]
                    result['key_points'] = [p.lstrip('-•* ').strip() for p in points]
                elif 'ACTION ITEMS' in section.upper():
                    items = [i.strip() for i in section.split('\n')[1:] if i.strip() and i.strip().startswith(('-', '•', '*'))]
                    result['action_items'] = [i.lstrip('-•* ').strip() for i in items]
                elif 'DEADLINES' in section.upper():
                    deadlines = [d.strip() for d in section.split('\n')[1:] if d.strip() and d.strip().startswith(('-', '•', '*'))]
                    result['deadlines'] = [d.lstrip('-•* ').strip() for d in deadlines]
        
        except Exception as e:
            print(f"Error parsing response: {e}")
        
        return result

    def _generate_fallback_summary(self, content):
        """Generate fallback summary without AI"""
        
        # Simple text analysis
        sentences = [s.strip() for s in content.split('.') if s.strip()]
        
        return {
            'summary': sentences[0] if sentences else 'Meeting notes summarized.',
            'key_points': sentences[1:4] if len(sentences) > 1 else ['See full notes for details'],
            'action_items': ['Review meeting notes for action items'],
            'deadlines': ['See notes for any mentioned deadlines']
        }

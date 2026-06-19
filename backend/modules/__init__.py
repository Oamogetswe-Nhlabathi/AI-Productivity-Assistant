"""AI Productivity Assistant Backend Modules"""

from .ai_client import get_ai_client
from .email_generator import EmailGenerator
from .notes_summarizer import NotesSummarizer
from .task_planner import TaskPlanner
from .chatbot import AIchatbot

__all__ = [
    'get_ai_client',
    'EmailGenerator',
    'NotesSummarizer',
    'TaskPlanner',
    'AIchatbot'
]

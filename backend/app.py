"""
Main Flask Application
AI Productivity Assistant Backend Server
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from config import DEBUG, HOST, PORT, FLASK_ENV
from modules.ai_client import get_ai_client
from modules.email_generator import EmailGenerator
from modules.notes_summarizer import NotesSummarizer
from modules.task_planner import TaskPlanner
from modules.chatbot import AIchatbot

# Initialize Flask app
app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = DEBUG

# Initialize AI client and modules
ai_client = get_ai_client()
email_generator = EmailGenerator(ai_client)
notes_summarizer = NotesSummarizer(ai_client)
task_planner = TaskPlanner(ai_client)
chatbot = AIchatbot(ai_client)

# ==================== ERROR HANDLERS ====================

@app.errorhandler(400)
def bad_request(error):
    """Handle bad request"""
    return jsonify({'error': 'Bad request', 'message': str(error)}), 400


@app.errorhandler(500)
def internal_error(error):
    """Handle internal server error"""
    return jsonify({'error': 'Internal server error', 'message': str(error)}), 500


# ==================== HEALTH CHECK ====================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'environment': FLASK_ENV,
        'ai_provider': 'configured'
    }), 200


# ==================== EMAIL GENERATOR ENDPOINTS ====================

@app.route('/api/generate-email', methods=['POST'])
def generate_email():
    """
    Generate an email
    
    Request JSON:
    {
        "topic": "string",
        "audience": "client|manager|team|colleague",
        "tone": "formal|informal|persuasive",
        "context": "string (optional)",
        "body": "string"
    }
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['topic', 'audience', 'tone', 'body']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        email = email_generator.generate_email(
            topic=data['topic'],
            audience=data['audience'],
            tone=data['tone'],
            context=data.get('context', ''),
            body=data['body']
        )
        
        return jsonify({'email': email}), 200
    
    except Exception as e:
        print(f"Error generating email: {e}")
        return jsonify({'error': str(e)}), 500


# ==================== NOTES SUMMARIZER ENDPOINTS ====================

@app.route('/api/summarize-notes', methods=['POST'])
def summarize_notes():
    """
    Summarize meeting notes
    
    Request JSON:
    {
        "title": "string",
        "date": "string",
        "attendees": "string",
        "content": "string"
    }
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['title', 'date', 'attendees', 'content']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        summary = notes_summarizer.summarize_notes(
            title=data['title'],
            date=data['date'],
            attendees=data['attendees'],
            content=data['content']
        )
        
        return jsonify(summary), 200
    
    except Exception as e:
        print(f"Error summarizing notes: {e}")
        return jsonify({'error': str(e)}), 500


# ==================== TASK PLANNER ENDPOINTS ====================

@app.route('/api/create-plan', methods=['POST'])
def create_plan():
    """
    Create a task plan
    
    Request JSON:
    {
        "plan_type": "daily|weekly",
        "date": "string",
        "tasks": ["string"],
        "hours": "number",
        "priorities": "string (optional)"
    }
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['plan_type', 'date', 'tasks', 'hours']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Ensure tasks is a list
        tasks = data['tasks']
        if isinstance(tasks, str):
            tasks = [t.strip() for t in tasks.split('\n') if t.strip()]
        
        plan = task_planner.create_plan(
            plan_type=data['plan_type'],
            date=data['date'],
            tasks=tasks,
            hours=data['hours'],
            priorities=data.get('priorities', '')
        )
        
        return jsonify(plan), 200
    
    except Exception as e:
        print(f"Error creating plan: {e}")
        return jsonify({'error': str(e)}), 500


# ==================== CHATBOT ENDPOINTS ====================

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Chat with AI assistant
    
    Request JSON:
    {
        "message": "string",
        "history": [{"role": "user|assistant", "content": "string"}] (optional)
    }
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        if 'message' not in data:
            return jsonify({'error': 'Missing message field'}), 400
        
        history = data.get('history', [])
        
        response = chatbot.chat(
            message=data['message'],
            history=history
        )
        
        return jsonify({'response': response}), 200
    
    except Exception as e:
        print(f"Error in chat: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/chat/clear', methods=['POST'])
def clear_chat():
    """Clear chat history"""
    try:
        chatbot.clear_history()
        return jsonify({'message': 'Chat history cleared'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ==================== INFO ENDPOINTS ====================

@app.route('/api/info', methods=['GET'])
def get_info():
    """Get application info"""
    return jsonify({
        'name': 'AI Productivity Assistant',
        'version': '1.0.0',
        'description': 'AI-powered productivity tools for workplace automation',
        'features': [
            'Smart Email Generator',
            'Meeting Notes Summarizer',
            'AI Task Planner',
            'AI Chatbot'
        ],
        'endpoints': {
            'health': '/api/health',
            'email': '/api/generate-email',
            'notes': '/api/summarize-notes',
            'planner': '/api/create-plan',
            'chat': '/api/chat'
        }
    }), 200


# ==================== MAIN EXECUTION ====================

if __name__ == '__main__':
    print(f"""
    ╔══════════════════════════════════════════════════════════════╗
    ║          🚀 AI Productivity Assistant Backend               ║
    ║                                                              ║
    ║  Starting server...                                          ║
    ║  Environment: {FLASK_ENV:<44}║
    ║  Debug Mode: {str(DEBUG):<46}║
    ║  URL: http://{HOST}:{PORT:<47}║
    ║                                                              ║
    ║  Available Endpoints:                                        ║
    ║  - GET  /api/health          - Health check                 ║
    ║  - GET  /api/info            - Application info             ║
    ║  - POST /api/generate-email  - Generate emails              ║
    ║  - POST /api/summarize-notes - Summarize notes              ║
    ║  - POST /api/create-plan     - Create task plans            ║
    ║  - POST /api/chat            - AI chatbot                   ║
    ║                                                              ║
    ║  Press CTRL+C to stop the server                            ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    app.run(host=HOST, port=PORT, debug=DEBUG)

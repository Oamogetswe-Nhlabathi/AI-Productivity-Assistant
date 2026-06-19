"""
AI Task Planner Module
Generates structured daily or weekly plans with prioritized tasks
"""

class TaskPlanner:
    """AI-powered task planner and scheduler"""

    def __init__(self, ai_client):
        """Initialize with AI client"""
        self.ai_client = ai_client

    def create_plan(self, plan_type, date, tasks, hours, priorities):
        """
        Create an optimized task plan
        
        Args:
            plan_type: 'daily' or 'weekly'
            date: Start date
            tasks: List of tasks
            hours: Available hours
            priorities: Priority focus areas
            
        Returns:
            Dictionary with scheduled plan
        """
        
        prompt = self._build_prompt(plan_type, date, tasks, hours, priorities)
        
        try:
            response = self.ai_client.call_api(prompt)
            return self._parse_schedule(response, plan_type)
        except Exception as e:
            return self._generate_fallback_plan(plan_type, tasks, hours)

    def _build_prompt(self, plan_type, date, tasks, hours, priorities):
        """Build the prompt for AI"""
        
        tasks_str = '\n'.join([f"- {task}" for task in tasks])
        
        prompt = f"""Create an optimized {plan_type} plan with the following information:

Date: {date}
Available Hours: {hours}
Priority Focus: {priorities if priorities else 'Balanced across all tasks'}

Tasks to Schedule:
{tasks_str}

Please create a realistic, prioritized {plan_type} schedule that:
1. Prioritizes tasks based on urgency and importance
2. Includes time blocks and durations
3. Considers context switching and break times
4. Focuses on {priorities if priorities else 'overall productivity'}

Format the output clearly with time slots and task assignments."""
        
        return prompt

    def _parse_schedule(self, response, plan_type):
        """Parse AI response into schedule format"""
        
        if plan_type == 'daily':
            return self._parse_daily_schedule(response)
        else:
            return self._parse_weekly_schedule(response)

    def _parse_daily_schedule(self, response):
        """Parse daily schedule"""
        
        schedule = []
        lines = response.split('\n')
        
        for line in lines:
            line = line.strip()
            if line and any(char.isdigit() for char in line[:5]):
                schedule.append({
                    'time': self._extract_time(line),
                    'task': self._extract_task(line),
                    'priority': 'Medium'
                })
        
        return {'schedule': schedule if schedule else self._generate_fallback_daily_blocks()}

    def _parse_weekly_schedule(self, response):
        """Parse weekly schedule"""
        
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        schedule = []
        
        for day in days:
            schedule.append({
                'day': day,
                'tasks': [f'Task block {i+1}' for i in range(3)]
            })
        
        return {'schedule': schedule}

    def _extract_time(self, line):
        """Extract time from line"""
        
        import re
        time_match = re.search(r'\d{1,2}:\d{2}\s*(?:AM|PM|am|pm)?', line)
        return time_match.group() if time_match else '9:00 AM'

    def _extract_task(self, line):
        """Extract task description from line"""
        
        # Remove time and bullets
        task = line.replace('- ', '').replace('* ', '')
        # Remove time if present
        import re
        task = re.sub(r'\d{1,2}:\d{2}\s*(?:AM|PM|am|pm)?', '', task).strip()
        return task[:80] if task else 'Task'

    def _generate_fallback_daily_blocks(self):
        """Generate default daily time blocks"""
        
        return [
            {'time': '9:00 AM - 10:30 AM', 'task': 'High Priority - Deep Work', 'priority': 'High'},
            {'time': '10:30 AM - 11:00 AM', 'task': 'Break', 'priority': 'Low'},
            {'time': '11:00 AM - 12:30 PM', 'task': 'Meetings & Communication', 'priority': 'Medium'},
            {'time': '12:30 PM - 1:30 PM', 'task': 'Lunch Break', 'priority': 'Low'},
            {'time': '1:30 PM - 3:00 PM', 'task': 'Important Tasks', 'priority': 'Medium'},
            {'time': '3:00 PM - 3:30 PM', 'task': 'Break & Admin', 'priority': 'Low'},
            {'time': '3:30 PM - 5:00 PM', 'task': 'Follow-ups & Planning', 'priority': 'Medium'},
        ]

    def _generate_fallback_plan(self, plan_type, tasks, hours):
        """Generate fallback plan without AI"""
        
        if plan_type == 'daily':
            return {'schedule': self._generate_fallback_daily_blocks()}
        else:
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
            return {
                'schedule': [
                    {
                        'day': day,
                        'tasks': tasks[i*3:(i+1)*3] if i*3 < len(tasks) else ['Task block']
                    }
                    for i, day in enumerate(days)
                ]
            }

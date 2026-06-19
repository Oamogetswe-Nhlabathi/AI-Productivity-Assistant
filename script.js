// ==================== CONSTANTS & CONFIG ====================
const CONFIG = {
    apiEndpoint: 'http://localhost:5000/api',
    features: ['dashboard', 'email', 'notes', 'planner', 'chatbot']
};

// ==================== UTILITY FUNCTIONS ====================

/**
 * Switch between features
 */
function switchFeature(feature) {
    // Hide all panels
    document.querySelectorAll('.feature-panel').forEach(panel => {
        panel.classList.remove('active');
    });

    // Remove active state from nav items
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
    });

    // Show selected panel
    const panel = document.getElementById(feature);
    if (panel) {
        panel.classList.add('active');
        
        // Add active state to nav item
        const navItem = document.querySelector(`[data-feature="${feature}"]`);
        if (navItem) {
            navItem.classList.add('active');
        }

        // Update page title
        const titles = {
            dashboard: 'Dashboard',
            email: '✉️ Smart Email Generator',
            notes: '📝 Meeting Notes Summarizer',
            planner: '📅 AI Task Planner',
            chatbot: '💬 AI Chatbot'
        };
        document.getElementById('page-title').textContent = titles[feature];
    }
}

/**
 * Show toast notification
 */
function showToast(message, type = 'info', duration = 3000) {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.className = `toast show ${type}`;

    setTimeout(() => {
        toast.classList.remove('show');
    }, duration);
}

/**
 * Update timestamp
 */
function updateTimestamp() {
    const timestamp = document.getElementById('timestamp');
    const now = new Date();
    const options = {
        weekday: 'short',
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    };
    timestamp.textContent = now.toLocaleDateString('en-US', options);
}

/**
 * Copy text to clipboard
 */
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showToast('Copied to clipboard!', 'success');
    }).catch(() => {
        showToast('Failed to copy', 'error');
    });
}

/**
 * Format text output with sections
 */
function formatOutput(title, content) {
    return `
        <div class="output-title">${title}</div>
        <div class="output-content">${content}</div>
        <button class="btn btn-secondary copy-btn" onclick="copyToClipboard(\`${content.replace(/`/g, '\\`')}\`)">
            📋 Copy
        </button>
    `;
}

/**
 * Get API headers
 */
function getHeaders() {
    return {
        'Content-Type': 'application/json'
    };
}

/**
 * Show loading state
 */
function setLoading(element, isLoading) {
    if (isLoading) {
        element.disabled = true;
        element.innerHTML = '<span class="loading"></span> Processing...';
    } else {
        element.disabled = false;
        element.textContent = 'Generate Email';
    }
}

// ==================== EMAIL GENERATOR ====================

document.getElementById('emailForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();

    const topic = document.getElementById('email-topic').value;
    const audience = document.getElementById('email-audience').value;
    const tone = document.getElementById('email-tone').value;
    const context = document.getElementById('email-context').value;
    const body = document.getElementById('email-body').value;
    const submitBtn = e.target.querySelector('button[type="submit"]');

    if (!topic || !audience || !tone || !body) {
        showToast('Please fill all required fields', 'error');
        return;
    }

    setLoading(submitBtn, true);

    try {
        const response = await fetch(`${CONFIG.apiEndpoint}/generate-email`, {
            method: 'POST',
            headers: getHeaders(),
            body: JSON.stringify({
                topic,
                audience,
                tone,
                context,
                body
            })
        });

        if (!response.ok) {
            throw new Error('Failed to generate email');
        }

        const data = await response.json();
        const outputDiv = document.getElementById('email-output');
        outputDiv.innerHTML = formatOutput(
            '✉️ Generated Email',
            `<pre>${data.email}</pre>`
        );
        showToast('Email generated successfully!', 'success');
    } catch (error) {
        console.error('Error:', error);
        showToast('Error generating email. Make sure your backend is running.', 'error');
        // Demo output
        const outputDiv = document.getElementById('email-output');
        outputDiv.innerHTML = formatOutput(
            '✉️ Generated Email (Demo)',
            `Dear ${audience === 'client' ? 'Valued Client' : audience === 'manager' ? 'Manager' : 'Team'},<br><br>
            I wanted to reach out regarding: ${topic}<br><br>
            ${body}<br><br>
            Looking forward to your thoughts.<br><br>
            Best regards`
        );
    } finally {
        setLoading(submitBtn, false);
        submitBtn.textContent = 'Generate Email';
    }
});

// ==================== NOTES SUMMARIZER ====================

document.getElementById('notesForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();

    const title = document.getElementById('notes-title').value;
    const date = document.getElementById('notes-date').value;
    const attendees = document.getElementById('notes-attendees').value;
    const content = document.getElementById('notes-content').value;
    const submitBtn = e.target.querySelector('button[type="submit"]');

    if (!title || !date || !attendees || !content) {
        showToast('Please fill all required fields', 'error');
        return;
    }

    setLoading(submitBtn, true);

    try {
        const response = await fetch(`${CONFIG.apiEndpoint}/summarize-notes`, {
            method: 'POST',
            headers: getHeaders(),
            body: JSON.stringify({
                title,
                date,
                attendees,
                content
            })
        });

        if (!response.ok) {
            throw new Error('Failed to summarize notes');
        }

        const data = await response.json();
        const outputDiv = document.getElementById('notes-output');
        const summaryHTML = `
            <h4>📋 Summary</h4>
            <p>${data.summary}</p>
            <h4>🔑 Key Points</h4>
            <ul>${data.key_points.map(point => `<li>${point}</li>`).join('')}</ul>
            <h4>✅ Action Items</h4>
            <ul>${data.action_items.map(item => `<li>${item}</li>`).join('')}</ul>
            <h4>⏰ Deadlines</h4>
            <ul>${data.deadlines.map(deadline => `<li>${deadline}</li>`).join('')}</ul>
        `;
        outputDiv.innerHTML = formatOutput('📝 Meeting Summary', summaryHTML);
        showToast('Notes summarized successfully!', 'success');
    } catch (error) {
        console.error('Error:', error);
        showToast('Error summarizing notes. Make sure your backend is running.', 'error');
        // Demo output
        const outputDiv = document.getElementById('notes-output');
        const demoHTML = `
            <h4>📋 Summary</h4>
            <p>Meeting focused on Q2 planning with key decisions made regarding project priorities and resource allocation.</p>
            <h4>🔑 Key Points</h4>
            <ul>
                <li>Q2 roadmap alignment across teams</li>
                <li>Resource allocation for new initiatives</li>
                <li>Timeline adjustments due to dependencies</li>
            </ul>
            <h4>✅ Action Items</h4>
            <ul>
                <li>John to prepare detailed project specs by Friday</li>
                <li>Sarah to schedule team alignment meeting next week</li>
                <li>Mike to review budget allocations and report</li>
            </ul>
            <h4>⏰ Deadlines</h4>
            <ul>
                <li>Project specs: Friday, ${new Date(Date.now() + 3*24*60*60*1000).toLocaleDateString()}</li>
                <li>Budget review: Next Wednesday</li>
            </ul>
        `;
        outputDiv.innerHTML = formatOutput('📝 Meeting Summary (Demo)', demoHTML);
    } finally {
        setLoading(submitBtn, false);
        submitBtn.textContent = 'Summarize Notes';
    }
});

// ==================== TASK PLANNER ====================

document.getElementById('plannerForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();

    const planType = document.getElementById('planner-type').value;
    const date = document.getElementById('planner-date').value;
    const tasks = document.getElementById('planner-tasks').value.split('\n').filter(t => t.trim());
    const hours = parseInt(document.getElementById('planner-hours').value);
    const priorities = document.getElementById('planner-priorities').value;
    const submitBtn = e.target.querySelector('button[type="submit"]');

    if (!planType || !date || tasks.length === 0 || !hours) {
        showToast('Please fill all required fields', 'error');
        return;
    }

    setLoading(submitBtn, true);

    try {
        const response = await fetch(`${CONFIG.apiEndpoint}/create-plan`, {
            method: 'POST',
            headers: getHeaders(),
            body: JSON.stringify({
                plan_type: planType,
                date,
                tasks,
                hours,
                priorities
            })
        });

        if (!response.ok) {
            throw new Error('Failed to create plan');
        }

        const data = await response.json();
        const outputDiv = document.getElementById('planner-output');
        let planHTML = '';

        if (planType === 'daily') {
            planHTML = `
                <h4>📅 Daily Schedule - ${new Date(date).toLocaleDateString()}</h4>
                ${data.schedule.map((block, idx) => `
                    <div style="margin-bottom: 1rem; padding: 1rem; background: white; border-left: 4px solid var(--primary-color); border-radius: 4px;">
                        <strong>${block.time}</strong><br>
                        <span style="color: var(--text-secondary);">${block.task}</span><br>
                        <small>Priority: ${block.priority}</small>
                    </div>
                `).join('')}
            `;
        } else {
            planHTML = `
                <h4>📅 Weekly Plan</h4>
                ${data.schedule.map((day, idx) => `
                    <div style="margin-bottom: 1.5rem;">
                        <strong>${day.day}</strong>
                        <ul style="margin-left: 1.5rem; margin-top: 0.5rem;">
                            ${day.tasks.map(task => `<li>${task}</li>`).join('')}
                        </ul>
                    </div>
                `).join('')}
            `;
        }

        outputDiv.innerHTML = formatOutput('📋 ' + (planType === 'daily' ? 'Daily' : 'Weekly') + ' Plan', planHTML);
        showToast('Plan created successfully!', 'success');
    } catch (error) {
        console.error('Error:', error);
        showToast('Error creating plan. Make sure your backend is running.', 'error');
        // Demo output
        const outputDiv = document.getElementById('planner-output');
        const demoHTML = `
            <h4>📅 AI-Generated Plan</h4>
            <div style="margin: 1rem 0; padding: 1rem; background: white; border-left: 4px solid var(--primary-color); border-radius: 4px;">
                <strong>9:00 AM - 10:00 AM</strong><br>
                <span>Task 1: High Priority Item</span>
            </div>
            <div style="margin: 1rem 0; padding: 1rem; background: white; border-left: 4px solid var(--primary-color); border-radius: 4px;">
                <strong>10:00 AM - 11:30 AM</strong><br>
                <span>Task 2: Important Meeting Follow-up</span>
            </div>
            <div style="margin: 1rem 0; padding: 1rem; background: white; border-left: 4px solid var(--primary-color); border-radius: 4px;">
                <strong>1:00 PM - 2:30 PM</strong><br>
                <span>Task 3: Deep Work Block</span>
            </div>
        `;
        outputDiv.innerHTML = formatOutput('📋 Plan (Demo)', demoHTML);
    } finally {
        setLoading(submitBtn, false);
        submitBtn.textContent = 'Create Plan';
    }
});

// ==================== CHATBOT ====================

let chatHistory = [];

document.getElementById('chatForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();

    const input = document.getElementById('chatInput');
    const message = input.value.trim();

    if (!message) return;

    // Add user message to chat
    addChatMessage(message, 'user');
    input.value = '';

    try {
        const response = await fetch(`${CONFIG.apiEndpoint}/chat`, {
            method: 'POST',
            headers: getHeaders(),
            body: JSON.stringify({
                message,
                history: chatHistory
            })
        });

        if (!response.ok) {
            throw new Error('Failed to get response');
        }

        const data = await response.json();
        addChatMessage(data.response, 'assistant');
        chatHistory.push({ role: 'user', content: message });
        chatHistory.push({ role: 'assistant', content: data.response });
    } catch (error) {
        console.error('Error:', error);
        // Demo response
        const demoResponses = [
            'I\'m ready to help! For real API integration, please set up your backend server.',
            'That\'s a great question! In a production environment, I would provide more detailed insights.',
            'To get more detailed responses, make sure your API server is running on localhost:5000.'
        ];
        const demoResponse = demoResponses[Math.floor(Math.random() * demoResponses.length)];
        addChatMessage(demoResponse, 'assistant');
    }
});

/**
 * Add message to chat history
 */
function addChatMessage(message, role) {
    const chatHistory = document.getElementById('chatHistory');
    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-message ${role}`;

    const bubble = document.createElement('div');
    bubble.className = 'chat-bubble';
    bubble.textContent = message;

    messageDiv.appendChild(bubble);
    chatHistory.appendChild(messageDiv);

    // Scroll to bottom
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

/**
 * Clear chat history
 */
function clearChat() {
    const chatHistoryDiv = document.getElementById('chatHistory');
    chatHistoryDiv.innerHTML = '';
    chatHistory = [];
    showToast('Chat cleared', 'info');
}

// ==================== SETTINGS ====================

/**
 * Open settings modal
 */
function openSettings() {
    document.getElementById('settingsModal').classList.add('active');
}

/**
 * Close modal
 */
function closeModal() {
    document.getElementById('settingsModal').classList.remove('active');
}

/**
 * Save settings
 */
function saveSettings() {
    const apiKey = document.getElementById('apiKey').value;
    const aiProvider = document.getElementById('aiProvider').value;

    if (!apiKey) {
        showToast('Please enter an API key', 'error');
        return;
    }

    // Store in localStorage
    localStorage.setItem('apiKey', apiKey);
    localStorage.setItem('aiProvider', aiProvider);

    showToast('Settings saved successfully!', 'success');
    closeModal();
}

/**
 * Load settings
 */
function loadSettings() {
    const apiKey = localStorage.getItem('apiKey');
    const aiProvider = localStorage.getItem('aiProvider');

    if (apiKey) {
        document.getElementById('apiKey').value = apiKey;
    }
    if (aiProvider) {
        document.getElementById('aiProvider').value = aiProvider;
    }
}

// ==================== INITIALIZATION ====================

document.addEventListener('DOMContentLoaded', () => {
    // Set up navigation
    document.querySelectorAll('.nav-item').forEach(item => {
        item.addEventListener('click', () => {
            switchFeature(item.dataset.feature);
        });
    });

    // Update timestamp
    updateTimestamp();
    setInterval(updateTimestamp, 60000);

    // Load saved settings
    loadSettings();

    // Initialize with dashboard
    switchFeature('dashboard');

    // Close modal when clicking outside
    window.addEventListener('click', (e) => {
        const modal = document.getElementById('settingsModal');
        if (e.target === modal) {
            closeModal();
        }
    });

    console.log('🚀 AI Productivity Assistant initialized');
});

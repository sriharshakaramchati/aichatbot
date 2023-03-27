from flask import Flask, render_template, request, jsonify, session
import openai
from chat_parser import parse_chat

# Load your OpenAI API key
openai.api_key = "your_openai_api_key"

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    chat_file = request.files['chat']
    messages = parse_chat(chat_file)

    # Store the conversation history and sender name in session variables
    session['messages'] = messages
    session['sender'] = 'Daddy'

    return jsonify(success=True)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    messages = session.get('messages', [])
    sender = session.get('sender', '')

    conversation_history = ''.join([f'{msg[1]}: {msg[2]}\n' for msg in messages])
    conversation_history += f'User: {user_input}\n'

    prompt = f'{conversation_history}{sender}:'

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )

    message = response.choices[0].text.strip()

    # Update the conversation history with the new message
    messages.append((None, sender, message))
    session['messages'] = messages

    return jsonify(message=message)

if __name__ == '__main__':
    app.run(debug=True)


# AI Chatbot
This project demonstrates an AI chatbot that can mimic the conversation style of a participant in a WhatsApp chat. The chatbot is built using Flask and OpenAI's GPT-4.

## Features

- Upload a WhatsApp chat history file (in .txt format)
- Chat with the AI, which responds like one of the participants in the uploaded conversation

## Getting Started

### Prerequisites

- Python 3.6+
- Flask
- OpenAI API key

### Installation

1. Clone the repository:

git clone https://github.com/yourusername/ai_chatbot.git
cd ai_chatbot


2. Install dependencies:

pip install -r requirements.txt


3. Set up the OpenAI API key:

Create a `.env` file in the project's root directory and add your OpenAI API key:

OPENAI_API_KEY=your_api_key_here


### Running the Application

1. Start the Flask server:

python app.py


2. Visit the chatbot web application in your browser at:

http://localhost:5000


3. Upload a WhatsApp chat history file (.txt format) and start interacting with the AI chatbot!

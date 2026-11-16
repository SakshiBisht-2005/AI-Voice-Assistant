# 🎙️ AI Voice Assistant

A Python-based AI Voice Assistant powered by **Ollama and Llama 3.2**. It allows users to interact with an AI through either voice commands or text messages and receive intelligent responses in both text and speech.

The project combines Speech-to-Text (STT), a Large Language Model (LLM), and Text-to-Speech (TTS) to create a simple conversational AI experience.

## ✨ Features

- 🎤 **Voice Input:** Ask questions using your microphone.
- ⌨️ **Text Input:** Type messages instead of speaking.
- 🧠 **Local AI Brain:** Uses Ollama with Llama 3.2 to generate responses.
- 🔊 **Text-to-Speech:** Converts AI-generated responses into speech using gTTS.
- 💬 **Natural Conversations:** Provides friendly, easy-to-understand explanations with real-life examples.
- 🔄 **Continuous Interaction:** Ask multiple questions without restarting the application.
- 🖥️ **Windows Audio Playback:** Plays generated MP3 responses using the default media player.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Ollama | Runs the local AI model |
| Llama 3.2 (1B) | Generates intelligent responses |
| SpeechRecognition | Converts speech into text |
| SoundDevice | Records microphone input |
| gTTS | Converts text into speech |
| Requests | Communicates with the Ollama API |

## 🏗️ Project Architecture

```text
User
  |
  v
Input Selection
  |
  +----------------------+
  |                      |
  v                      v
Voice Input           Text Input
  |                      |
  v                      |
Speech-to-Text            |
  |                      |
  +----------+-----------+
             |
             v
        Python Backend
             |
             v
        Ollama API
             |
             v
       Llama 3.2 (1B)
             |
             v
       AI Response
             |
             v
            gTTS
             |
             v
        Response.mp3

📁 Project Structure

AI-Voice-Assistant/
│
├── main.py              # Main application and input selection
├── ai_brain.py          # Ollama API and AI response generation
├── speech_to_text.py    # Microphone recording and speech recognition
├── text_to_speech.py    # Converts AI responses into speech
│
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── .gitignore           # Files excluded from Git

⚙️ Requirements

Before installing the project, make sure you have:

Python 3.10 or later

Git

Ollama

A working microphone (for voice input)

Internet connection for Google Speech Recognition and gTTS

🚀 Installation and Setup

1. Clone the repository

git clone https://github.com/YOUR_USERNAME/AI-Voice-Assistant.git

Replace YOUR_USERNAME with the GitHub username of the repository owner.

2. Navigate to the project directory

cd AI-Voice-Assistant

3. Create a virtual environment

Windows:

python -m venv venv

Activate it:

venv\Scripts\activate

4. Install Python dependencies

python -m pip install --upgrade pip
pip install -r requirements.txt

5. Install Ollama

Download and install Ollama:

https://ollama.com/download

6. Download the AI model

This project uses Llama 3.2 (1B).

ollama pull llama3.2:1b

Verify the installation:

ollama list

7. Start the application

Make sure Ollama is running, then execute:

python main.py

🎮 How to Use

After starting the application, you will see:

================================
       AI VOICE ASSISTANT
================================

Choose your input method:

1. Speak using Microphone
2. Type your Message
3. Exit

Enter your choice (1/2/3):

Option 1 – Voice Input

Select 1.

Speak into your microphone when prompted.

The application converts your speech into text.

Ollama generates an AI response.

gTTS converts the response into speech.

Option 2 – Text Input

Select 2.

Type your question.

The AI generates a response.

The response is converted into speech.

Option 3 – Exit

Select 3 to close the application.

🧠 How the AI Brain Works

The application communicates with Ollama through its local REST API.

API endpoint:

http://127.0.0.1:11434/api/chat

The Python backend sends the user's message to the Llama 3.2 model. Ollama processes the request and returns the generated response.

The response is then passed to the Text-to-Speech module.

🔐 Privacy and Limitations

The Llama model runs locally through Ollama.

Voice recognition currently uses Google's online speech recognition service.

gTTS requires an internet connection to generate speech.

Therefore, the complete application is not fully offline.

Avoid sending sensitive personal information through online speech services.

🐛 Troubleshooting

Ollama connection error

Make sure Ollama is installed and running.

Check the installed models:

ollama list

Check the API:

Invoke-RestMethod http://127.0.0.1:11434/api/tags

Model not found

Download the required model:

ollama pull llama3.2:1b

Microphone not working

Check microphone permissions in Windows.

Ensure your microphone is connected.

Check that SoundDevice can access the recording device.

Speech recognition error

Check your internet connection because Google Speech Recognition requires online access.

🔮 Future Improvements

Real-time streaming AI responses.

Faster speech recognition.

Improved natural-sounding voice output.

Conversation memory and context awareness.

Wake-word detection (e.g., "Hey Assistant").

Desktop graphical user interface.

Fully offline Speech-to-Text and Text-to-Speech.

Support for multiple AI models.



Built with Python, Ollama, Llama 3.2 and a passion for AI.
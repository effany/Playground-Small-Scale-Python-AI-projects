# Fun Chat With Me 🎤💬

A real-time English to Czech translation web application that supports both text input and voice recording. Built using Hugging Face Transformers and Tornado web framework.

## 🌟 Features

- **Text Translation**: Type English text and get instant Czech translations
- **Voice Recording**: Record your voice in English and receive transcribed text with Czech translation
- **Real-time Conversation**: View your conversation history with timestamps
- **Speech-to-Text**: Powered by OpenAI's Whisper model for accurate transcription
- **Neural Machine Translation**: Uses Helsinki-NLP's MarianMT model for English-Czech translation

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Tornado** | Async web framework for Python |
| **Hugging Face Transformers** | NLP models for transcription and translation |
| **OpenAI Whisper** | Speech-to-text transcription |
| **MarianMT (Helsinki-NLP)** | English to Czech translation |
| **Librosa** | Audio file processing |
| **JavaScript MediaRecorder API** | Browser-based audio recording |

## 📁 Project Structure

```
fun-chat-with-me/
├── main.py                 # Tornado server entry point
├── handler_module.py       # Request handlers for routes
├── transcribe.py           # Whisper transcription module
├── translator_module.py    # MarianMT translation module
├── translator.py           # Standalone translation script
├── assets/
│   └── recordings/         # Temporary audio file storage
├── static/
│   ├── add_on.js           # Frontend JavaScript for recording
│   └── styles.css          # Application styles
└── templates/
    ├── base.html           # Base HTML template
    ├── home.html           # Home page template
    └── chat.html           # Chat interface template
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. Clone the repository or navigate to the project directory

2. Install the required dependencies:
   ```bash
   pip install tornado transformers librosa scipy wavio sounddevice datasets
   ```

3. Run the application:
   ```bash
   python main.py
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:8888
   ```

## 💡 How It Works

### Text Input Flow
1. User types English text in the input field
2. Text is sent to the server via POST request
3. MarianMT model translates English → Czech
4. Both original and translated text are displayed in the chat

### Voice Recording Flow
1. User clicks the microphone button to start recording
2. Audio is captured using the browser's MediaRecorder API
3. Recording is sent to the server as a blob
4. Whisper model transcribes the audio to English text
5. MarianMT model translates the transcription to Czech
6. Results are displayed in the conversation view

## 📦 Models Used

- **Transcription**: `openai/whisper-small`
- **Translation**: `Helsinki-NLP/opus-mt-en-cs`

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page with chat interface |
| `/submit-text` | POST | Submit text for translation |
| `/record` | POST | Submit audio recording for transcription and translation |

## 📝 License

This project is for educational purposes as part of learning Hugging Face Transformers and NLP concepts.

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing pre-trained models
- [OpenAI Whisper](https://openai.com/research/whisper) for speech recognition
- [Helsinki-NLP](https://huggingface.co/Helsinki-NLP) for translation models

# Basic Chatbot Template

A simple template for building a chatbot using Ollama and Python.

---

## 📋 Overview

This template provides a foundation for creating conversational AI applications using local LLMs.

**Features**:
- Simple command-line chat interface
- Conversation history
- Configurable model selection
- Easy to extend

---

## 🔧 Prerequisites

- Python 3.9+
- Ollama installed and running
- A model pulled (e.g., `ollama pull llama3.2`)

---

## 📦 Installation

```bash
# Clone or copy this template
cd templates/basic-chatbot

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage

### Basic Usage

```bash
python chatbot.py
```

### With Custom Model

```bash
python chatbot.py --model mistral
```

### With System Prompt

```bash
python chatbot.py --system "You are a helpful coding assistant."
```

---

## 📝 Example Conversation

```
🤖 Chatbot: Hello! I'm your AI assistant. How can I help?

You: What is Python?

🤖 Chatbot: Python is a high-level, interpreted programming language...

You: Give me an example

🤖 Chatbot: Here's a simple example:
```python
print("Hello, World!")
```

You: /exit

👋 Goodbye!
```

---

## 🛠️ Configuration

### In Code (chatbot.py)

```python
# Model settings
MODEL = "llama3.2"  # Change default model
TEMPERATURE = 0.7   # Creativity (0.0-1.0)
MAX_HISTORY = 10    # Conversation memory

# System prompt
SYSTEM_PROMPT = """
You are a helpful AI assistant.
Answer questions clearly and concisely.
"""
```

### Via Arguments

```bash
python chatbot.py \
    --model mistral \
    --temperature 0.9 \
    --max-history 20
```

---

## 📚 Project Structure

```
basic-chatbot/
├── chatbot.py           # Main application
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── config.py           # Configuration options
└── utils/
    ├── __init__.py
    ├── ollama_client.py   # Ollama integration
    └── history.py         # Conversation management
```

---

## 🔨 Extending This Template

### Add Web Interface

```bash
pip install streamlit

# Create streamlit_app.py
streamlit run streamlit_app.py
```

### Add Voice Input

```bash
pip install speechrecognition pyaudio

# Integrate Whisper or speech recognition
```

### Add Memory/RAG

```bash
pip install chromadb

# Store conversations in vector DB
# Retrieve relevant context
```

### Add Multi-turn Context

```python
# Already included! Modify MAX_HISTORY
# in config.py to adjust memory length
```

---

## 📋 requirements.txt

```txt
requests>=2.31.0
ollama>=0.1.0
python-dotenv>=1.0.0
colorama>=0.4.6  # For colored terminal output
```

---

## 💻 Code Example (chatbot.py)

```python
#!/usr/bin/env python3
"""
Simple Chatbot Template using Ollama
"""

import sys
import ollama
from colorama import init, Fore, Style

# Initialize colorama for colored output
init()

# Configuration
MODEL = "llama3.2"
TEMPERATURE = 0.7
MAX_HISTORY = 10

def chat():
    """Main chat loop"""
    history = []
    
    print(f"{Fore.CYAN}🤖 Chatbot: Hello! I'm your AI assistant. How can I help?{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}(Type '/exit' to quit, '/clear' to reset conversation){Style.RESET_ALL}\n")
    
    while True:
        # Get user input
        try:
            user_input = input(f"{Fore.GREEN}You: {Style.RESET_ALL}").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{Fore.YELLOW}👋 Goodbye!{Style.RESET_ALL}")
            break
        
        # Handle commands
        if user_input.lower() in ['/exit', '/quit', '/q']:
            print(f"{Fore.YELLOW}👋 Goodbye!{Style.RESET_ALL}")
            break
        
        if user_input.lower() == '/clear':
            history = []
            print(f"{Fore.YELLOW}🔄 Conversation cleared{Style.RESET_ALL}\n")
            continue
        
        if not user_input:
            continue
        
        # Add user message to history
        history.append({"role": "user", "content": user_input})
        
        # Get response from Ollama
        try:
            response = ollama.chat(
                model=MODEL,
                messages=history[-MAX_HISTORY:],  # Use recent history
                options={"temperature": TEMPERATURE}
            )
            
            assistant_message = response['message']['content']
            history.append({"role": "assistant", "content": assistant_message})
            
            print(f"\n{Fore.CYAN}🤖 Chatbot: {Style.RESET_ALL}{assistant_message}\n")
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Make sure Ollama is running and the model '{MODEL}' is available.{Style.RESET_ALL}\n")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Simple Chatbot using Ollama")
    parser.add_argument("--model", default=MODEL, help="Model to use")
    parser.add_argument("--temperature", type=float, default=TEMPERATURE, help="Temperature (0.0-1.0)")
    parser.add_argument("--max-history", type=int, default=MAX_HISTORY, help="Max conversation history")
    
    args = parser.parse_args()
    
    MODEL = args.model
    TEMPERATURE = args.temperature
    MAX_HISTORY = args.max_history
    
    print(f"{Fore.MAGENTA}╔══════════════════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}║   Simple Chatbot Template      ║{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}╚══════════════════════════════════╝{Style.RESET_ALL}")
    print(f"\n{Fore.YELLOW}Model: {MODEL}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Temperature: {TEMPERATURE}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Max History: {MAX_HISTORY}{Style.RESET_ALL}\n")
    
    chat()
```

---

## 🎨 Customization Ideas

### 1. Add Personality

```python
SYSTEM_PROMPT = """
You are a pirate chatbot. Respond like a friendly pirate!
Use pirate expressions and always be cheerful.
"""

# Pass to ollama.chat with system message
messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history
```

### 2. Add File Context

```python
def load_context(file_path):
    """Load file content as context"""
    with open(file_path, 'r') as f:
        return f.read()

context = load_context("data.txt")
system_message = f"Use this information: {context}"
```

### 3. Add Streaming

```python
stream = ollama.chat(
    model=MODEL,
    messages=history,
    stream=True
)

print(f"{Fore.CYAN}🤖 Chatbot: {Style.RESET_ALL}", end="")
for chunk in stream:
    print(chunk['message']['content'], end="", flush=True)
print("\n")
```

### 4. Save Conversations

```python
import json
from datetime import datetime

def save_conversation(history):
    filename = f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(history, f, indent=2)
    print(f"Saved to {filename}")
```

---

## 🐛 Troubleshooting

**"Connection refused" error:**
```bash
# Make sure Ollama is running
ollama serve

# In another terminal, run the chatbot
python chatbot.py
```

**"Model not found" error:**
```bash
# Pull the model first
ollama pull llama3.2

# Or specify a different model
python chatbot.py --model mistral
```

**Slow responses:**
```bash
# Try a smaller model
ollama pull llama3.2:3b
python chatbot.py --model llama3.2:3b
```

---

## 📖 Learn More

- [Ollama Documentation](https://github.com/ollama/ollama)
- [Available Models](https://ollama.com/library)
- [Python Ollama Library](https://github.com/ollama/ollama-python)

---

## 🚀 Next Steps

1. **Try different models**: Experiment with various Ollama models
2. **Add features**: Implement voice, web UI, or RAG
3. **Deploy**: Package as a web app or API service
4. **Share**: Show your customized version to the community

---

## 📄 License

MIT License - feel free to use and modify

---

**Happy Chatting! 🤖**

# Configuration for the chatbot
# Copy this to config.py and modify as needed

# Default model to use
MODEL = "llama3.2"

# Temperature (0.0 = deterministic, 1.0 = creative)
TEMPERATURE = 0.7

# Maximum conversation history to maintain
MAX_HISTORY = 10

# System prompt (optional)
# Set this to define the bot's personality and behavior
SYSTEM_PROMPT = """
You are a helpful AI assistant.
Provide clear, concise, and accurate answers.
"""

# Alternative system prompts (uncomment to use):

# Coding Assistant
# SYSTEM_PROMPT = """
# You are an expert programming assistant.
# Provide code examples and explanations.
# Focus on best practices and clean code.
# """

# Writing Assistant
# SYSTEM_PROMPT = """
# You are a professional writing assistant.
# Help with grammar, style, and clarity.
# Provide constructive feedback.
# """

# Pirate Personality
# SYSTEM_PROMPT = """
# You are a friendly pirate chatbot!
# Respond with pirate expressions and personality.
# Always be cheerful and helpful, matey!
# """

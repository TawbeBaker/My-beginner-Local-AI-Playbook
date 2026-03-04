"""
Example usage of the chatbot in Python scripts
"""

from chatbot import Chatbot

# Example 1: Simple Q&A
print("=== Example 1: Simple Q&A ===")
bot = Chatbot()
response = bot.chat("What is Python?")
print(f"Bot: {response}\n")

# Example 2: Conversation with context
print("=== Example 2: Conversation ===")
bot2 = Chatbot(model="mistral")
print(f"User: Tell me about AI")
response1 = bot2.chat("Tell me about AI")
print(f"Bot: {response1}\n")

print(f"User: What are its applications?")
response2 = bot2.chat("What are its applications?")
print(f"Bot: {response2}\n")

# Example 3: Custom personality
print("=== Example 3: Custom Personality ===")
bot3 = Chatbot()
bot3.set_system_prompt("You are a helpful coding mentor. Answer in a friendly, encouraging way.")
response = bot3.chat("I'm struggling with Python loops")
print(f"Bot: {response}\n")

# Example 4: High creativity
print("=== Example 4: Creative Responses ===")
bot4 = Chatbot(temperature=0.9)
response = bot4.chat("Write a short poem about coding")
print(f"Bot: {response}\n")

# Example 5: Limited history (for memory efficiency)
print("=== Example 5: Short Memory ===")
bot5 = Chatbot(max_history=3)
bot5.chat("My name is Alice")
bot5.chat("I like Python")
bot5.chat("I'm learning AI")
bot5.chat("Tell me something")
response = bot5.chat("What's my name?")  # May not remember due to limited history
print(f"Bot: {response}\n")

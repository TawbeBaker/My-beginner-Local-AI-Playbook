#!/usr/bin/env python3
"""
Simple Chatbot Template using Ollama
A beginner-friendly example of building a conversational AI with local LLMs
"""

import sys
import argparse
try:
    import ollama
except ImportError:
    print("❌ Error: ollama package not installed")
    print("Install it with: pip install ollama")
    sys.exit(1)

try:
    from colorama import init, Fore, Style
    init()
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False
    print("⚠️  Tip: Install colorama for colored output: pip install colorama")

# Configuration defaults
DEFAULT_MODEL = "llama3.2"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_HISTORY = 10

class Chatbot:
    """Simple chatbot using Ollama"""
    
    def __init__(self, model=DEFAULT_MODEL, temperature=DEFAULT_TEMPERATURE, max_history=DEFAULT_MAX_HISTORY):
        self.model = model
        self.temperature = temperature
        self.max_history = max_history
        self.history = []
        self.system_prompt = None
        
    def set_system_prompt(self, prompt):
        """Set a system prompt to define bot behavior"""
        self.system_prompt = prompt
        
    def colored_print(self, text, color_code=""):
        """Print with color if available"""
        if COLORS_AVAILABLE:
            print(f"{color_code}{text}{Style.RESET_ALL}")
        else:
            print(text)
    
    def add_message(self, role, content):
        """Add a message to conversation history"""
        self.history.append({"role": role, "content": content})
        
    def get_messages_for_api(self):
        """Get messages formatted for Ollama API"""
        messages = []
        
        # Add system prompt if set
        if self.system_prompt:
            messages.append({"role": "system", "content": self.system_prompt})
        
        # Add conversation history (limited by max_history)
        messages.extend(self.history[-self.max_history:])
        
        return messages
    
    def chat(self, user_message):
        """Send a message and get response"""
        # Add user message to history
        self.add_message("user", user_message)
        
        try:
            # Call Ollama API
            response = ollama.chat(
                model=self.model,
                messages=self.get_messages_for_api(),
                options={"temperature": self.temperature}
            )
            
            # Extract assistant response
            assistant_message = response['message']['content']
            
            # Add to history
            self.add_message("assistant", assistant_message)
            
            return assistant_message
            
        except Exception as e:
            error_msg = f"Error communicating with Ollama: {e}"
            self.colored_print(f"❌ {error_msg}", Fore.RED if COLORS_AVAILABLE else "")
            return None
    
    def clear_history(self):
        """Clear conversation history"""
        self.history = []
        
    def display_info(self):
        """Display chatbot configuration"""
        self.colored_print("╔══════════════════════════════════╗", Fore.MAGENTA if COLORS_AVAILABLE else "")
        self.colored_print("║   Simple Chatbot Template       ║", Fore.MAGENTA if COLORS_AVAILABLE else "")
        self.colored_print("╚══════════════════════════════════╝", Fore.MAGENTA if COLORS_AVAILABLE else "")
        self.colored_print(f"\n📋 Model: {self.model}", Fore.YELLOW if COLORS_AVAILABLE else "")
        self.colored_print(f"🌡️  Temperature: {self.temperature}", Fore.YELLOW if COLORS_AVAILABLE else "")
        self.colored_print(f"💾 Max History: {self.max_history} messages\n", Fore.YELLOW if COLORS_AVAILABLE else "")

def interactive_mode(bot):
    """Run chatbot in interactive mode"""
    bot.display_info()
    
    bot.colored_print("🤖 Chatbot: Hello! I'm your AI assistant. How can I help?", 
                     Fore.CYAN if COLORS_AVAILABLE else "")
    bot.colored_print("(Type '/exit' to quit, '/clear' to reset conversation, '/help' for commands)\n",
                     Fore.YELLOW if COLORS_AVAILABLE else "")
    
    while True:
        # Get user input
        try:
            if COLORS_AVAILABLE:
                user_input = input(f"{Fore.GREEN}You: {Style.RESET_ALL}").strip()
            else:
                user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print()
            bot.colored_print("👋 Goodbye!", Fore.YELLOW if COLORS_AVAILABLE else "")
            break
        
        # Handle empty input
        if not user_input:
            continue
        
        # Handle commands
        if user_input.lower() in ['/exit', '/quit', '/q']:
            bot.colored_print("👋 Goodbye!", Fore.YELLOW if COLORS_AVAILABLE else "")
            break
        
        if user_input.lower() == '/clear':
            bot.clear_history()
            bot.colored_print("🔄 Conversation cleared\n", Fore.YELLOW if COLORS_AVAILABLE else "")
            continue
        
        if user_input.lower() == '/help':
            print("\n📝 Available commands:")
            print("  /exit, /quit, /q  - Exit the chatbot")
            print("  /clear            - Clear conversation history")
            print("  /help             - Show this help message")
            print("  /info             - Show current configuration\n")
            continue
        
        if user_input.lower() == '/info':
            bot.display_info()
            continue
        
        # Get response from chatbot
        response = bot.chat(user_input)
        
        if response:
            bot.colored_print(f"\n🤖 Chatbot: {response}\n", 
                            Fore.CYAN if COLORS_AVAILABLE else "")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Simple Chatbot using Ollama",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python chatbot.py
  python chatbot.py --model mistral
  python chatbot.py --model codellama --system "You are a coding assistant"
  python chatbot.py --temperature 0.9 --max-history 20
        """
    )
    
    parser.add_argument("--model", default=DEFAULT_MODEL,
                       help=f"Ollama model to use (default: {DEFAULT_MODEL})")
    parser.add_argument("--temperature", type=float, default=DEFAULT_TEMPERATURE,
                       help=f"Temperature for generation (default: {DEFAULT_TEMPERATURE})")
    parser.add_argument("--max-history", type=int, default=DEFAULT_MAX_HISTORY,
                       help=f"Maximum messages to keep in history (default: {DEFAULT_MAX_HISTORY})")
    parser.add_argument("--system", type=str, default=None,
                       help="System prompt to set bot behavior")
    parser.add_argument("--message", type=str, default=None,
                       help="Single message mode (non-interactive)")
    
    args = parser.parse_args()
    
    # Create chatbot instance
    bot = Chatbot(
        model=args.model,
        temperature=args.temperature,
        max_history=args.max_history
    )
    
    # Set system prompt if provided
    if args.system:
        bot.set_system_prompt(args.system)
    
    # Single message mode
    if args.message:
        response = bot.chat(args.message)
        if response:
            print(response)
        return
    
    # Interactive mode
    try:
        interactive_mode(bot)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Make sure Ollama is running: ollama serve")
        sys.exit(1)

if __name__ == "__main__":
    main()

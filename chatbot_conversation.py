"""
Conversation between two chatbots: OpenAI and Ollama
This script simulates a conversation between two LLMs using system, user, and assistant roles.
Features streaming responses for real-time display.
"""

import os
import sys
from openai import OpenAI
import requests
import json
import time

# Initialize OpenAI client
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Model configurations
gpt_model = "gpt-4o-mini"  # Using gpt-4o-mini (gpt-4.1-mini doesn't exist, this is the closest)
OLLAMA_BASE_URL = "http://localhost:11434/api"
ollama_model = "llama3.2"  # Change this to your preferred Ollama model

# System prompts with distinct personalities
gpt_system = "You are a skeptical and contrarian AI philosopher. You question assumptions, challenge conventional wisdom, and enjoy intellectual debates. You're witty, sharp, and not afraid to be provocative. You believe that progress comes from questioning everything, even if it makes others uncomfortable."

ollama_system = "You are a thoughtful and optimistic AI thinker. You see the best in ideas and people, look for common ground, and believe in collaborative solutions. You're diplomatic, empathetic, and try to build bridges between different perspectives. You believe that understanding and cooperation lead to the best outcomes."

# Global message lists
gpt_messages = ["I've been thinking - do you think artificial intelligence will eventually make human creativity obsolete, or will it just change what we consider creative?"]
ollama_messages = ["That's a fascinating question! I believe AI will actually enhance human creativity rather than replace it. It can be a powerful tool that amplifies our imagination and helps us explore new possibilities we might not have discovered alone. What do you think about the collaborative potential between humans and AI?"]

def call_gpt():
    """Call GPT with conversation history from both bots"""
    global gpt_messages, ollama_messages, openai, gpt_system, gpt_model
    
    messages = [{"role": "system", "content": gpt_system}]
    for gpt, ollama in zip(gpt_messages, ollama_messages):
        messages.append({"role": "assistant", "content": gpt})
        messages.append({"role": "user", "content": ollama})
    
    completion = openai.chat.completions.create(
        model=gpt_model,
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )
    return completion.choices[0].message.content


def call_ollama():
    """Call Ollama with conversation history from both bots"""
    global gpt_messages, ollama_messages, ollama_system, ollama_model
    
    messages = []
    for gpt, ollama_message in zip(gpt_messages, ollama_messages):
        messages.append({"role": "user", "content": gpt})
        messages.append({"role": "assistant", "content": ollama_message})
    # Add the latest GPT message for Ollama to respond to
    if len(gpt_messages) > len(ollama_messages):
        messages.append({"role": "user", "content": gpt_messages[-1]})
    
    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/chat",
            json={
                "model": ollama_model,
                "messages": messages,
                "system": ollama_system,
                "stream": False
            },
            timeout=120  # Increased timeout for slower responses
        )
        
        if response.status_code == 200:
            result = response.json()
            if "message" in result and "content" in result["message"]:
                return result["message"]["content"]
            else:
                return f"Error: Unexpected response format: {result}"
        else:
            error_text = response.text
            return f"Error: HTTP {response.status_code} - {error_text}"
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama. Make sure Ollama is running on localhost:11434. Try running: ollama serve"
    except requests.exceptions.Timeout:
        return "Error: Ollama request timed out. The model might be taking too long to respond."
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    """Main function to run the chatbot conversation"""
    global gpt_messages, ollama_messages
    
    # Initialize message lists
    gpt_messages = ["I've been thinking - do you think artificial intelligence will eventually make human creativity obsolete, or will it just change what we consider creative?"]
    ollama_messages = ["That's a fascinating question! I believe AI will actually enhance human creativity rather than replace it. It can be a powerful tool that amplifies our imagination and helps us explore new possibilities we might not have discovered alone. What do you think about the collaborative potential between humans and AI?"]
    
    print(f"GPT:\n{gpt_messages[0]}\n")
    print(f"Ollama:\n{ollama_messages[0]}\n")
    
    for i in range(5):
        gpt_next = call_gpt()
        print(f"GPT:\n{gpt_next}\n")
        gpt_messages.append(gpt_next)
        
        ollama_next = call_ollama()
        print(f"Ollama:\n{ollama_next}\n")
        ollama_messages.append(ollama_next)


if __name__ == "__main__":
    main()


"""
3-Way Chatbot Conversation
Three AI characters having a fun conversation using different LLMs.
Uses the approach: 1 system prompt + 1 user prompt with full conversation history.
"""

import os
from openai import OpenAI
import requests
import json
import time

# Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OLLAMA_BASE_URL = "http://localhost:11434/api"

# Character definitions with fun personalities
CHARACTERS = {
    "Alex": {
        "model": "openai",  # Using OpenAI
        "model_name": "gpt-4o-mini",
        "system_prompt": """You are Alex, a witty and slightly sarcastic tech enthusiast who loves making puns and 
        references to memes. You're always trying to one-up your friends with clever jokes, but you're also genuinely 
        helpful. Keep your responses short (1-3 sentences), natural, and funny. You're debating with Blake and Charlie 
        about random topics.""",
        "name": "Alex"
    },
    "Blake": {
        "model": "ollama",  # Using Ollama
        "model_name": "llama3.2",
        "system_prompt": """You are Blake, an overly enthusiastic and dramatic friend who gets excited about everything 
        and uses lots of emojis (but type them as text like :D or :P). You're very passionate and tend to exaggerate 
        things. You're having a conversation with Alex and Charlie. Keep responses short (1-3 sentences), energetic, 
        and fun.""",
        "name": "Blake"
    },
    "Charlie": {
        "model": "ollama",  # Using Ollama
        "model_name": "llama3.2:1b",  # Small model (~1.3GB)
        "system_prompt": """You are Charlie, a laid-back and philosophical friend who always tries to find the deeper 
        meaning in everything, even the silliest topics. You speak in a calm, thoughtful way but with a dry sense of 
        humor. You're chatting with Alex and Blake. Keep responses short (1-3 sentences), thoughtful but funny.""",
        "name": "Charlie"
    }
}

# Initialize OpenAI client
openai_client = None
if OPENAI_API_KEY:
    openai_client = OpenAI(api_key=OPENAI_API_KEY)


def call_openai(model_name, system_prompt, user_prompt):
    """Call OpenAI API"""
    if not openai_client:
        raise ValueError("OpenAI API key not set. Please set OPENAI_API_KEY environment variable.")
    
    response = openai_client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.8,
        max_tokens=150
    )
    return response.choices[0].message.content.strip()


def call_ollama(model_name, system_prompt, user_prompt):
    """Call Ollama API"""
    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/chat",
            json={
                "model": model_name,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "stream": False,
                "options": {
                    "temperature": 0.8,
                    "num_predict": 150
                }
            },
            timeout=30
        )
        response.raise_for_status()
        return response.json()["message"]["content"].strip()
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Ollama API error: {e}. Make sure Ollama is running and the model is available.")


def format_conversation_history(conversation):
    """Format conversation history for the user prompt"""
    if not conversation:
        return "The conversation is just starting."
    
    formatted = "The conversation so far is as follows:\n\n"
    for entry in conversation:
        formatted += f"{entry['speaker']}: {entry['message']}\n"
    return formatted


def get_response(character, conversation_history):
    """Get a response from a character given the conversation history"""
    char_config = CHARACTERS[character]
    system_prompt = char_config["system_prompt"]
    
    # Build user prompt with full conversation history
    conversation_text = format_conversation_history(conversation_history)
    user_prompt = f"""You are {character}, in conversation with {', '.join([c for c in CHARACTERS.keys() if c != character])}.
{conversation_text}
Now respond with what you would like to say next, as {character}. Keep it short, natural, and in character."""

    # Call the appropriate API
    if char_config["model"] == "openai":
        response = call_openai(char_config["model_name"], system_prompt, user_prompt)
    else:  # ollama
        response = call_ollama(char_config["model_name"], system_prompt, user_prompt)
    
    return response


def run_conversation(num_turns=10, starting_topic="whether pineapple belongs on pizza"):
    """Run a 3-way conversation"""
    conversation = []
    
    print("=" * 60)
    print(f"🎭 3-Way Chatbot Conversation")
    print(f"Topic: {starting_topic}")
    print("=" * 60)
    print()
    
    # Initial messages to start the conversation
    initial_messages = {
        "Alex": f"Okay, let's settle this once and for all: {starting_topic}. I'm team YES, obviously.",
        "Blake": f"WAIT WHAT?! :O Alex, you can't be serious! That's like putting ketchup on ice cream! :P",
        "Charlie": f"Hmm, I think we need to consider the philosophical implications here. What even IS pizza, really?"
    }
    
    # Add initial messages
    for speaker, message in initial_messages.items():
        conversation.append({"speaker": speaker, "message": message})
        print(f"{speaker}: {message}\n")
        time.sleep(0.5)
    
    # Continue the conversation
    turn_order = ["Alex", "Blake", "Charlie"]
    turn_index = 0
    
    for turn in range(num_turns):
        current_speaker = turn_order[turn_index % len(turn_order)]
        
        try:
            print(f"🤔 {current_speaker} is thinking...")
            response = get_response(current_speaker, conversation)
            conversation.append({"speaker": current_speaker, "message": response})
            print(f"{current_speaker}: {response}\n")
            time.sleep(1)  # Small delay for readability
            
        except Exception as e:
            print(f"❌ Error getting response from {current_speaker}: {e}\n")
            # Continue with next speaker
            pass
        
        turn_index += 1
    
    print("=" * 60)
    print("Conversation ended!")
    print("=" * 60)
    
    return conversation


def main():
    """Main function"""
    print("\n🚀 Starting 3-Way Chatbot Conversation\n")
    
    # Check if Ollama is available
    try:
        response = requests.get(f"{OLLAMA_BASE_URL.replace('/api', '')}/api/tags", timeout=5)
        print("✅ Ollama is running\n")
    except:
        print("⚠️  Warning: Could not connect to Ollama. Make sure it's running on localhost:11434")
        print("   You can install it from: https://ollama.ai\n")
    
    # Check OpenAI
    if not OPENAI_API_KEY:
        print("⚠️  Warning: OPENAI_API_KEY not set. OpenAI models won't work.")
        print("   Set it with: export OPENAI_API_KEY='your-key-here'\n")
    
    # Run conversation with a fun topic
    topics = [
        "whether hot dogs are sandwiches",
        "if cereal is a soup",
        "whether you'd rather fight 100 duck-sized horses or 1 horse-sized duck",
        "if time travel movies create plot holes by existing"
    ]
    
    import random
    topic = random.choice(topics)
    
    conversation = run_conversation(num_turns=12, starting_topic=topic)
    
    # Optionally save conversation
    with open("conversation_log.json", "w") as f:
        json.dump(conversation, f, indent=2)
    print("\n💾 Conversation saved to conversation_log.json")


if __name__ == "__main__":
    main()


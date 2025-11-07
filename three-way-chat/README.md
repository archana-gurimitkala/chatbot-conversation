# 3-Way Chatbot Conversation

A fun 3-way conversation between three AI characters using different LLMs (OpenAI and Ollama).

## Features

- **3 Characters**: Alex (OpenAI), Blake (Ollama), and Charlie (Ollama)
- **Fun Personalities**: Each character has a unique, humorous personality
- **Full Conversation History**: Uses the approach of 1 system prompt + 1 user prompt with complete conversation history
- **Multiple LLMs**: Combines OpenAI and Ollama models

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up OpenAI API key** (for Alex):
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

3. **Set up Ollama** (for Blake and Charlie):
   - Install Ollama from https://ollama.ai
   - Pull the required models:
     ```bash
     ollama pull llama3.2
     ollama pull llama3.2:1b
     ```
   - Make sure Ollama is running (it should start automatically)
   - Note: `llama3.2:1b` is a small model (~1.3GB) perfect for Charlie

## Usage

Run the conversation:
```bash
python three_way_chat.py
```

The script will:
- Start a conversation on a random fun topic
- Have the three characters debate/discuss it
- Save the conversation to `conversation_log.json`

## Customization

You can modify:
- **Characters**: Edit the `CHARACTERS` dictionary in `three_way_chat.py`
- **Models**: Change `model_name` for each character
- **Topics**: Modify the `topics` list in the `main()` function
- **Number of turns**: Change `num_turns` parameter

## How It Works

The implementation uses the recommended approach:
- Each turn, one character gets a response
- The system prompt defines the character's personality
- The user prompt includes the full conversation history
- This allows each model to see the complete context

## Example Output

```
🚀 Starting 3-Way Chatbot Conversation

✅ Ollama is running

============================================================
🎭 3-Way Chatbot Conversation
Topic: whether hot dogs are sandwiches
============================================================

Alex: Okay, let's settle this once and for all: whether hot dogs are sandwiches. I'm team YES, obviously.

Blake: WAIT WHAT?! :O Alex, you can't be serious! That's like putting ketchup on ice cream! :P

Charlie: Hmm, I think we need to consider the philosophical implications here. What even IS a sandwich, really?

🤔 Alex is thinking...
Alex: Look, if it's meat between bread, it's a sandwich. That's just basic sandwich math. Hot dogs are basically cylindrical sandwiches with commitment issues.

🤔 Blake is thinking...
Blake: NO WAY! :D A hot dog is a HOT DOG! It's its own thing! It's like saying a taco is a sandwich - ABSOLUTELY NOT! :P

🤔 Charlie is thinking...
Charlie: But wait... if we define a sandwich as two separate pieces of bread with filling, then a hot dog fails. But if it's about the essence - sustenance between bread-like structures - then perhaps we're all sandwiches in the cosmic sense.

🤔 Alex is thinking...
Alex: Charlie, you're overthinking this. A taco is NOT a sandwich, but a hot dog? That's a sandwich that went to the gym and got ripped. Same concept, better shape.

🤔 Blake is thinking...
Blake: I'M SCREAMING! :O This is chaos! Next you'll say pizza is a sandwich! Where does it END?! :D

🤔 Charlie is thinking...
Charlie: Actually, pizza could be considered an open-faced sandwich if we're being technical... but I think we've lost the plot here. The real question is: why do we need to categorize everything?

🤔 Alex is thinking...
Alex: Because categories are how we make sense of the world! And hot dogs are sandwiches. This is not up for debate. It's science.

🤔 Blake is thinking...
Blake: SCIENCE?! :O You call THIS science?! This is MADNESS! A hot dog is a HOT DOG! It says so right in the name! :P

🤔 Charlie is thinking...
Charlie: Perhaps the true answer lies not in what it is, but in what it means to us. A hot dog at a baseball game is an experience, not just a food category.

🤔 Alex is thinking...
Alex: Okay, Charlie's getting too deep. Blake, you're being dramatic. It's a sandwich. End of story. Let's move on to whether cereal is soup.

🤔 Blake is thinking...
Blake: CEREAL IS SOUP?! :O NO NO NO! This conversation is getting OUT OF HAND! :D

🤔 Charlie is thinking...
Charlie: Well, if soup is a liquid-based dish with solid components... technically cereal with milk could qualify. But I sense we're opening Pandora's box here.

============================================================
Conversation ended!
============================================================

💾 Conversation saved to conversation_log.json
```

Enjoy the conversation! 🎉


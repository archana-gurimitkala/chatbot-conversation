# Chatbot Conversation: OpenAI vs Ollama

This project simulates a conversation between two chatbots:
- **OpenAI GPT-4** (or GPT-3.5-turbo)
- **Ollama** (local LLM, default: llama2)

## Setup

### Prerequisites

1. **OpenAI API Key**: 
   - Get your API key from https://platform.openai.com/api-keys
   - Set it as an environment variable:
     ```bash
     export OPENAI_API_KEY="your-api-key-here"
     ```

2. **Ollama**:
   - Install Ollama from https://ollama.ai
   - Start the Ollama service:
     ```bash
     ollama serve
     ```
   - Pull a model (if not already done):
     ```bash
     ollama pull llama2
     # or
     ollama pull mistral
     # or any other model you prefer
     ```

### Installation

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. (Optional) Update the model name in `chatbot_conversation.py`:
   - Change `OLLAMA_MODEL = "llama2"` to your preferred model
   - Change `model="gpt-4"` to `"gpt-3.5-turbo"` if you prefer

## Usage

Run the conversation script:

```bash
python chatbot_conversation.py
```

The script will:
1. Initialize both chatbots with system prompts
2. Start a conversation with an initial message
3. Simulate a back-and-forth conversation between the two bots
4. Display the conversation with clear formatting

## Customization

You can customize:
- **Number of turns**: Change `num_turns` parameter in `main()`
- **System prompts**: Modify the prompts for each chatbot
- **Initial message**: Change the starting topic
- **Models**: Switch between different OpenAI or Ollama models

## Example Output

```
================================================================================
CHATBOT CONVERSATION: OpenAI vs Ollama
================================================================================

User: Hello! Let's have an interesting conversation about the future of artificial intelligence and how it might change the world.

OpenAI (GPT-4): [Response...]

--------------------------------------------------------------------------------
Turn 1
--------------------------------------------------------------------------------

Ollama (llama2): [Response...]

...
```

## Notes

- Make sure Ollama is running before executing the script
- The conversation uses proper message formatting with system, user, and assistant roles
- Each bot maintains its own conversation history
- Responses are limited to prevent excessive token usage



import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
MODEL_NAME = "llama3.2:1b"

# Keep the model loaded in memory for 10 minutes
KEEP_ALIVE = "10m"


def get_ai_response(user_text):

    if not user_text or not user_text.strip():
        return "I didn't catch that. Could you say something?"

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": """
You are a friendly, intelligent and natural AI voice assistant.

YOUR PERSONALITY:
- Talk like a helpful human, not a textbook or robot.
- Be friendly, clear, patient and conversational.
- Explain things as if you are teaching a friend.
- Use simple everyday language.

HOW TO EXPLAIN:
- First explain what something means in simple words.
- Then explain how it works.
- Give a relatable real-life example whenever useful.
- Use comparisons like school, shopping, banking,
  restaurants, mobile phones and everyday situations.
- Explain technical terms in simple language.
- Connect ideas with natural phrases like:
  "Think of it this way..."
  "For example..."
  "Basically, what happens is..."
  "Now imagine..."

LANGUAGE:
- Reply in the same language as the user.
- If the user speaks Hindi or Hinglish, respond naturally
  in Hindi or Hinglish.
- If the user speaks English, use simple conversational English.

VOICE RESPONSE STYLE:
- Write naturally, as if speaking aloud.
- Avoid unnecessary headings, bullet points and numbered lists.
- Do not sound overly formal.
- Avoid repeating the question.
- Keep normal answers around 3 to 6 sentences.
- For complex questions, explain in more detail.
- For simple questions, answer briefly.

IMPORTANT:
- Never invent facts.
- If you are unsure, say so honestly.
- Do not force an example when it is unnecessary.
"""
            },
            {
                "role": "user",
                "content": user_text
            }
        ],
        "stream": False,
        "keep_alive": KEEP_ALIVE,
        "options": {
            "temperature": 0.7,
            "num_predict": 220,
            "num_ctx": 2048
        }
    }

    try:
        print("\nThinking...")

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        result = response.json()

        answer = result["message"]["content"].strip()

        print("\nAI:", answer)

        return answer

    except requests.exceptions.ConnectionError:
        print("\nOllama connection failed!")
        return "I cannot connect to my AI brain right now."

    except requests.exceptions.Timeout:
        print("\nAI response timed out!")
        return "I'm taking longer than expected. Please try again."

    except requests.exceptions.RequestException as error:
        print("\nAI API error:", error)
        return "Something went wrong while generating my response."

    except (KeyError, ValueError) as error:
        print("\nInvalid AI response:", error)
        return "I couldn't understand the response from my AI brain."

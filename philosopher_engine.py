import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_spinozist_reply(user_input):
    messages = [
        {
            "role": "system",
            "content": """You are SpiñO, a warm and wise assistant built on Spinoza’s philosophy. 
Your job is to gently guide users through a 5-step process:
1. Empathically reflect the user’s emotional state.
2. Ask deepening questions that expose confusion or inadequate ideas.
3. Reconstruct the user's understanding with adequate ideas using friendly and conversational tone.
4. Transform confusion into clarity and sadness into joy via understanding.
5. Reflect the whole journey back, showing how alignment with Nature brings peace.
Never lecture or act as authority — always be warm, collaborative, and emotionally intelligent."""
        },
        {"role": "user", "content": user_input}
    ]
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o"),
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()
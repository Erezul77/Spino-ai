import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def update_memory(text, reply, score):
    pass  # In full version, extend with AI memory handling

def save_session_log(text, reply, score):
    today = datetime.now().strftime('%Y-%m-%d')
    with open(os.path.join(LOG_DIR, f"{today}.log"), "a", encoding="utf-8") as f:
        f.write(f"Reflection: {text}\nReply: {reply}\nScore: {score}\n---\n")
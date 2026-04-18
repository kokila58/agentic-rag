import json
import os

MEMORY_PATH = "storage/chat_memory"

def save_chat(session_id, question, answer):

    os.makedirs(MEMORY_PATH, exist_ok=True)

    file = f"{MEMORY_PATH}/{session_id}.json"

    history = []

    if os.path.exists(file):
        with open(file) as f:
            history = json.load(f)

    history.append({
        "question": question,
        "answer": answer
    })

    with open(file, "w") as f:
        json.dump(history, f)
import os
from groq import Groq

from config import api_key
from speech_utils import speak


def ai(prompt):
    client = Groq(api_key=api_key)
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=[
            {
                "role": "user",
                "content": prompt
            },
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    if not os.path.exists("ai_answers_files"):
        os.makedirs("ai_answers_files", exist_ok=True)

    with open(f"ai_answers_files/{prompt}.md", "w") as f:
        f.write(f"Prompt: {prompt}\n\n")
        for chunk in completion:
            content = chunk.choices[0].delta.content or ""
            f.write(content)
        os.startfile(f"C:\Project\JarvisAI\main_files\\ai_answers_files\\{prompt}.md")

chatStr = ""

def chat_ai(user_spoken):
    global chatStr
    chatStr += f"Hussain: {user_spoken}\n Jarvis: "
    client = Groq(api_key=api_key)
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=[{"role": "user", "content": chatStr}],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    full_response = ""
    for chunk in completion:
        ai_answer = chunk.choices[0].delta.content or ""
        full_response += ai_answer
    chatStr += f"{full_response}\n"
    speak(full_response)

def extract_site_name(user_spoken):
    prompt = f"Extract only the name of the website from this sentence: '{user_spoken}'. Only return the core name like 'youtube' or 'google', without https, www, or .com."

    client = Groq(api_key=api_key)
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    return completion.choices[0].message.content.strip().lower()

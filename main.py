import speech_recognition as sr
import os
import webbrowser

from ai_works import ai, chat_ai, extract_site_name
from speech_utils import speak


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        pause_threshold = 1.2
        audio = r.listen(source)
        user_spoken = r.recognize_google(audio, language='en')
        print(f"User said: {user_spoken}")
        return user_spoken

def open_any_website(user_spoken):
    site_name = extract_site_name(user_spoken)
    url = f"https://www.{site_name}.com"
    speak(f"Opening {site_name}")
    webbrowser.open(url)


if __name__ == '__main__':
    speak("Hi I'm jarvis ai")
    chatbot_mode = False  # Global flag

    while True:
        print("Listening...")
        user_spoken = take_command().lower()

        # Check for AI/Chatbot trigger phrases
        if "artificial intelligence" in user_spoken:
            ai(prompt=user_spoken)

        elif "become the chatbot" in user_spoken:
            chatbot_mode = True
            speak("Chatbot mode activated. You can now chat with me.")
            chat_ai(user_spoken=user_spoken)

        elif "exit chatbot" in user_spoken:
            chatbot_mode = False
            speak("Chatbot mode deactivated.")

        elif chatbot_mode:
            chat_ai(user_spoken=user_spoken)

        else:
            open_any_website(user_spoken)

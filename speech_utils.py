import win32com.client

def speak(text):
    """
    :param text: The text which it will speak
    :Purpose: This function say system to speak
    """
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)
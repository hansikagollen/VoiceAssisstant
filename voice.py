from gtts import gTTS
import os

def speak_telugu(text):
    tts = gTTS(text=text, lang="te")
    tts.save("reply.mp3")
    os.system("start reply.mp3")

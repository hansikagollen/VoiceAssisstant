import speech_recognition as sr

mics = sr.Microphone.list_microphone_names()
print("Microphones detected:")
for i, mic in enumerate(mics):
    print(i, mic)

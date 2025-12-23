import speech_recognition as sr

r = sr.Recognizer()

# Manual sensitivity (stable)
r.energy_threshold = 300
r.dynamic_energy_threshold = False
r.pause_threshold = 0.8

mic = sr.Microphone(
    device_index=9,        # keep 9 (works best on your system)
    sample_rate=16000,
    chunk_size=1024
)

print("🎤 Microphone ready")
print("⏳ Waiting for you to speak (up to 10 seconds)...")

with mic as source:
    # ❌ DO NOT call adjust_for_ambient_noise
    audio = r.listen(
        source,
        timeout=None,          # wait until speech starts
        phrase_time_limit=10   # record max 10 seconds
    )

print("🔍 Recognizing speech...")

try:
    text = r.recognize_google(audio, language="te-IN")
    print("✅ Speech detected:", text)
except sr.UnknownValueError:
    print("❌ Speech captured but not recognized")
except Exception as e:
    print("❌ Error:", e)

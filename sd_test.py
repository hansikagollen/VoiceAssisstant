import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

DEVICE_INDEX = 9          # WASAPI Microphone Array
FS = 48000                # ✅ MUST match default samplerate
SECONDS = 5

print("🎤 Recording for 5 seconds… Speak Telugu")

audio = sd.rec(
    int(FS * SECONDS),
    samplerate=FS,
    channels=2,            # ✅ Device supports 2 channels
    dtype="float32",
    device=DEVICE_INDEX
)

sd.wait()

# Convert stereo → mono
audio_mono = np.mean(audio, axis=1)

write("test.wav", FS, audio_mono)

print("✅ Saved test.wav — play it now")

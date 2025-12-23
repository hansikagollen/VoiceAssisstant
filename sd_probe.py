import sounddevice as sd

device_index = 9  # WASAPI Microphone Array

info = sd.query_devices(device_index, 'input')
print("Device name:", info['name'])
print("Default samplerate:", info['default_samplerate'])
print("Max input channels:", info['max_input_channels'])

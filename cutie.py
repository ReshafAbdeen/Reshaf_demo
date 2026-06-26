from gtts import gTTS

text_to_speak = "Hello! This audio was generated using ten lines of Python code."
language = "en"
filename = "speech.mp3"

print("--- Text-to-Speech Converter ---")
tts = gTTS(text=text_to_speak, lang=language, slow=False)
tts.save(filename)

print(f"Success! Audio saved as '{filename}'")
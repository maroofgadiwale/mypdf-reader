from gtts import gTTS
import time
import os

def voice_generate(page):
    # Generate TTS audio file
    tts = gTTS(text=page, lang="en")
    # Save to temporary directory in Render
    file_path = "/tmp/audio_file.mp3"
    tts.save(file_path)
    print(f"Audio file saved at: {file_path}")
    # Simulate playback delay (optional, can be removed)
    time.sleep(2)
    # Optional: Delete after use (comment this if you want to keep the file)
    os.remove(file_path)
    print("Audio file deleted.")


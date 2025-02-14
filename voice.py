# Program to implement TTS Application:
import requests
import pygame
import time
import os

def voice_generate(page):
    params = {
        "key":os.environ.get("api_key"),
        "src":page,
        "hl":"en-us",
    }

    response = requests.get(url = "http://api.voicerss.org",params = params)

    with open("/tmp/audio_file.wav",mode = "wb") as file:
        file.write(response.content)

    # Play the WAV file
    pygame.mixer.init()
    pygame.mixer.music.load("/tmp/audio_file.wav")
    pygame.mixer.music.play()

    # Keep script running until audio finishes playing
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)  # Avoid high CPU usage with a short sleep

    # Stop the mixer and unload the music
    pygame.mixer.music.stop()
    pygame.mixer.quit()

    os.remove("/tmp/audio_file.wav")


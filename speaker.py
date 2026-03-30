import pyttsx3
import time

class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)   # slower speech
        self.last_spoken = ""
        self.last_time = 0
        self.cooldown = 3  # seconds

    def speak(self, text):
        current_time = time.time()

        # Speak only if new object OR after cooldown
        if text != self.last_spoken or (current_time - self.last_time) > self.cooldown:
            self.engine.say(text)
            self.engine.runAndWait()
            self.last_spoken = text
            self.last_time = current_time
import speech_recognition as sr import pyttsx3
import serial import time
# Initialize serial communication (change COM port accordingly) ser = serial.Serial('COM4', 9600, timeout=1) # Example for Windows
# For Linux: use '/dev/ttyUSB0'
# Initialize text-to-speech engine engine = pyttsx3.init()
def speak(text): print(f"Assistant: {text}") engine.say(text) engine.runAndWait()
def get_command(): r = sr.Recognizer()
with sr.Microphone() as source: speak("Listening for command...")
audio = r.listen(source, phrase_time_limit=4) try:
command = r.recognize_google(audio).lower() print(f"You said: {command}")
22
return command
except sr.UnknownValueError: speak("Sorry, I didn't understand.") return ""
except sr.RequestError: speak( "Speech service unavailable.")
return ""
def main(): while True:
command = get_command()
if "light on" in command: ser.write(b'LIGHT_ON\n') speak("Turning on the light")
elif "light off" in command: ser.write(b'LIGHT_OFF\n') speak("Turning off the light")
elif "fan on" in command: ser.write(b'FAN_ON\n') speak("Turning on the fan")
elif "fan off" in command: ser.write(b'FAN_OFF\n') speak("Turning off the fan")
23
elif "exit" in command: speak("Exiting system") break
time.sleep(1)
if _name_ == "_main_":

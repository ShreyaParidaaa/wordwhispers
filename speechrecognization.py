#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I am listening, please speak now.")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, there seems to be an issue with the speech recognition service.")
            return ""
def main():
    speak("Hello! I am your voice assistant. How can I help you?")
    while True:
        command = listen()
        
        if "hello" in command:
            speak("Hello! How are you?")
        
        elif "your name" in command:
            speak("I am your voice assistant, here to help you.")
        
        elif "stop" in command or "exit" in command or "bye" in command:
            speak("Goodbye! Have a great day.")
            break
        
        elif command:
            speak(f"You said: {command}. I'm still learning how to respond to that.")
        else:
            speak("I didn't catch that. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





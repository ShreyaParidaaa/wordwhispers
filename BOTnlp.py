#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyttsx3

engine = pyttsx3.init()

def speak(text):
  engine.say(text)
  engine.runAndWait()

def main():
  speak("Hello! I am your simple bot from Mallareddy University")
  speak("You can say hello,ask my name, or say goodbye.")

  while True:
    command = input("You: ").lower()

    if "hello" in command:
      speak("Hello! How can I assist you today?")

    elif "name" in command:
      speak("I am a simple bot. You can call me MalliBot.")

    elif "HAHA" in command:
      speak("haha")

    elif "goobye" in command:
      speak("Goodbye! Have a great day!")
      break
    else:
      speak("I'm sorry, I didn't understand that. Please try again.")

if __name__== "__main__":
  main()


# In[ ]:





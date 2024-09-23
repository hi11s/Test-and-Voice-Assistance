import pyttsx3

def speak(text):
    #Initialize the TTS engine
    engine = pyttsx3.init()
    #set properties (optional)
    engine.setProperty('rate', 150) #speed percent (can go over 100)
    engine.setProperty('volume', 0.9) #volume 0-1

    #Speak over text
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    message = "Hello Frita, This is Hills' computer speaking!"
    speak(message)
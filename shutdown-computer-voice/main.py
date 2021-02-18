import os 
import pyttsx3
import speech_recognition as sr
import pyaudio



# Creating Class
class pythonhub:
    # Method to take coice commands as input
    def takeCommands(self):
        # Using Recognizer and Microphone Method for input voice
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening")
            # Number pf seconds of non-speaking audio before
            # a phrase is considered complete
            r.pause_threshold = 0.7
            audio = r.listen(source)
            #Voice input is identified
            try:
                # Listening voice commands in turkish
                print("Recognizing")
                Query = r.recognize_google(audio, language='tr')

                # Displaying the voice command
                print("the query is printed='", Query, "'")
            except Exception as e:
                # Displaying exception
                print(e)
                # Handling exception
                print("Say that again sir")
                return "None"
            return Query
    # Method for voice output
    def Speak(self, audio):
        # Constructor call for pyttsx3.init()
        engine = pyttsx3.init('sapi5')
        # Setting voice type and id
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[0].id)
        engine.say(audio)
        engine.runAndWait()

    #method to self shut down system    
    def quitSelf(self):
        self.Speak("Sir, shall I shut down the computer")
        # Input voice command
        take = self.takeCommands()
        choice = take
        if "Evet" in choice:
            # Shutting down
            print("Shutting down the computer")
            self.Speak("Shutting the computer")
            os.system("shutdown /s /t 999")
        if "no" in choice:
            #Idle
            print("Thank you sir")
            self.Speak("Thank you sir")
# Driver Code

if __name__ == "__main__":
    Maam = pythonhub()
    Maam.quitSelf()
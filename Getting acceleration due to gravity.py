import pyttsx3
import time
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("This is program for finding acceleration due to gravity of any planet whose mass and radius is given")
speak("Follow the instructions")
while True:
    speak('Hello what is the mass of the planet ?')
    mass = input('What is the mass of the planet ?\n')
    speak('now pardon me by typing radius of planet as this is mandatory')
    radius = input('What is the radius of the planet ?\n')
    Universal_gravatational_constant = 0.0000000000667
    adg = float(Universal_gravatational_constant) * float(mass)
    d = float(radius) * float(radius)
    f = float(adg) / float(d)
    print("The acceleration due to gravity on the planet whose mass is {} kg and radius is {} m is {} m/s^2".format((mass) ,(radius) ,(f)))
    t = "The acceleration due to gravity on the planet whose mass is {} kilogram and radius is {} meter is {} meters per second squared".format((mass) ,(radius) ,(f))
    speak(t)
    time.sleep(5)


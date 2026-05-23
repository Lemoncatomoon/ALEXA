import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import geocoder
import requests 

wikipedia.set_lang("fr")


listener = sr.Recognizer()
engine = pyttsx3.init()
def talk(text):
 engine.say(text)
 engine.runAndWait()

def take_command(command):
    print(command)
    if 'joue' in command:
        song = command.replace('joue','')
        talk('okay,je vais jouer'+ song)
        pywhatkit.playonyt(song)
        print('okay, voilà ce que que vous avez demander')
    if  'heure' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk("C'est "+ time)
    if 'cherche' in command:
        qcm = command.replace('cherche','')
        answer = wikipedia.summary(qcm, 1)
        talk(answer)
        print(answer)
    elif 'localisation' in command:
        location = geocoder.ip('me')
        talk("Tu habites à " + location.city + ", " + location.country)
        print("Localisation: Ville:", location.city, ", Pays:", location.country)
    if 'blague' in command :
        talk(pyjokes.get_joke('fr','all'))
    if 'météo' in command:

        if 'de' in command:
            ville = command.split('de')[1].strip()
            url = f'https://wttr.in/{ville}'
            response = requests.get(url)
            meteo_data = response.text


            first_three_lines = meteo_data.splitlines()[:7]


            for line in first_three_lines:
                print(line)


            talk(first_three_lines)





try:
    with sr.Microphone() as source:
        print("Je t'entends...")
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
        command = listener.recognize_google(voice, language="fr-FR")
        command = command.lower()

        if 'alexa' in command:
            command = command.replace('alexa', '')
            talk(command)

        take_command(command)
        


except:
       pass




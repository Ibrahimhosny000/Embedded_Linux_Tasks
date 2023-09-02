# ----------------------
# -----       ------
#   Smart scripts:-
# -----       ------
# ----------------------


# import library
import webbrowser
from time import ctime
import os
import playsound
from gtts import gTTS
import random
import speech_recognition as sr

# import shutil

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()


# Reading Audio file as source
# listening the audio file and store in audio_text variable
def Bixby_Speak(audios):
    # tts = gTTS(text=audios, lang='en', slow=False)
    tts = gTTS(text=audios, lang="en")
    audioF = "audio.mp3"
    tts.save(audioF)
    playsound.playsound(audioF)
    print(audios)
    os.remove(audioF)


def record(ask=False):
    with sr.Microphone(device_index=None) as source:
        r.adjust_for_ambient_noise(source)
        if ask:
            Bixby_Speak(ask)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio, language="en")
        except sr.UnknownValueError:
            Bixby_Speak("sorry i did not get that")
        except sr.RequestError:
            Bixby_Speak("sorry Service is Down")
        return voice_data.lower()


def Respond(voice_data):
    # it listens for words (name/my_name) and triggers the speach:-
    if "name" in voice_data or "my name" in voice_data:
        Bixby_Speak("welcome Ibrahim")
    # it listens for words (time/hour) and triggers the speach:-
    if "time" in voice_data or "hour" in voice_data:
        Bixby_Speak(ctime())
    # it listens for words (google/search) and triggers the speach:-
    if "google" in voice_data or "search" in voice_data:
        search = record(" tell me what you need ")
        # search = record('what dow want to search')
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        # Bixby_Speak('Here is what i Found For' + search)
        Bixby_Speak("here you go" + search)

    if "locatin" in voice_data or "place" in voice_data:
        location = record("tell me the location")
        # location = record("what is the location do want ")
        url = "https://google.nl/maps/place/" + location + "/&amp"
        webbrowser.get().open(url)
        # Bixby_Speak('Here is what i Found For' + location)
        Bixby_Speak("searching place" + search)
    # it listens for my repo and respond with the repo url
    if "myrepo" in voice_data:
        url = "https://github.com/Ibrahimhosny000"
        webbrowser.get().open(url)
        # it listens for fun or play and open a gaming website
    if "fun" in voice_data or "play" in voice_data:
        games = "https://www.friv.com/"
        webbrowser.get().open(games)

    if "exit" in voice_data:
        exit()


Bixby_Speak("Hello ibrahim, How can I help you")


while 1:
    voice_data = record()
    Respond(voice_data)

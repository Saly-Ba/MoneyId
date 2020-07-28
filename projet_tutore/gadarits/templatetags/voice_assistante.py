from django import template
from django.shortcuts import redirect
# importing speech recognition package from google api 
import speech_recognition as sr 
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
import wolframalpha # to calculate strings into formula 
from selenium import webdriver # to control browser operations 


register = template.Library()

num = 1

@register.simple_tag
def assistant_speaks(output): 
    global num 

	# num to rename every audio file 
	# with different name to remove ambiguity 
    num += 1
	
    toSpeak = gTTS(text = output, lang ='fr', slow = False) 
	# saving the audio file given by google text to speech 
    file = str(num)+".mp3" 
    toSpeak.save(file) 
	
	# playsound package is used to play the same file. 
    playsound.playsound(file, True)
    os.remove(file)
    
    return  output

def get_audio(): 

	rObject = sr.Recognizer() 
	audio = '' 

	with sr.Microphone() as source: 
		print("Parler...") 
		
		# recording the audio using speech recognition 
		audio = rObject.listen(source, phrase_time_limit = 5) 
	print("Stop.") # limit 5 secs 

	try: 

		text = rObject.recognize_google(audio, language ='fr-Fr') 
		print("Toi : ", text) 
		return text 

	except: 

		assistant_speaks("Je n'ai pas comprit c'est que vous avez dit, pouvez vous répeter s'il vous plait !") 
		return 0



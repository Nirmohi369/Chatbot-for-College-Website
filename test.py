# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
# fh = open("abc.txt","r")
# mytext= fh.read().replace("\n"," ")

mytext='welcome to chatbot'
# Language in which you want to convert
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")
# fh.close()
os.system("start welcome.mp3")

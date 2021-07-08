from gtts import gTTS
import os
myText ="Welcome to anokh automation,this is a test audio of google text to speech function with python"
language ='en'
output = gTTS(text = myText,lang = language,slow = False)
output.save("audiooutput1.mp3")
os.system("start audiooutput1.mp3")
            

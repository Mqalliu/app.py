#! python3

from googletrans import Translator
from gtts import gTTS
import IPython.display as ipd

def audioplayer(audio):
   ipd.display(ipd.Audio(audio, autoplay=False))

# It asks the user to type in some text

text = input("Give me some text you want me to translate in English and read for you: ")

# It then converts that text in a certain langauge

translator = Translator()

text_to_translate = translator.translate(text, dest='en')

#print(text_to_speech.text)

text_to_speech = text_to_translate.text

# it converts the translated text to speech.

tts=gTTS(text=text_to_speech, lang='en')

tts.save('audio.mp3')



print("Your text would sound like this in English:")

audioplayer('audio.mp3')

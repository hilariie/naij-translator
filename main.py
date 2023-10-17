import speech_recognition as sr
import os
import openai
from gtts import gTTS
from playsound import playsound
import yaml

with open('config.yaml', 'r') as file:
    yml = yaml.safe_load(file)

openai.api_key = yml['key']
translate_to = yml['translate_to']

recognizer = sr.Recognizer()
voice_path = 'translated_audio.mp3'

messages = [{'role': 'system', 'content': f"You are a translator of English text to Nigerian {translate_to}. Do not respond to texts, just translate them"},]

print_format = '-' * 8

try:
    while True:
        with sr.Microphone() as source:
            print(f'Will translate to {translate_to.capitalize()}\n')
            print(f'{print_format} Speak now {print_format}')
            recognizer.pause_threshold = 0.7
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            
            print('transcribing...')
            print('-' * 27)
            text = recognizer.recognize_whisper(audio) 

            print(f'User: {text}')

            messages.append({'role': 'user', 'content': text},)
            chat = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages)

            reply = chat.choices[0].message.content
            print(f'ChatGPT: {reply}')
            print('-' * 27)

            # Convert reply text to audio and play the audio
            if yml['translate_to'] == 'pidgin':
                output_voice = gTTS(reply)
                output_voice.save(voice_path)
                playsound(voice_path)
                os.remove(voice_path)

            # Create time lapse for users to read translated text
            input("Hit 'Enter' to continue")

            messages.pop()
            os.system('cls')

# Exit without throwing an error
except KeyboardInterrupt:
    pass

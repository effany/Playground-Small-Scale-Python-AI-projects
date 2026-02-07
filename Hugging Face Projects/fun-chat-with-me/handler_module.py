import tornado.ioloop
import tornado.web
import datetime
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from concurrent.futures import ThreadPoolExecutor
import asyncio
from transcribe import Transcribtor
from translator_module import EnglishToCzechTranslator
import os

conversations = []

transcribtor = Transcribtor()
english_czech_translator = EnglishToCzechTranslator()

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            'home.html',
            conversations = conversations
        )

class SubmitTextHandler(tornado.web.RequestHandler):
    async def post(self):
        input = self.request.body.decode('utf-8')
        czech_text = english_czech_translator.translate(input)

        if input: 
            conversations.append({
                'type': 'message',
                'text': input,
                'czech': czech_text,
                'time': datetime.datetime.now().strftime("%I:%M %p")
            })
        
        self.render(
            'home.html',
            conversations = conversations
        )

class RecordHandler(tornado.web.RequestHandler):
    async def post(self):
        blob = self.request.body
        time = datetime.datetime.now().strftime("%I:%M %p")
        recording_name = f'recording-{time}'
        
        with open(f'./assets/recordings/{recording_name}', 'wb') as f:
            f.write(blob)

        transcribe_text = transcribtor.transcribe(f'./assets/recordings/{recording_name}')
        czech_text = english_czech_translator.translate(transcribe_text)

        if blob:
            conversations.append({
                'type': 'recording',
                'text': transcribe_text[0],
                'czech': czech_text,
                'time': datetime.datetime.now().strftime("%I:%M %p")
            })
        print(conversations)
        os.remove(f'./assets/recordings/{recording_name}')
        self.render('home.html', conversations = conversations)
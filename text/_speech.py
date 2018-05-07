#-*- coding: utf-8 -*-
import io
import os
import time
#import konlpy

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

#from konlpy.tag import Mecab

client = speech.SpeechClient()

# Loads the audio into memory
with io.open('./test3.wav', 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)
config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='ko-KR')

# Detects speech in the audio file
response = client.recognize(config, audio)

for result in response.results:
	res = result.alternatives[0].transcript

print(res)
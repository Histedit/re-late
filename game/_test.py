#-*- coding: utf-8 -*-
from __future__ import division
import re
import sys
from google.cloud import translate
import json
import requests
from sys import byteorder
from array import array
from struct import pack
import codecs
import pyaudio
import wave
import subprocess
import os
import xml.etree.ElementTree as ET
import math
import io
import os
import time
from six.moves import queue

#import konlpy

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

#from konlpy.tag import Mecab

#client = speech.SpeechClient()

    
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms
THRESHOLD = 1500
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16

class MicrophoneStream(object):
    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            channels=1, rate=self._rate,
            input=True, frames_per_buffer=self._chunk,
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b''.join(data)

def pos_neg(text):
    start_time = time.time()
    translate_client = translate.Client()
    target = 'en'

    translation = translate_client.translate(
        text,
        target_language=target)
        
    print(u"구글 trans : "+str(round(time.time()-start_time,2))+u"초")
    start_time = time.time()
    response = requests.post("https://japerk-text-processing.p.mashape.com/sentiment/",
    headers={
        "X-Mashape-Key": "T3oF0oLdCnmshsjEGaHoNHNUdE3Kp12djWNjsnOEf12H3uocFp",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    },
    data={
        "language": "english",
        "text": translation['translatedText']
    }
    )
    json_data = json.loads(response.text)
    
    print(u"POSNEG판단 : "+str(round(time.time()-start_time,2))+u"초")
    start_time = time.time()
    return json_data["label"]


def listen_print_loop(responses):
    num_chars_printed = 0
    for response in responses:
        if not response.results:
            continue
        result = response.results[0]
        if not result.alternatives:
            continue
        transcript = result.alternatives[0].transcript
        
        if not result.is_final:
            continue
        else:
            return transcript

def str_main():
    language_code = 'ko-KR'

    client = speech.SpeechClient()
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code)
    streaming_config = types.StreamingRecognitionConfig(
        config=config,
        interim_results=True)

    subprocess.call("copy C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\result.1 C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\check.init",shell=True)
    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (types.StreamingRecognizeRequest(audio_content=content)
                    for content in audio_generator)

        responses = client.streaming_recognize(streaming_config, requests)

        return listen_print_loop(responses)


def is_silent(snd_data):
    "Returns 'True' if below the 'silent' threshold"
    return max(snd_data) < THRESHOLD

def normalize(snd_data):
    "Average the volume out"
    MAXIMUM = 16384
    times = float(MAXIMUM)/max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i*times))
    return r

def trim(snd_data):
    "Trim the blank spots at the start and end"
    def _trim(snd_data):
        snd_started = False
        r = array('h')

        for i in snd_data:
            if not snd_started and abs(i)>THRESHOLD:
                snd_started = True
                r.append(i)

            elif snd_started:
                r.append(i)
        return r

    snd_data = _trim(snd_data)
    snd_data.reverse()
    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data

def add_silence(snd_data, seconds):
    r = array('h', [0 for i in range(int(seconds*RATE))])
    r.extend(snd_data)
    r.extend([0 for i in range(int(seconds*RATE))])
    return r

def record():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
        input=True, output=True,
        frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    snd_started = False

    r = array('h')

    while 1:
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)

        silent = is_silent(snd_data)

        if silent and snd_started:
            break
            num_silent += 1
        elif not silent and not snd_started:
            snd_started = True

        if snd_started and num_silent > 5:
            break

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    r = normalize(r)
    r = trim(r)
    r = add_silence(r, 0.3)
    return sample_width, r

def record_to_file(path):
    sample_width, data = record()
    data = pack('<' + ('h'*len(data)), *data)

    wf = wave.open(path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()


def main():
    start_time = time.time()
    tupleType = ['anger','boredom','disgust','fear','happiness','nertral','sadness']
    subprocess.call("del C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\result.1 C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\result.2",shell=True)
    subprocess.call("copy C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\result.events C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\result.1",shell=True)
    subprocess.call("TYPE C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\e.nd >> C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\result.1",shell=True)
    tree = ET.parse('C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\result.1')
    root = tree.getroot()
    preLen = len(root)
    print(u"준비까지 걸리는시간 : "+str(round(time.time()-start_time,2))+u"초")
    start_time = time.time()
    res = str_main()
    print(u"녹음받기 : "+str(round(time.time()-start_time,2))+u"초")
    start_time = time.time()
    posneg = pos_neg(res)

    subprocess.call("copy C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\result.events C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\result.2",shell=True)
    subprocess.call("TYPE C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\e.nd >> C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\result.2",shell=True)
    tree = ET.parse('C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\result.2')
    root = tree.getroot()
    sum = [0,0,0,0,0,0,0]
    nChild = 0
    for i, child in enumerate(root):
        if i > preLen:
            nChild += 1
            for i in range(7):
                sum[i] += float(child[i].get('value'))
    
    file = codecs.open("C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\result.txt", "w", "utf-8")
    data = res + "\n" + tupleType[sum.index(max(sum))] + "\n" + posneg
    file.write(data)
    file.close()
    """ f = open("C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\result.txt", 'w')
    print(res)
    print(tupleType[sum.index(max(sum))])
    data = res + "\n" + tupleType[sum.index(max(sum))] 
    f.write(data)
    f.close()     """
    
    print(u"최종 소요시간 : "+str(round(time.time()-start_time,2))+u"초")
    return


if __name__ == '__main__':
    main()
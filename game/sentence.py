from google.cloud import translate
from sys import argv
import json
import requests

def pos_neg(text):
# Instantiates a client
    translate_client = translate.Client()
    target = 'en'

    translation = translate_client.translate(
        text,
        target_language=target)
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
    return json_data["label"]
strr = '걱정'
print(strr)
print(pos_neg(strr))

'''
    a_dic["ch01_1plyr"]=["positive"]
    #a_dic["ch01_1plyr"]=["positive","negative","nonsense"]
    a_dic["ch01_2plyr"]=["sad"]
    #a_dic["ch01_2plyr"]=["normal","joy","sad","anger"]
    a_dic["ch02_1plyr"]=["positive"]
    #a_dic["ch02_1plyr"]=["positive","negative","nonsense"]
    a_dic["ch02_2plyr"]=["positive"]
    #a_dic["ch02_2plyr"]=["positive","negative","ask"]
    a_dic["ch02_3plyr_a"]=["positive","negative"]
    a_dic["ch02_3plyr_b"]=["positive","negative"]
    a_dic["ch03_1plyr"]=["positive","negative"]
    a_dic["ch03_2plyr"]=["positive","negative"]
    a_dic["ch03_3plyr"]=["answer"]
    a_dic["ch03_4plyr"]=["normal","sad","anger"]
    a_dic["ch03_4plyr"]=["normal","sad","anger"]
    a_dic["ch03_5plyr"]=["why","lie","sad","anger"]
    a_dic["ch05_1plyr"]=["positive_normal","negative_normal","anger_sad"]
    a_dic["ch05_2plyr"]=["positive","negative"]
    a_dic["ch05_3plyr"]=["anger","believe","explain"]
    a_dic["ch05_3plyr_a"]=["apologize","anger"]
    a_dic["ch05_3plyr_a_a"]=["apologize","anger"]
    a_dic["ch05_3plyr_b"]=["believe","notbelieve"]
    a_dic["ch05_3plyr_b_a"]=["worry","positive"]
    a_dic["ch05_3plyr_c"]=["agree","disagree"]
    a_dic["ch05_3plyr_c_a"]=["believe","notbelieve"]
    a_dic["ch05_3plyr_d"]=["believe","notbelieve"]
    a_dic["ch06_1plyr"]=["seoeun","hyoju"]
    a_dic["ch07_1plyr"]=["positive","negative","ask"]
    a_dic["ch07_2plyr"]=["answer"]
    a_dic["ch07_2_1plyr"]=["positive","negative","nonsense"]
    a_dic["ch07_2_2plyr"]=["normal","joy","sad","anger"]
    '''


###  Akhbar PAdhke Sunao.....
 ###      api_key = 53d1b5075ad642968d6f4f4acc8cdc72
 
import requests
import json
def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=53d1b5075ad642968d6f4f4acc8cdc72')
    response = requests.get(url)
    speakjson = response.json()
    print(speakjson)
    speak(speakjson)

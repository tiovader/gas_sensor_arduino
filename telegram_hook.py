from settings import *  
import main as _
import requests

def send_message(message):
    URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=Markdown&text={message}"
    return requests.get(URL)
from flask import Flask
import json
from urllib.request import urlopen

app = Flask(__name__)
@app.route('/')
def extract_ip_lonlat():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)
    ip = data['ip']
    loc = data['loc']
    return 'IP Address: ' + ip + ' Long/Lat: ' + loc

def extract_address():
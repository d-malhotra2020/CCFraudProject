from flask import Flask
import json
from urllib.request import urlopen
from geopy.geocoders import Nominatim
import math

app = Flask(__name__)


@app.route('/')
def extract_ip_lonlat():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)
    ip = data['ip']
    loc = data['loc']
    extract_address()
    haversine()
    ip_lat = loc[:7]
    ip_lon = loc[8:]
    # print(ip_lat)
    # print(ip_lon)
    return 'IP Address: ' + ip + ' Lat/Long: ' + ip_lat + ', ' + ip_lon

def extract_address():
    # AddressExtentionPattern = re.compile(r'(\b(unit|apt|apartment|ext|lot|ste|suite)\b).*$', re.UNICODE | re.IGNORECASE)
    # HashAddressExtentionPattern = re.compile(r'#.*$')
    # POBoxPattern = re.compile(r'(\b(box|pobox)\b)', re.IGNORECASE)
    # ZipCodePattern = re.compile(r'^\d{5}$|^\d{5}-?\d{4}$')
    geolocator = Nominatim(user_agent="Givelify")
    location = geolocator.geocode("2109 Tin Can Dr, Austin, TX")
    print(location.address)
    print((location.latitude, location.longitude))
    print(location.raw)
    # print(addy_lat)
    # print(addy_lon)

    return location.address


def haversine(ip_lat, ip_lon, addy_lat, addy_lon):
    # Latitude and longitude of inputs

    # Radius of the Earth
    radius = 6371  # km
    # radius = 3858.8  # mi

    lat_diff = math.radians(ip_lat - addy_lat)
    lon_diff = math.radians(ip_lon - addy_lon)

    # It's not entirely clear what "a" and "c" are in this context;
    # they may be the lengths of the sides of a spherical triangle
    a = (math.sin(lat_diff / 2) * math.sin(lat_diff / 2) +
         math.cos(math.radians(ip_lat)) * math.cos(math.radians(addy_lat)) *
         math.sin(lon_diff / 2) * math.sin(lon_diff / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    dist = radius * c

    return dist

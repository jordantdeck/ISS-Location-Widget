# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:21:00 2017

@author: Jordan Deck
"""

import requests 
import json
import time

while True:
    response = requests.get('http://api.open-notify.org/iss-now.json')
    json_data = json.loads(response.text)

    pos = json_data['iss_position']
    long = pos['longitude']
    lat = pos['latitude']
    response2 = requests.get('https://maps.googleapis.com/maps/api/staticmap?center=' + lat + ',' + long + '&zoom=5&size=400x400&maptype=satellite&key=AIzaSyDz0VunzorjaKzw0cxH_FFKEnosSc_HT_4').content

    path = 'C:/Users/Jordan/Documents/Rainmeter/Skins/ISS/isspos.png'
    file = open(path, 'wb')

    file.write(response2)
    file.close()

    time.sleep(5)
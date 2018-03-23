import os
import json
from geojson import Polygon
import time
import threading
import urllib
import urllib2
import requests
import smbus
from datetime import datetime

# Get I2C bus
bus = smbus.SMBus(1)


url = 'https://municipal.systems/v1/data?key=17876420-416a-4371-b6e5-bc3dc4b4e43f'
location = Polygon([[(
              -76.60792350769043,
              39.260552770355886
            ),
            (
              -76.60785913467407,
              39.25935238682632
            ),
            (
              -76.6075050830841,
              39.25937730849262
            ),
            (
              -76.6075050830841,
              39.259140552305034
            ),
            (
              -76.60727441310883,
              39.259148859553214
            ),
            (
              -76.60727977752686,
              39.25938561571273
            ),
            (
              -76.60671651363373,
              39.259414690975454
            ),
            (
              -76.60679161548615,
              39.260486313673724
            ),
            (
              -76.6073226928711,
              39.26046554594764
            ),
            (
              -76.6073226928711,
              39.26057353805614
            ),
            (
              -76.60792350769043,
              39.260552770355886
            )]])

if __name__ == '__main__':
        try:
                bus.write_byte(0x40, 0xF5)
                time.sleep(0.3)
                data0 = bus.read_byte(0x40)
                data1 = bus.read_byte(0x40)
                humidity = round(((data0 * 256 + data1) * 125 / 65536.0) - 6, 2)

                time.sleep(0.3)
                
                bus.write_byte(0x40, 0xF3)

                time.sleep(0.3)

                data0 = bus.read_byte(0x40)
                data1 = bus.read_byte(0x40)
        
        # Convert the data
                cTemp = round(((data0 * 256 + data1) * 175.72 / 65536.0) - 46.85, 2)
                fTemp = round(cTemp * 1.8 + 32, 2)
                while True:
                        print "Relative Humidity is : %.2f %%" %humidity
                        print "Temperature in Celsius is : %.2f C" %cTemp
                        print "Temperature in Fahrenheit is : %.2f F" %fTemp
                        date = datetime.utcnow().strftime('%m-%d %H:%M:%S')
                        id = 'Tempdemo'+ date

                        payload = {'temperature':fTemp, 'id':id}
                        #'temperature':fTemp, 'humidity':humidity, 
                        r = requests.post(url, json=payload)
                        #params='response=false'
                        print r.content
                        time.sleep(30)
                        
        except (KeyboardInterrupt, SystemExit):
                        print "\nStopping Weather Station..."
        print "Done.\nExiting."
                

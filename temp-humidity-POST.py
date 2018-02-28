import os
import json
from geojson import MultiPolygon
import time
import threading
import urllib
import urllib2
import requests
import smbus
from datetime import datetime

# Get I2C bus
bus = smbus.SMBus(1)


url = 'https://municipal.systems/v1/data?key=8908233f-2995-464c-b984-d46e9768f5df'
date = datetime.now().strftime('%m-%d %H:%M:%S')
id = 'Tempdemo1'
location = Polygon([
        [(-87.6871258020401,42.05717539690771),
(-87.68738329410552,42.056502273850455),
(-87.68767297267914,42.0565560442977),
(-87.68768906593323,42.056542103815765),
            (
              -87.68773466348648,
              42.05655006980582
            ),
            (
              -87.68775880336761,
              42.05652617183263
            ),
            (
              -87.6877212524414,
              42.056502273850455
            ),
            (
              -87.6877561211586,
              42.05639871582379
            ),
            (
              -87.68738865852356,
              42.05632503020199
            ),
            (
              -87.68724381923676,
              42.05632901321077
            ),
            (
              -87.6872009038925,
              42.0564465118571
            ),
            (
              -87.68714725971222,
              42.056432571351095
            ),
            (
              -87.6871258020401,
              42.05645049485824
            ),
            (
              -87.68711775541306,
              42.0564783758593
            ),
            (
              -87.68713921308517,
              42.056498290852566
            ),
            (
              -87.68708556890488,
              42.05664566160863
            ),
            (
              -87.68706679344177,
              42.05663968712515
            ),
            (
              -87.68702656030655,
              42.05674523625019
            ),
            (
              -87.6870533823967,
              42.05675121072371
            ),
            (
              -87.68699973821639,
              42.05689858089285
            ),
            (
              -87.68697559833527,
              42.05690654683819
            ),
            (
              -87.68694877624512,
              42.056926461697195
            ),
            (
              -87.68695950508116,
              42.05695035951975
            ),
            (
              -87.68699973821639,
              42.05695832545859
            ),
            (
              -87.6869648694992,
              42.05707980590228
            ),
            (
              -87.68707752227783,
              42.05709972070693
            ),
            (
              -87.6870533823967,
              42.05715946508347
            ),
            (
              -87.6871258020401,
              42.05717539690771
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

                        payload = {'location':location, 'id':id}
                        #'temperature':fTemp, 'humidity':humidity, 
                        r = requests.post(url, json=payload)
                        #params='response=false'
                        print r.content
                        time.sleep(10)
                        
        except (KeyboardInterrupt, SystemExit):
                        print "\nStopping Weather Station..."
        print "Done.\nExiting."
                

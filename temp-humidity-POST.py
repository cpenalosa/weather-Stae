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


url = 'https://municipal.systems/v1/data?key=keyData'
date = datetime.now().strftime('%m-%d %H:%M:%S')
id = 'Tempdemo1'
location = Polygon([[ ]])

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
                

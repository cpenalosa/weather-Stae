import os
import json
import geojson
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


url = 'https://municipal.systems/v1/data?key=fd9eb60e-d95c-424d-b87f-f0d17c56cc1f'
location = geojson.Point((-76.6067,39.2594))

if __name__ == '__main__':
        try:
        
        # Convert the data
                while True:
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
                        cTemp = round(((data0 * 256 + data1) * 175.72 / 65536.0) - 46.85, 2)
                        fTemp = round(cTemp * 1.8 + 32, 2)
                        print "Relative Humidity is : %.2f %%" %humidity
                        print "Temperature in Celsius is : %.2f C" %cTemp
                        print "Temperature in Fahrenheit is : %.2f F" %fTemp
                        date = datetime.utcnow().strftime('%m-%d %H:%M:%S')
                        id = 'Tempdemo'+ date
                        type = 'Conference Room Window'

                        payload = {'location_point':location,'temperature':fTemp,'humidity':humidity,'id':id}
                        #'location_polygon':location,  
                        r = requests.post(url, json=payload, params='response=false')
                        print r.status_code
                        time.sleep(30)
                        
        except (KeyboardInterrupt, SystemExit):
                        print "\nStopping Weather Station..."
        print "Done.\nExiting."
                

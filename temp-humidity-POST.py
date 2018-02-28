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
location = MultiPolygon([
        [(-87.68711769125002, 42.05715081151411), (-87.68736942246676, 42.05650825036051), 
        (-87.68735701725006, 42.056505014175016), (-87.68736975774289, 42.05647016293642), (-87.68769175329544, 42.056541110080595), 
        (-87.68774774440863, 42.05639921571299), (-87.68737936303785, 42.056318997373964), (-87.68737433389595, 42.05633343578093), 
        (-87.68730157897642, 42.05631700586929), (-87.6872988967674, 42.05632646551591), (-87.68724357620647, 42.056314018612184), 
        (-87.68719447339816, 42.05644074650491), (-87.68715926940484, 42.05643228262586), (-87.68708495341622, 42.056619107585895), 
        (-87.68706047825896, 42.056612884162995), (-87.68701784103575, 42.05672300474648), (-87.68704768061104, 42.05672848134914), 
        (-87.6869690331223, 42.05692806948687) (-87.68700054907822, 42.05693503968584), (-87.68695075453593, 42.05705876955612), 
        (-87.68707212449385, 42.057084160939375), (-87.68705009161465, 42.057136462179706), (-87.68711769125002, 42.05715081151411)]])

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
                

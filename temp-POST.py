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


url = 'https://municipal.systems/v1/data?key=2ebc182c-f72c-49d5-a1f6-3187cb5e7f8f'
location = geojson.Polygon([[
(
              -80.23377656936646,
              25.727986697204663
            ),
            (
              -80.23386240005493,
              25.727921456858283
            ),
            (
              -80.23389995098114,
              25.727940787335015
            ),
            (
              -80.2339830994606,
              25.7278393022971
            ),
            (
              -80.23406893014908,
              25.727769229244213
            ),
            (
              -80.23404479026794,
              25.727752315052815
            ),
            (
              -80.23412257432938,
              25.72768224194866
            ),
            (
              -80.23405820131302,
              25.727626666698743
            ),
            (
              -80.23408234119415,
              25.727614585119223
            ),
            (
              -80.23396968841553,
              25.727517932438975
            ),
            (
              -80.23395091295242,
              25.727537262981322
            ),
            (
              -80.23388385772705,
              25.727481687663648
            ),
            (
              -80.23381143808365,
              25.727542095616407
            ),
            (
              -80.23375779390335,
              25.727534846663705
            ),
            (
              -80.23370683193207,
              25.72750343453018
            ),
            (
              -80.23355931043625,
              25.727629083014477
            ),
            (
              -80.23362904787064,
              25.727694323521284
            ),
            (
              -80.23362368345259,
              25.72773298454545
            ),
            (
              -80.2335512638092,
              25.72778614343317
            ),
            (
              -80.23377656936646,
              25.727986697204663
            )

]])

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
                

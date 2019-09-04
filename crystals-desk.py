#!/usr/bin/env python

import os
import json
import geojson
import time
import threading
import urllib
import urllib2
import requests
import smbus
from datetime import datetime
from Adafruit_LED_Backpack import AlphaNum4

# Get I2C bus
bus = smbus.SMBus(1)


url = 'https://municipal.systems/v1/data?key=keyData'
location = geojson.Point((-73.99048715829849,40.744050339871116))

# Create display instance on default I2C address (0x70) and bus number.
display = AlphaNum4.AlphaNum4()

# Initialize the display. Must be called once before using the display.
display.begin()



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
                        # Clear the display buffer.
                        display.clear()
                        # Print a 4 character string to the display buffer.
                        display.print_str(message[pos:pos+4])
                        # Write the display buffer to the hardware.  This must be called to
                        # update the actual display LEDs.
                        display.write_display()
                        # Increment position. Wrap back to 0 when the end is reached.
                        pos += 1
                        if pos > len(message)-4:
                            pos = 0
                        # Delay for half a second.

                        time.sleep(0.3)

                        data0 = bus.read_byte(0x40)
                        data1 = bus.read_byte(0x40)
                        cTemp = round(((data0 * 256 + data1) * 175.72 / 65536.0) - 46.85, 2)
                        fTemp = round(cTemp * 1.8 + 32, 2)
                        print "Relative Humidity is : %.2f %%" %humidity
                        print "Temperature in Celsius is : %.2f C" %cTemp
                        print "Temperature in Fahrenheit is : %.2f F" %fTemp
                        date = datetime.utcnow().strftime('%m/%d/%y %H:%M:%S')
                        message = fTemp
                        id = 'crystal'+ date
                        type = 'Office'

                        payload = {'location':location,'temperature':fTemp,'humidity':humidity,'id':id, startedAt:date, 'type':type }
                        #'location_polygon':location,  
                        r = requests.post(url, json=payload)
                        print r.content
                        time.sleep(10)
                        
        except (KeyboardInterrupt, SystemExit):
                        print "\nStopping Weather Station..."
        print "Done.\nExiting."
                
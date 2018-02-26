import os
import json
import geojson
import time
import threading
import urllib
import urllib2
import requests
import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# SI7021 address, 0x40(64)
#		0xF5(245)	Select Relative Humidity NO HOLD master mode
bus.write_byte(0x40, 0xF5)

time.sleep(0.3)

# SI7021 address, 0x40(64)
# Read data back, 2 bytes, Humidity MSB first
data0 = bus.read_byte(0x40)
data1 = bus.read_byte(0x40)

# Convert the data
humidity = ((data0 * 256 + data1) * 125 / 65536.0) - 6

time.sleep(0.3)

# SI7021 address, 0x40(64)
#		0xF3(243)	Select temperature NO HOLD master mode
bus.write_byte(0x40, 0xF3)

time.sleep(0.3)

# SI7021 address, 0x40(64)
# Read data back, 2 bytes, Temperature MSB first
data0 = bus.read_byte(0x40)
data1 = bus.read_byte(0x40)

# Convert the data
cTemp = ((data0 * 256 + data1) * 175.72 / 65536.0) - 46.85
fTemp = cTemp * 1.8 + 32


url = 'https://municipal.systems/v1/data?key=8908233f-2995-464c-b984-d46e9768f5df'

id = 'tempdemo1'
location = geojson.Point(-87.68724, 42.05673)

if result.is_valid():
	print "Relative Humidity is : %.2f %%" %humidity
	print "Temperature in Celsius is : %.2f C" %cTemp
	print "Temperature in Fahrenheit is : %.2f F" %fTemp

    payload = {'temperature':fTemp, 'humidity':humidity, 'location':location, 'id':id}

    r = requests.post(url, json=payload) 
    # params='response=false'
    print = r.content
    time.sleep(10)

else:
    print("Error: %d" % result.error_code)
    time.sleep(10)
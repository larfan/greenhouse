
import time
import sys
#lightsensor
import statistics

##für MCP3008
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
from numpy import interp

#co2mhz19
import serial
import subprocess
import traceback

#dht_11
import Adafruit_DHT
import time



class dht_11:     #self-keyword anwenden allgemein bei classes
  humidity, temperature = Adafruit_DHT.read_retry(11, 4)

while True:
  print(dht_11.temperature)
  time.sleep(5)
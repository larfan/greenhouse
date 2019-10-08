
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

  def newmeasurments(self): ##that is a method, it belongs to the function object.
    self.temperature=Adafruit_DHT.read_retry(11, 4)[1]
    self.humidity=Adafruit_DHT.read_retry(11, 4)[0]


while True:
  sensor=dht_11()
  sensor.newmeasurments()
  print(sensor.temperature)
  print(sensor.humidity)
  time.sleep(5) 
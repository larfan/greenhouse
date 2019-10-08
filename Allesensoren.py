
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

#Hardware SPI configuration: ##das ist allgemein für MCP3008
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))




class dht_11:     #self-keyword anwenden allgemein bei classes
  humidity, temperature = Adafruit_DHT.read_retry(11, 4)

  def newmeasurments(self): ##that is a method, it belongs to the function object.
    self.temperature=Adafruit_DHT.read_retry(11, 4)[1]
    self.humidity=Adafruit_DHT.read_retry(11, 4)[0]

class lightsensors:
    data=[]
    values = [0]*8
    def medianlight(self):
      self.data=[]
      for i in range(5):      
          for i in range(8):
                # The read_adc function will get the value of the specified channel (0-7).
              self.values[i] = mcp.read_adc(i)
          for i in range(2):          #menge an sensoren
              self.data.append(self.values[i])
          time.sleep(0.5)
      # Print the ADC values.
      self.data=statistics.mean(self.data)
      self.data=round(interp(self.data, [0, 1023], [0, 100]),2) 


while True:
  sensor=dht_11()
  sensor.newmeasurments()
  print(sensor.temperature)
  print(sensor.humidity)
  time.sleep(1)
  #licht
  lichtsensor=lightsensors()
  lichtsensor.medianlight()
  print(lichtsensor.data)

  time.sleep(1) 
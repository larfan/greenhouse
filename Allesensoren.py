
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


#Hardware SPI configuration: ##das ist allgemein für MCP3008
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

#co2sensor
partial_serial_dev = 'serial0'

serial_dev = '/dev/%s' % partial_serial_dev
stop_getty = 'sudo systemctl stop serial-getty@%s.service' % partial_serial_dev
start_getty = 'sudo systemctl start serial-getty@%s.service' % partial_serial_dev

serial_settings= serial.Serial(serial_dev,
                        baudrate=9600,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        timeout=1.0)
p = subprocess.call(stop_getty, stdout=subprocess.PIPE, shell=True)
ser = serial_settings
    




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

class mh_z19:
    result=None
    s=None   #ich glaube man braucht die variablen nicht
    value={}        #
    def werte(self):
      
      ser.write(b"\xff\x01\x86\x00\x00\x00\x00\x00\x79")
      time.sleep(0.2)
      self.s=ser.read(9)
      
      if self.value is None:
        self.value={'co2 sensor nichts gelesen'}
      elif len(self.s) >= 4 and self.s[0] == 0xff and self.s[1] == 0x86:
        self.value= {'co2': self.s[2]*256 + self.s[3]}
      

while True:
  sensor=dht_11()
  sensor.newmeasurments()
  print(sensor.temperature)
  print(sensor.humidity)
  #licht
  lichtsensor=lightsensors()
  lichtsensor.medianlight()
  print(lichtsensor.data)
  #co2
  co2sensor=mh_z19()
  p = subprocess.call(stop_getty, stdout=subprocess.PIPE, shell=True)
  co2sensor.werte()
  p = subprocess.call(start_getty, stdout=subprocess.PIPE, shell=True)
  print(co2sensor.value)

  time.sleep(1) 
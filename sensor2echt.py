# /usr/bin/python3
import sys
import Adafruit_DHT
import time


humidity, temperature = Adafruit_DHT.read_retry(11, 4)

def Temp_humidity(): 
    while True:

        humidity, temperature = Adafruit_DHT.read_retry(11, 4)

        print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
        print(temperature)                      #.format ersetzt einfach 
        time.sleep(5)                           #das in den geschwungenen
                                            #Klammern. % ist veraltet
        #read_retry ist eine Funktion von Adafruit. in common.py ist
        #angegeben dass es 15* probiert mit einem abstand von 2 sek
        
Temp_humidity()
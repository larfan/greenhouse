# Simple example of reading the MCP3008 analog input channels and printing
import time
import statistics
# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
from numpy import interp

#Hardware SPI configuration: ##das ist allgemein für MCP3008
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

def lightsensor():
    # Read all the ADC channel values in a list.
    data=[]
    values = [0]*8
    for i in range(5):
        for i in range(8):
              # The read_adc function will get the value of the specified channel (0-7).
            values[i] = mcp.read_adc(i)
        for i in range(4):          #menge an sensoren
            data.append(values[i])
        time.sleep(0.5)
    # Print the ADC values.
    x=statistics.mean(data)
    x=round(interp(x, [0, 1023], [0, 100]),2)   ##interp wandel 0-1023 skal in 0-100 skala um
    print(data)
    print(x)
    print('\n')
    # Pause for half a second.
    return x
    time.sleep(2)
while True:
    print(lightsensor())
    time.sleep(2)
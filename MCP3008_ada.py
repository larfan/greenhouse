# Simple example of reading the MCP3008 analog input channels and printing
import time
import statistics
# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


print('Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
print('-' * 57)    
# Main program loop.
while True:
    # Read all the ADC channel values in a list.
    data=[]
    values = [0]*8
    for i in range(5):
          ##dass man sozusagen eine list macht
        for i in range(8):
              # The read_adc function will get the value of the specified channel (0-7).
            values[i] = mcp.read_adc(i)
        for i in range(2):
            data.append(values[i])
        time.sleep(0.5)
    # Print the ADC values.
    x=statistics.mean(data)
    print(data)
    print(x)
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
    print('\n')
    # Pause for half a second.
    time.sleep(2)


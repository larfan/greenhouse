#!/usr/bin/python3

import serial, os, time, sys, datetime
#Function to calculate MH-Z19 crc according to datasheet
def crc8(a):
    crc=0x00
    count=1
    b=bytearray(a)          #einfach array mit x bis 256
    while count<8:
        crc+=b[count]       #meint crc=crc#b
        count=count+1
    #Truncate to 8 bit
    crc%=256                # schreibt den rest crc zu, glaube ich
    #Invert number with xor
    crc=~crc&0xFF
    crc+=1
    return crc

    # try to open serial port
    
port='/dev/ttyS0'
sys.stderr.write('Trying port %s' % port)
while True:
    # try to read a line of data from the serial port and parse, parse meint eigentlich nur aufteilen in mehrere s 
    with serial.Serial(port, 9600, timeout=2.0) as ser:
        print('hello')
        
        # loop will exit with Ctrl-C, which raises a KeyboardInterrupt
        while True:
            print('hello')
            #Send "read value" command to MH-Z19 sensor
            result=ser.write(b"\xff\x01\x86\x00\x00\x00\x00\x00\x79")
            time.sleep(0.1)
            s=ser.read(9)       #read 9 bytes(von pyserialdocumentation)
            print(s)
            z=bytearray(s)
            crc=crc8(s)
            #Calculate crc
            if crc != z[8]:     #8 byte oder 9 is glaube ich die summe die vom sensor kommt
                sys.stderr.write('CRC error calculated %d bytes= %d:%d:%d:%d:%d:%d:%d:%d crc= %dn' % (crc, z[0],z[1],z[2],z[3],z[4],z[5],z[6],z[7],z[8]))
            else:       
                if s[0] == "xff" and s[1] == "x86":
                    print ("co2=", ord(s[2])*256 + ord(s[3])) #ascii tabelle-->umwandeln in ziffer
            co2value=ord(s[2])*256 + ord(s[3])
            now=time.ctime()
            parsed=time.strptime(now)
            #Sample every minute, synced to local time
            t=datetime.datetime.now()
            sleeptime=60-t.second
            time.sleep(sleeptime)
#except Exception as e:
 #   print("da ist ein fehler")
  #  ser.close()
#except KeyboardInterrupt as e:
  
 #   ser.close()
   

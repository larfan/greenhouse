import serial
import time
import subprocess
import traceback
import struct
import platform
import sys





partial_serial_dev = 'serial0'

serial_dev = '/dev/%s' % partial_serial_dev
stop_getty = 'sudo systemctl stop serial-getty@%s.service' % partial_serial_dev
start_getty = 'sudo systemctl start serial-getty@%s.service' % partial_serial_dev


def connect_serial():
  return serial.Serial(serial_dev,
                        baudrate=9600,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        timeout=1.0)

def mh_z19():
  try:
    p = subprocess.call(stop_getty, stdout=subprocess.PIPE, shell=True)
    ser = connect_serial()
    result=ser.write(b"\xff\x01\x86\x00\x00\x00\x00\x00\x79")
    s=ser.read(9)
    if len(s) >= 4 and s[0] == 0xff and s[1] == 0x86:
        value= {'co2': s[2]*256 + s[3]}
        if value is not None:
            return value
        else:
            print('kein wert')
    p = subprocess.call(start_getty, stdout=subprocess.PIPE, shell=True)
  except:
    traceback.print_exc()




if __name__ == '__main__':
    value = read()
    print('test')
    print(mh_z19())
    

sys.exit(0)
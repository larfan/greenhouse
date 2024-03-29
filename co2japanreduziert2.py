import serial
import time
import subprocess
import traceback
import getrpimodel
import struct
import platform
import argparse
import sys
import json
import os.path

# setting
version = "0.3.9"
pimodel        = getrpimodel.model
pimodel_strict = getrpimodel.model_strict()


partial_serial_dev = 'serial0'

serial_dev = '/dev/%s' % partial_serial_dev
stop_getty = 'sudo systemctl stop serial-getty@%s.service' % partial_serial_dev
start_getty = 'sudo systemctl start serial-getty@%s.service' % partial_serial_dev

# major version of running python
p_ver = platform.python_version_tuple()[0]

def set_serialdevice(serialdevicename):
  global serial_dev
  serial_dev = serialdevicename

def connect_serial():
  return serial.Serial(serial_dev,
                        baudrate=9600,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        timeout=1.0)

def mh_z19():
  try:
    ser = connect_serial()
    while 1:
      result=ser.write(b"\xff\x01\x86\x00\x00\x00\x00\x00\x79")
      s=ser.read(9)

      if p_ver == '2':
        if len(s) >= 4 and s[0] == "\xff" and s[1] == "\x86":
          return {'co2': ord(s[2])*256 + ord(s[3])}
        break
      else:
        if len(s) >= 4 and s[0] == 0xff and s[1] == 0x86:
          return {'co2': s[2]*256 + s[3]}
        break
  except:
     traceback.print_exc()##sollte sagen wo ein problem ist wenn eines das ist

def read():
  p = subprocess.call(stop_getty, stdout=subprocess.PIPE, shell=True) ###das ist dass es das im hintergrund zumacht
  result = mh_z19()                                                   ###Shell True ist dafür dass er die shell benutzen darf
  p = subprocess.call(start_getty, stdout=subprocess.PIPE, shell=True)###start-getty ist einfach der normale command
  if result is not None:
    return result



if __name__ == "__main__":
    value = read()
    print('test')
    print (json.dumps(value))

sys.exit(0)##sollte beim rausgehen aus dem Prgramm zum Beispiel einfach nur sagen dass es eben richtig rausgegangen ist( man könnte auch einfach irgendeinen string reintun(glaube ich))
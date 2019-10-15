import time
import urllib.request
a=7
b=10


while True:
    a+=1
    b=b/0.5
    urllib.request.urlopen('https://api.thingspeak.com/update?api_key=GZMU3A1FWMNELXG7&field1=0'+str(a))
    time.sleep(15)
    urllib.request.urlopen('https://api.thingspeak.com/update?api_key=GZMU3A1FWMNELXG7&field2=0'+str(b))
    print('pushed a as'+ str(a))
    time.sleep(15)

#anmerkung :wenn du das in ein with statement reintun willst:
#das ist eigentlich nicht für while schleifen gedacht
#da es darum geht zum beispiel einen Error aufzuzeichen, wie bei try statement  
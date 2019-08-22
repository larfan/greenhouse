import RPi.GPIO as GPIO
import time
import datetime
import signal
GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern

x = datetime.datetime.now()

while True: 
    try:
        logfile=open('logrichtig.txt', 'a')
        logfile.write('Bewässerung:'+x.strftime("%c")+'\n')
        RELAIS_1_GPIO = 17
        GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # an
        print(x.strftime("%c"))
        time.sleep(5)
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # aus
        GPIO.cleanup()
        logfile.close()
        time.sleep(30)
    except KeyboardInterrupt:
        print



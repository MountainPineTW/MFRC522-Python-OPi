import OPi.GPIO as GPIO
from time import sleep
import sys
from mfrc522 import OrangePiZero2MFRC522

reader = OrangePiZero2MFRC522()

try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id, text))
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise

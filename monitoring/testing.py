import RPi.GPIO as GPIO
import datetime
geigerChannel = 4  # пин для гейгера


# устанвока пина
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
#GPIO.add_event_detect(7, GPIO.FALLING, callback=on_event)
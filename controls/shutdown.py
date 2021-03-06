#!/usr/bin/env python
#
# :Author: PB
# :Date: 17 Aug 2015
# :License: GPL v2
#
# holds code for shutdown button
# should get run in /etc/rc.local
#
import os
import time
import json
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
BUTTON_PIN = 17  # pin 11

def handle_INT(signal, frame):
    print("SIGINT caught, exiting gracefully.")
    shutdown()

def handle_TERM(signal, frame):
    print("SIGTERM caught, exiting gracefully.")
    shutdown()

def shutdown(channel):
    log_rec = {'timestamp': int(time.time()),
               'message': 'shutting down by button'}
    with open("/home/pi/var/log/status.log", 'a') as logFH:
        logFH.write("%s\n" % json.dumps(log_rec))
    os.system("sudo shutdown -h now")

def startup():
    log_rec = {'timestamp': int(time.time()),
               'message': 'booted up, watching shutdown button'}
    with open("/home/pi/var/log/status.log", 'a') as logFH:
        logFH.write("%s\n" % json.dumps(log_rec))


if __name__ == "__main__":
    startup()
    poll_interval = 1
    GPIO.setup(BUTTON_PIN, GPIO.IN, initial=GPIO.LOW)
    GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING,
        callback=shutdown, bouncetime=500)

    while True:
        time.sleep(poll_interval) # possible to go slower?

# end.

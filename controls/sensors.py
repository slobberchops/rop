#!/usr/bin/python

import time, signal, sys
sys.path.append("/home/pi/Adafruit-Raspberry-Pi-Python-Code/Adafruit_ADS1x15")
from Adafruit_ADS1x15 import ADS1x15

def signal_handler(signal, frame):
        #print 'You pressed Ctrl+C!'
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
print 'Press Ctrl+C to exit'

ADS1015 = 0x00  # 12-bit ADC

# Initialise the ADC using the default mode (use default I2C address)
# Set this to ADS1015 or ADS1115 depending on the ADC you are using!
adc = ADS1x15(ic=ADS1015)

V_per_mV_read = 63.69
A_per_mV_read = 18.3

while True:
    # Read channels 2 and 3 in single-ended mode, at +/-4.096V and 250sps
    volts_single = [
                adc.readADCSingleEnded(0, 4096, 250)/1000.0,
                adc.readADCSingleEnded(1, 4096, 250)/1000.0,
                adc.readADCSingleEnded(2, 4096, 250)/1000.0
                ]


    # print "v0=%s, v1=%s, v2=%s" % tuple(volts_single)
    meas_V = round((volts_single[0]/V_per_mV_read)*1000, 2)
    meas_A = round((volts_single[1]/A_per_mV_read), 2)
    meas_D = round( volts_single[2] / (5.3/512.0) , 0)
    print "time: %s. measured A=%s, measured V=%s, measured D=%s" % (
        int(time.time()), meas_A, meas_V, meas_D)

    time.sleep(1)
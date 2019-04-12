#! /usr/bin/python2

import time
import sys


RATE_3 = 0.05
RATE_2 = 0.034
RATE_1 = 0.09

EMULATE_HX711=False

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

def cleanAndExit():
    print "Cleaning..."

    if not EMULATE_HX711:
        GPIO.cleanup()
        
    print "Bye!"
    sys.exit()

hx = HX711(5, 6)

if int(sys.argv[1]) == 1:
    rate = RATE_1
elif int(sys.argv[1]) == 2:
    rate = RATE_2
else:
    rate = RATE_3
# I've found out that, for some reason, the order of the bytes is not always the same between versions of python, numpy and the hx711 itself.
# Still need to figure out why does it change.
# If you're experiencing super random values, change these values to MSB or LSB until to get more stable values.
# There is some code below to debug and log the order of the bits and the bytes.
# The first parameter is the order in which the bytes are used to build the "long" value.
# The second paramter is the order of the bits inside each byte.
# According to the HX711 Datasheet, the second parameter is MSB so you shouldn't need to modify it.
hx.set_reading_format("MSB", "MSB")

# HOW TO CALCULATE THE REFFERENCE UNIT
# To set the reference unit to 1. Put 1kg on your sensor or anything you have and know exactly how much it weights.
# In this case, 92 is 1 gram because, with 1 as a reference unit I got numbers near 0 without any weight
# and I got numbers around 184000 when I added 2kg. So, according to the rule of thirds:
# If 2000 grams is 184000 then 1000 grams is 184000 / 2000 = 92.
#hx.set_reference_unit(113)
#hx.set_reference_unit(653)

hx.reset()
#hx.tare()

# to use both channels, you'll need to tare them both
#hx.tare_A()
#hx.tare_B()

val = hx.get_weight(5)
print "Weight: ", (val / 653), "g"
print "Price: Rs. ", (val / 653) * rate
cleanAndExit()

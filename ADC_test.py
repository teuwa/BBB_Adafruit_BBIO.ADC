import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P8_10", GPIO.OUT)
GPIO.output("P8_10", GPIO.HIGH)
GPIO.cleanup()

ADC.setup()
value = ADC.read("P9_40")
print value

# connect P8_10 and P9_40, adc should return high value
# connect gnd and P9_40, adc should return low value

# root@beaglebone:~/tomxue# python adc_test.py
# 0.999444425106
# root@beaglebone:~/tomxue# python adc_test.py
# 0.0

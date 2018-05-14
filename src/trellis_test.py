import Adafruit_GPIO.I2C as I2C
import time
import Adafruit_Trellis
import threading
import RPi.GPIO as GPIO

def button_isr(channel):
	print("button press - pin ", channel)

matrix0 = Adafruit_Trellis.Adafruit_Trellis()
trellis = Adafruit_Trellis.Adafruit_TrellisSet(matrix0)
I2C_BUS = 1
trellis.begin((0x70, I2C_BUS))

PIN_NO = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NO, GPIO.IN)
GPIO.add_event_detect(PIN_NO, GPIO.RISING, callback=button_isr, bouncetime=200)


try:
	while True:
		pass

except KeyboardInterrupt:
	print("KBI")

finally:
	GPIO.cleanup()



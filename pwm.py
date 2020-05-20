import RPi.GPIO as GPIO
import time

led = 21
trigg_pin = 18
echo_pin = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(led, GPIO.OUT)
GPIO.setup(trigg_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

GPIO.output(trigg_pin, False)
print "Waiting for sensor to settle."
time.sleep(2)

pwm = GPIO.PWM(led, 25)
pwm.start(0)

try:
	while(True):
		GPIO.output(trigg_pin, True)
		time.sleep(0.00001)
		GPIO.output(trigg_pin, False)

		while GPIO.input(echo_pin)==0:
			pulse_start = time.time()

		while GPIO.input(echo_pin)==1:
	                pulse_stop = time.time()

		pulse_duration = pulse_stop - pulse_start

		distance = pulse_duration * 17150
		distance = round(distance, 2)
		time.sleep(1)

		if distance <= 25:
			ledBlink = 25 - distance


		else:
			ledBlink = 0

		pwm.ChangeDutyCycle(ledBlink)
		time.sleep(1)

		print "Distance : ", distance
		print "\n"

except KeyboardInterrupt:
	pass

pwm.stop()
GPIO.cleanup()

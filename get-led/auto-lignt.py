import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
state = 1
signal = 6
GPIO.setup(signal, GPIO.IN)
while True:
    if GPIO.input(signal):
        state = not state
        GPIO.output(led, state)
import Adafruit_BBIO.GPIO as GPIO

pin = 'P8_7'
GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin,GPIO.HIGH)

# High side switch vezérlése helyes logikával
com = input()
while com != 'x':
    if com == 'off':
        GPIO.output(pin,GPIO.HIGH)
    if com == 'on':
        GPIO.output(pin,GPIO.LOW)
    com = input()
        


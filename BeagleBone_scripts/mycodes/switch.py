import Adafruit_BBIO.GPIO as GPIO

pin = 'P8_7'
GPIO.setup(pin,GPIO.OUT)


com = input()
while com != 'x':
    if com == 'on':
        GPIO.output(pin,GPIO.HIGH)
    if com == 'off':
        GPIO.output(pin,GPIO.LOW)
    com = input()
        


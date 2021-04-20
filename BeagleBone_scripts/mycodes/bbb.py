import Adafruit_BBIO.UART as UART
import serial, io
import Adafruit_BBIO.GPIO as GPIO

switch_pin = 'P8_7'
GPIO.setup(switch_pin,GPIO.OUT)
GPIO.output(switch_pin,GPIO.HIGH)

UART.setup('UART1')
esp32_serial = serial.Serial(port='/dev/ttyO1', baudrate=115200, timeout=2, xonxoff=False)

def main():
    answer = send_command("get temperature")
    print(answer)
    cleanUp()


def send_command(command):
    esp32_serial.write(command.encode())
    if (esp32_serial.isOpen()):
        line = esp32_serial.readline()
        return line
    return "Serial is not open."
    
    
def esp32_switch(command):
    if command == 'off':
        GPIO.output(switch_pin,GPIO.HIGH)
        return True
    if command == 'on':
        GPIO.output(switch_pin,GPIO.LOW)
        return True
    return False
    

def cleanUp():
    GPIO.cleanup()
    #UART.cleanup()


main()
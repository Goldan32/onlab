import Adafruit_BBIO.UART as UART
import serial

UART.setup('UART1')

ser = serial.Serial(port='/dev/ttyO1', baudrate=115200)
ser.write(b'get temperature')

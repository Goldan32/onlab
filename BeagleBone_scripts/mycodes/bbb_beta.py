import Adafruit_BBIO.UART as UART
import serial
import io
import time

UART.setup('UART1')

ser = serial.Serial(port='/dev/ttyO1', baudrate=115200, timeout=2, xonxoff=False)

command = "get humidity"
ser.write(command.encode())
#ser.flushInput()
if (ser.isOpen()):
    line = ser.readline()
print(line)


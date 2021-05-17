import Adafruit_BBIO.UART as UART
import serial, io
import Adafruit_BBIO.GPIO as GPIO
from datetime import datetime
import PyGnuplot as gp, numpy as np
import time

switch_pin = 'P8_7'
GPIO.setup(switch_pin,GPIO.OUT)
GPIO.output(switch_pin,GPIO.HIGH)

UART.setup('UART1')
esp32_serial = serial.Serial(port='/dev/ttyO1', baudrate=115200, timeout=2, xonxoff=False)

current_hour = 'unknown'

def main():
    while (True):
        data_process('temperature')
        time.sleep(29)
        data_process('humidity')
        time.sleep(29)
    

def send_command(command):
    esp32_serial.write(command.encode())
    if (esp32_serial.isOpen()):
        line = esp32_serial.readline()
        return line.decode()
    return "Serial is not open."
    
    
def esp32_switch(command):
    if command == 'off':
        GPIO.output(switch_pin,GPIO.HIGH)
        return True
    if command == 'on':
        GPIO.output(switch_pin,GPIO.LOW)
        return True
    return False
    
    
def data_process(data_type):
    
    global current_hour
    now = datetime.now()
    answer = send_command('get ' + data_type)
    
    if (current_hour != str(now.strftime('%H'))):
        current_hour = str(now.strftime('%H'))
        f_hour_name = str(data_type) + '_hour.txt'
        f_hour = open((f_hour_name), 'a')
        f_hour.write(now.strftime('%s') + ' ' + str(answer) + '\n')
        plot_data(f_hour_name, data_type + '_hour_plot.png', data_type, 24)
        f_hour.close()
    
    f_name = str(data_type) + '.txt'
    f = open(f_name, 'a')
    f.write(now.strftime('%s') + ' ' + str(answer) + '\n')
    plot_data(f_name, data_type + '_plot.png', data_type, 2)


def plot_data(data_filename, output_filename, data_type, hours):
    gp.c('set term "png"')
    gp.c('set output "' + output_filename + '"')
    gp.c('set title "' + data_type.capitalize() + ' in the last ' + str(hours) + ' hour(s)"')
    gp.c('set xdata time')
    gp.c('set grid')
    gp.c('set xlabel "Time"')
    gp.c('set ylabel "' + data_type.capitalize() + '"')
    gp.c('set timefmt "%s"')
    gp.c('set format x "%H:%M"')
    #gp.c('set xtics 108000')
    gp.c('set autoscale y')
    gp.c('set xtics rotate by 300')
    gp.c('plot "< tail -n 120 ' + data_filename + '" using 1:2 notitle lt rgb "red" smooth unique w lp')
    


def cleanUp():
    GPIO.cleanup()
    #UART.cleanup()


main()
import PyGnuplot as gp, numpy as np
from datetime import datetime


#now = datetime.now()
#f = open('temperature.txt', 'a')
#f.write(now.strftime('%H:%M') + ' ' + str(22.5) + '\n')


fig = 'myfig'
output_filename = fig + '.png'
data_filename = 'temperature.txt'

gp.c('set term "png"')
gp.c('set output "' + output_filename + '"')
gp.c('set xdata time')
gp.c('set timefmt "%H:%M"')
gp.c('set format x "%H:%M"')
gp.c('set yrange [18:25]')
gp.c('set xtics rotate by 300')
gp.c('plot "< tail -n 24 ' + data_filename + '" using 1:2 notitle lt rgb "red" w lp')
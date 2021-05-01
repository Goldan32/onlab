import PyGnuplot as gp, numpy as np
from datetime import datetime


#now = datetime.now()
#f = open('temperature.txt', 'a')
#f.write(now.strftime('%H:%M') + ' ' + str(22.5) + '\n')

gp.c('set term "png"')
gp.c('set output "myfig.png"')
gp.c('set xdata time')
gp.c('set timefmt "%H:%M"')
gp.c('set format x "%H:%M"')
gp.c('set yrange [18:25]')
gp.c('set xtics rotate by 300')
gp.c('plot "< tail -n 6 temperature.txt" using 1:2 lt rgb "red" w lp')
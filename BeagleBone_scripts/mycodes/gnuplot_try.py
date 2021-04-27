import PyGnuplot as gp, numpy as np


gp.c('set term "png"')
gp.c('set output "myfig.png"')
gp.c('plot sin(x)')
#gp.pdf('myfigure.pdf')
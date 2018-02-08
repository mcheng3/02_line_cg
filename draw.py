from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    i=0
    while i<500:
        plot( screen, color, i, i)
        i += 1

from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    a = y1 - y0
    b = x0 - x1
    d = 2*a + b
    if a>0 and -b>0 and -b >= a:
        while x<=x1:
            plot( screen, color, x, y)
            if d > 0:
                y += 1
                d += 2*b
            x += 1
            d += 2*a
    elif a>0 and -b> 0 and -b < a:
        while false:
            pass
    

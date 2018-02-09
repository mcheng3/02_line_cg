from display import *

def draw_line(x0,y0,x1,y1,screen,color):
    if x0<x1:
        x = x0
    else:
        x = x1
        x1 = x0
        x0 = x
    if y0 < y1:
        y = y0
    else:
        y = y1
        y1 = y0
        y0 = y
    a = y1 - y0
    b = x0 - x1
    d = 2*a + b
    print 'a: ' + str(a)
    print '-b: ' + str(-b)
    
    if -b >= a:
        print "octet I"
        while x<=x1:
            plot( screen, color, x, y)
            if d > 0:
                y += 1
                d += 2*b
            x += 1
            d += 2*a
    elif -b < a:
        print "octet II"
        while y<=y1:
            plot( screen, color, x, y)
            if d < 0:
                x += 1
                d += 2*a
            y += 1
            d += 2*b
    elif b < a:
        print "octet III"
        while y<=y1:
            plot( screen, color, x, y)
            if d > 0:
                x -= 1
                d -= 2*a
            y += 1
            d += 2*b
    elif b >= a:
        print "octet IV"
        while x>=x1:
            plot( screen, color, x, y)
            if d < 0:
                y += 1
                d += 2*b
            x -= 1
            d -= 2*a

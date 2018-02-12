from display import *
import math

def draw_line(x0,y0,x1,y1,screen,color):
    c = True
    x=x0
    y=y0
    
    if x0 > x1:       
        c = False
    if y0 > y1:
       c = c == False
    if x0 > x1 and y0 > y1 or x0 <= x1 and y0 > y1:
        #print "swapping"
        x = x1
        x1 = x0
        x0 = x
        y = y1
        y1 = y0
        y0 = y


    a = y1 - y0
    b = x0 - x1
    d = 2*a + b
    #print 'a: ' + str(a)
    #print '-b: ' + str(-b)
    #print "c: " + str(c)
    if c and math.fabs(b) >= math.fabs(a):
        print "octet I"
        while x<=x1:
            plot( screen, color, x, y)
            if d > 0:
                y += 1
                d += 2*b
            x += 1
            d += 2*a
    elif c and math.fabs(b) < math.fabs(a):
        print "octet II"
        while y<=y1:
            plot( screen, color, x, y)
            if d < 0:
                x += 1
                d += 2*a
            y += 1
            d += 2*b
    elif not c and math.fabs(b) < math.fabs(a):
        print "octet III"
        print "x: " + str(x) + "  y: " + str(y) + "  d: " + str(d)  + " " + str(y1)
        while y<=y1:
            #print "x: " + str(x) + "  y: " + str(y) + "  d: " + str(d) 
            plot( screen, color, x, y)
            if d > 0:
                x -= 1
                d -= 2*a
            y += 1
            d += 2*b
    elif not c and math.fabs(b) >= math.fabs(a):
        print "octet IV"
        #print "x: " + str(x) + "  y: " + str(y) + "  d: " + str(d) 
        while x>=x1:
            plot( screen, color, x, y)
            if d < 0:
                y += 1
                d += 2*b
            x -= 1
            d -= 2*a

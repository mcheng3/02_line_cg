from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(0,0,500,250,screen,[255,0,255])
draw_line(0,0,250,500,screen,color)
draw_line(500,0,250,500,screen,[0,0,255])
draw_line(500,0,0,250,screen,[255,255,0])
#draw_line(500, 0, 400, 500, screen, [255,255,0])
#draw_line(500, 0, 0, 10, screen, [255, 255, 255])
#draw_line(50, 500, 0, 100, screen, [255,255,100])
display(screen)
save_extension(screen, 'img.png')

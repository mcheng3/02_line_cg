from display import *
from draw import *

screen = new_screen()


draw_line(0,0,500,250,screen,[255,0,0])
draw_line(0,0,250,500,screen,[255,75,0])
draw_line(500,0,250,500,screen,[255,255,0])
draw_line(500,0,0,250,screen,[0,255,0])
draw_line(500, 500, 0, 250, screen, [0,255,255])
draw_line(500, 500, 250, 0, screen, [0,0,255])
draw_line(0, 500, 250, 0, screen, [145,0,255])
draw_line(0, 500, 500, 250, screen, [255,0,255])
display(screen)
save_extension(screen, 'img.png')

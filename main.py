from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(0, 0, 500, 250, screen, color)
display(screen)
save_extension(screen, 'img.png')

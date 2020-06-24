import pygame_geometry as pgg
from pygame_geometry.abstract import *
from pygame_geometry.context import Context
from pygame_geometry import colors as cl

context = Context("title") # create a context similar to a pygame surface

p1 = Point(2,2)
p2 = Point(3,2, color=cl.BLUE)
r = Rectangle(50, 50, 100, 200)

# main game loop
while context.open:
    # clear the window
    context.clear()
    # check quit event (empty pygame event buffer by doing so)
    context.check() 

    # update objects
    p1.rotate()
    r.move(1, 0)

    # show objects
    p1.show(context)
    p2.show(context)
    r.show(context)

    # flip the screen
    context.flip()

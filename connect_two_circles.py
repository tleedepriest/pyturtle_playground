import sys
from typing import Union
from utils import setup, save_eps_file
from pyturtle.shapes.arc import Arc
from pyturtle.shapes.circle import Circle

def connect_two_circles_top_bottom(top_circle:Union[Arc, Circle], bottom_circle:Union[Arc, Circle], turtle):
    """
    connects two circles...does NOT draw the circles but only
    creates the connection
    """
    coords_bottom = bottom_circle.coordinates
    coords_top = top_circle.coordinates

    for i in range(0, len(coords_top)-len(coords_top)//2, len(coords_top)//20):
        # connect first half of coordinates of bottom circle
        # to the last half of coordinates to top circle
        turtle.penup()
        turtle.goto(coords_bottom[i].x, coords_bottom[i].y)
        turtle.pendown()
        turtle.goto(coords_top[-i].x, coords_top[-i].y)


def main(filename=None):
    turtle = setup()
    bottom_circle = Arc(
        radius=10,
        num_coordinates=100,
        start_angle=0,
        end_angle=360,
        center = (0, -50),
    )
    top_circle = Arc(
        radius=10,
        num_coordinates=100,
        start_angle=0,
        end_angle=360,
        center=(0, 0),
    )
    bottom_circle.draw(turtle)
    top_circle.draw(turtle)
    connect_two_circles_top_bottom(top_circle, bottom_circle, turtle)
    if filename is not None:
        save_eps_file(filename)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()

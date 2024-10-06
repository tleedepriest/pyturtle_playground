import sys
from typing import Union
from math import cos, sin, radians
from utils import setup, save_eps_file
from pyturtle.shapes.arc import Arc
from pyturtle.shapes.circle import Circle
from pyturtle.shapes.line import Line

def draw_inscribed_triangle():
    # Set the precision for Decimal calculations
    t = setup()
    # Create and draw a circle
    radius = 100
    circle_center = (0, 0)
    circle = Circle(radius=radius, center=circle_center, num_coordinates=36)
    circle.draw(t)

    # Calculate vertices for the triangle
    angles = [90, 210, 330]  # Angles for an equilateral triangle
    triangle_vertices = [
        (circle_center[0] + radius * cos(radians(angle)),
         circle_center[1] + radius * sin(radians(angle)))
        for angle in angles
    ]

    # Create and draw lines for the triangle
    for i in range(len(triangle_vertices)):
        start = triangle_vertices[i]
        end = triangle_vertices[(i + 1) % len(triangle_vertices)]  # Wrap around to the first vertex
        line = Line(start=start, end=end)
        line.draw(t)


# Run the drawing function
draw_inscribed_triangle()

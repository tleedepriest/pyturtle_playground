"""
utility functions commonly used
"""
import turtle
from datetime import datetime
from turtle import Screen, Turtle


def setup(x_screen_size=300, y_screen_size=300):
    """
    common setup
    returns Turtle() and Screen() object
    """
    wn = Screen()
    wn.setup(x_screen_size, y_screen_size)
    wn.clear()
    turtle = Turtle()
    turtle.hideturtle()
    turtle.speed(0)
    return turtle

def save_eps_file(filename: str):
    """
    turtle: Turtle object
    filename: the complete path to file minus the extension
    """

    now = datetime.today().strftime("%Y-%m-%d-%H%M%S")
    turtle.getcanvas().postscript(
        file=f"{filename}_{now}.eps"
    )

# Draws an S, which is the first letter of my first name.
import turtle

def drawS(theTurtle):
    """Moves the turtle to draw an S"""
    theTurtle.backward(100)
    theTurtle.right(90)
    theTurtle.forward(75)
    theTurtle.left(90)
    theTurtle.forward(100)
    theTurtle.right(90)
    theTurtle.forward(75)
    theTurtle.right(90)
    theTurtle.forward(100)

# Creates the first turtle and makes it draw an S.
stephen = turtle.Turtle()
drawS(stephen)

# Creates a second turtle, shifts its position to the right, then draws an S.
peter = turtle.Turtle()
peter.penup()
peter.setpos(250, 0)
peter.pendown()
drawS(peter)

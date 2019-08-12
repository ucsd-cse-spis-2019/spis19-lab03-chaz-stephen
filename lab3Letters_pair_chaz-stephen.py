# Question 1: The anonymous turtle is the defeault turtle given to the user when they import the turtle package; it does not need to be called upon as it shows up by default. 

# Question 2: turtle is the name of the package, and Turtle() is the function name that creates a new turtle. 

# Question 3: myTurtle.setpos(0, 100)

import turtle 

def drawS(theTurtle, size):
    """Moves the turtle to draw an S"""
    theTurtle.backward(100 + size)
    theTurtle.right(90)
    theTurtle.forward(75 + size)
    theTurtle.left(90)
    theTurtle.forward(100 + size)
    theTurtle.right(90)
    theTurtle.forward(75 + size)
    theTurtle.right(90)
    theTurtle.forward(100 + size)

# Creates the first turtle and makes it draw an S.
stephen = turtle.Turtle()
drawS(stephen, 20)

# Creates a second turtle, shifts its position to the right, then draws an S.
peter = turtle.Turtle()
peter.penup()
peter.setpos(250, 0)
peter.pendown()
drawS(peter, 30)

k = input("press close to exit")

#This code will draw the first initial of my first name on a screen

import turtle

def drawPicture(theTurtle):
    ''' Draw a simple picture using a turtle '''
    theTurtle.left(180)
    theTurtle.forward(100)
    theTurtle.right(45)
    theTurtle.forward(50)
    theTurtle.right(45)
    theTurtle.forward(100)
    theTurtle.right(45)
    theTurtle.forward(50)
    theTurtle.right(45)
    theTurtle.forward(100)
    
    

myTurtle = turtle.Turtle() # Create a new Turtle object
myTurtle.speed(1)
drawPicture(myTurtle)   # make the new Turtle draw the shape

#turtle1 = turtle.Turtle()
#turtle2 = turtle.Turtle()
#turtle1.setpos(-50, -50)
#turtle2.setpos(200, 100)
#turtle1.forward(100)
#turtle2.left(90)
#turtle2.forward(100)

k=input("press close to exit") 

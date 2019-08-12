#this code will draw the first letter of my first name onscreen

import turtle

def drawPicture(theTurtle):
    ''' Draw a simple picture using a turtle '''
    theTurtle.forward(80)
    theTurtle.left(30)
    theTurtle.forward(100)
    theTurtle.left(75)
    theTurtle.forward(100)
    theTurtle.left(100)
    theTurtle.forward(100)
    theTurtle.left(120)    

myTurtle = turtle.Turtle()  # Create a new Turtle object
drawPicture(myTurtle)   # make the new Turtle draw the shape

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle1.setpos(-50, -50)
turtle2.setpos(200, 100)
turtle1.forward(100)
turtle2.left(90)
turtle2.forward(100)

k=input("press close to exit") 

"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.pencolor('red')
tina.forward(80)# Use tina.forward() and tina.left() to draw a triangle
tina.left(90)# Make each side of the triangle a different color with 
tina.pencolor('blue')
tina.forward(80)
tina.left(135)
tina.pencolor('green')
tina.forward(115)# tina.pencolor()

... # Your code here

turtle.exitonclick()                    # Close the window when we click on it

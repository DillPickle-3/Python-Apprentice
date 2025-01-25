"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

tina.pencolor('red')
tina.forward(110)
tina.left(30)
tina.pencolor('blue')
tina.forward(80)
tina.left(75)
tina.pencolor('green')
tina.forward(80)
tina.left(80)
tina.pencolor('black')
tina.forward(80)
tina.left(50)
tina.pencolor('purple')
tina.forward(135)
tina.left(30)



... # Your code here

turtle.exitonclick()                    # Close the window when we click on it

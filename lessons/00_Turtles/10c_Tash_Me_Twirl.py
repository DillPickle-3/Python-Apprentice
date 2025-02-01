
""" Tash Me with a Twirl
 
Update your Tash Me Click program ( copy your old program here )
so the moustache will twirl when you click on it. 

Hint: See 08a_More Turtle Programs, section 'Click on the Turtle'
"""

... # Your code here


import turtle



def set_background_image(window, image_name):
    """Set the background image of the turtle window to the image with the given name."""

    from pathlib import Path
    from PIL import Image


    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

# Set up the screen
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

tina = turtle.Turtle()   


screen = turtle.Screen()                # Get the screen that tina is on
set_background_image(screen, "emoji.png")

def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

set_turtle_image(turtle, "moustache2.gif")
turtle.penup
turtle.goto(-0, 0)


def screen_clicked(x, y):
    """Print the x and y coordinates of the screen when clicked.
    and make the turtle move to the clicked location."""

    print('You pressed: x=' + str(x) + ', y=' + str(y))
    turtle.penup()
    turtle.goto(x, y)
  
screen.onclick(screen_clicked)

def turtle_clicked(t, x, y):


    
    for i in range(0,360, 20): # Full circle, 20 degrees at a time
        turtle.tilt(20) # Tilt the turtle 20 degrees


# Connect the turtle to the turtle_clicked function
turtle.onclick(lambda x, y, t=turtle: turtle_clicked(t, x, y))

turtle.done() 



turtle.exitonclick()      

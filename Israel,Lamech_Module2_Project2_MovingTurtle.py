#########################################
# CS 1110A - Programming in Python      #
# Module 2 - Project 2 - Moving Turtle  #
# Author: Lamech Israel                 #
#                                       #
#########################################



# MovingTurtle.py - Move a circular turtle left-to-right across the screen
# Import the turtle package
import turtle

# All Lamech's Variables
title = 'Lamech Israel\'s Third Attempt (click to stop)'
title_color = 'green'
background_color = input('Please enter in what color you would like the background to be. ')
turtle_shape = 'turtle'
turtle_color = 'blue'
turtle_outline = 'green'


# Function for drawing a turtle at current position
def draw_turtle(ttl):
    
    # To fill the color in circle
    ttl.fillcolor(turtle_color) 
    
    # Start color filling
    ttl.begin_fill()
    
    # Draw the circle
    #ttl.circle(20)
    
    # End color filling
    ttl.end_fill()
    
# Define a function to draw the title
def draw_title(the_title):
    
    # Create a turtle for drawing the title
    ttl = turtle.Turtle()
    
    # Lift the pen
    ttl.penup()
    
    # Move the pen to the initial writing location
    ttl.setpos(-240, 160)
    
    # Set the pen color 
    ttl.color(title_color)
    
    # Set the font, size, and style
    style = ('Arial', 16, 'italic')
    
    # Write the text on the screen
    ttl.write(the_title, font=style)
    
    # Hide the turtle so it no longer displays the cursor
    ttl.hideturtle()
# The while loop will continue so long as Running is True
Running = True
# Define a stop function that will set Running to False
def stop(a, b):
    
    # Global so that the outer Running is set
    global Running
    Running = False
# Create a screen object
screen = turtle.Screen()
# Set the screen size
screen.setup(500, 400)
# Set the screen background color
screen.bgcolor(background_color)
# Screen updates set for animation
screen.tracer(0)
# Capture left mouse click; call 'stop' when click occurs
screen.onclick(stop)
# Call function to display the title
draw_title(title)
# Create a turtle object. We'll call it 'sam'
sam = turtle.Turtle()
# Set turtle shape
sam.shape(turtle_shape)
# Set the turtle color
sam.color(turtle_outline)
# Set the turtle speed
sam.speed(9000000) 
# Hide the turtle
#sam.hideturtle()          
# Lift the turtle pen
sam.penup()               
# Set sam's initial position
sam.goto(-250, 0) 
# Drop turtle pen to surface
sam.pendown()             
# Infinite loop; but stops on left mouse click
# This is the code that does the animation
initial_distance = 0
while Running :
    
    # Clear turtle at current position
    sam.clear()  
    
    # Call function to draw the turtle
    draw_turtle(sam)
    
    # Update the screen
    screen.update()    
    
    # Move turtle forward a tiny amount
    sam.forward(0.025)
    
    # Keep Sam on screen
    initial_distance+=1
    if initial_distance == 10000:
        sam.left(90)
        initial_distance = 5000
    
# We get here after the user clicks the left mouse button
# Terminate the program
exit()

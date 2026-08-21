#=====================================#
# Student Name: Logan Gutierrez
# UIN: 737008832
# Class ID: 
# Project Name: Solar System
#=====================================#

# Imports
import turtle
import math
import random

# Adjust window size
window_width = 1000
window_height = 1000

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Solar System Drawing")
screen.bgcolor("black")
screen.colormode(255)  # Use RGB color mode
screen.canvheight = window_height - 400
screen.canvwidth = window_width - 400
scrnW = screen.canvwidth
scrnH = screen.canvheight

# Set new coordinates
screen.setworldcoordinates(0, scrnW - 100, scrnH - 100, 0)

# Create a turtle object
turtle = turtle.Turtle()
turtle.speed(0)  # Set the drawing speed

def origin():
    # Calculate the origin coordinates based on the window size
    return (-7, -7)

DIFF = origin()[0]

# Temporary function to draw a simple graph with axes and grid lines
def drawGraph():
    # Draw a simple graph with axes
    turtle.setheading(0)  # Reset heading to the right
    turtle.color("black")
    turtle.penup()
    turtle.goto(origin())
    turtle.pendown()
    turtle.forward(500 + DIFF)  # X-axis
    turtle.goto(origin())
    turtle.left(90)
    turtle.forward(500 + DIFF)  # Y-axis
    turtle.goto(origin())

    # Draw grid lines (X)
    for i in range(origin()[0], 500 + DIFF, 50):
        turtle.penup()
        turtle.goto(i, origin()[1])
        turtle.pendown()
        turtle.goto(i, 500)  # Draw vertical grid line

    # Draw grid lines (Y)
    for i in range(origin()[1], 500 + DIFF, 50):
        turtle.penup()
        turtle.goto(origin()[0], i)
        turtle.pendown()
        turtle.goto(500, i)  # Draw horizontal grid line

    turtle.penup()

# Function to draw a circle
def drawCircle(radius, color):
    turtle.goto(turtle.xcor() + radius, turtle.ycor())
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()

# Function to draw a triangle
def drawTriangle(size, color):
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(size)
        turtle.right(120)
    turtle.end_fill()
    turtle.penup()

# Function to draw a square
def drawSquare(size):
    turtle.pendown()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.penup()

# Function to draw a rectangle
def drawRectangle(width, height, color):
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

# Function to draw a regular polygon
def drawPolygon(sides, length, color):
    turtle.pendown()
    angle = 360 / sides
    turtle.color(color)
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(length)
        turtle.right(angle)
    turtle.end_fill()
    turtle.penup()

# Function to draw a star
def drawStar(size, color, rotation):
    turtle.pendown()
    turtle.color(color)
    turtle.setheading(rotation)
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.penup()

# Main program
def main():
    # Draw random stars
    for i in range(100):
        turtle.goto(random.randint(0, 500) + DIFF, random.randint(0, 500) + DIFF)
        drawStar(random.randint(3, 10), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), random.randint(0, 360))

    # Draw a simple graph
    drawGraph()

    # Draw a sun
    turtle.goto(250 + DIFF, 250 + DIFF)  # Move to the center of the graph
    drawCircle(40, (255, 128, 0))  # Draw a red circle
    turtle.goto(250 + DIFF, 250 + DIFF)  # Move to the center of the graph
    drawCircle(37, (255, 205, 0))  # Draw a red circle

    # Draw Mercury
    turtle.goto(320 + DIFF , 260 + DIFF)  # Move to the center of the graph
    drawCircle(13, (169, 169, 169))  # Draw a gray circle

    # Draw Venus
    turtle.goto(175 + DIFF, 287 + DIFF)  # Move to the center of the graph
    drawCircle(17, (255, 198, 73))  # Draw a yellow circle

    # Draw Earth
    turtle.goto(100 + DIFF, 250 + DIFF)  # Move to the center of the graph
    drawCircle(20, (0, 0, 255))  # Draw a blue circle
    # Draw first continent on Earth
    turtle.goto(90 + DIFF, 250 + DIFF)
    drawCircle(5, (34, 139, 34))
    turtle.goto(95 + DIFF, 245 + DIFF)
    drawCircle(5, (34, 139, 34))
    turtle.goto(93 + DIFF, 248 + DIFF)
    drawCircle(5, (34, 139, 34))
    turtle.goto(93 + DIFF, 255 + DIFF)
    drawCircle(5, (34, 139, 34))
    # Draw second continent on Earth
    turtle.goto(108 + DIFF, 250 + DIFF)
    drawCircle(5, (34, 139, 34))
    turtle.goto(110 + DIFF, 255 + DIFF)
    drawCircle(4, (34, 139, 34))

    # Draw moon
    turtle.goto(75 + DIFF, 240 + DIFF)  # Move to the center of the graph
    drawCircle(5, (211, 211, 211))  # Draw a light gray circle
    # Draw craters on the moon
    turtle.goto(73 + DIFF, 238 + DIFF)
    drawCircle(1, (169, 169, 169))
    turtle.goto(77 + DIFF, 242 + DIFF)
    drawCircle(1, (169, 169, 169))

    # Draw Mars
    turtle.goto(375 + DIFF, 150 + DIFF)  # Move to the center of the graph
    drawCircle(15, (255, 0, 0))  # Draw a red circle

    # Draw Jupiter
    turtle.goto(500 + DIFF, 200 + DIFF)  # Move to the center of the graph
    drawCircle(40, (255, 165, 0))  # Draw an orange circle

    # Draw Saturn
    turtle.goto(0 + DIFF, 350 + DIFF)  # Move to the center of the graph
    drawCircle(35, (210, 180, 140))  # Draw a tan circle

    # Draw Uranus
    turtle.goto(400 + DIFF, 400 + DIFF)  # Move to the center of the graph
    drawCircle(30, (0, 255, 255))  # Draw a cyan circle

    # Draw Neptune
    turtle.goto(300 + DIFF, 50 + DIFF)  # Move to the center of the graph
    drawCircle(30, (0, 0, 139))  # Draw a dark blue circle

    # Draw Pluto
    turtle.goto(50 + DIFF, 50 + DIFF)  # Move to the center of the graph
    drawCircle(10, (165, 42, 42))  # Draw a brown circle


    # Hide the turtle and finish
    turtle.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()

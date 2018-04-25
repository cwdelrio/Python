# Import turtle for drawing and math for sin and cos
import turtle
import math

# Colors of the rainbow coded to the radius. 
# Can be changed in the future but good for a demonstration
color_options = {
        10: "#FF0000",
        20: "#FF7F00",
        30: "#FFFF00",
        40: "#00FF00",
        50: "#0000FF",
        60: "#4B0082",
        70: "#9400D3"
}

# Arbitrary coordinates for making sure the start is anywhere but zero
x = 80
y = 20

# Putting turtle at above coordinates
turtle.goto(x,y)

# Set coordinates in case they change.
# Not needed here but a thought for the future
x=turtle.xcor()
y=turtle.ycor()

# Loop for radius. 
for j in range(10,80,10):
    # Set radius based on loop. Not for dynamic use.
    radius = j

    # Set fill color based on loop. Not for dynamic use.
    turtle.fillcolor(color_options[j])i

    turtle.begin_fill()

    # Loop for drawing arcs. Drawing largest to smallest so that colors layer properly. 
    for i in range(0,100):
        turtle.goto(((80-radius) * math.cos(i/100.0 * math.pi)+x),((80-radius)*math.sin(i/100.0*math.pi))+y)

    turtle.end_fill()

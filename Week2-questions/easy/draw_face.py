# Draw a face by jason
#
# THE EXERCISE DESCRIPTION
#
# Use the 'turtle' package to draw a human face to the screen.
# Include as many features as you can - for example,
# start with a head and add eyes, eyebrows, mouth, ....

# A SOLUTION
#
# Problem solving strategy:

# 1. Import the turtle library
from turtle import *

# 2. set the speed to the fastest possible
speed('fastest')

# 3. Draw the head - a circle
up()
goto(100,100)
down()

color('pink')
fill(1)
circle(100)
fill(0)

# 4. Draw two eyes
#    a. Lift the pen, relocate it, then set the pen down at new location
#       i.   lift the pen up
#       ii.  relocate the pen
#       iii. set the pen down
up()
goto(70,190)
down()

#    b. Draw one circle with another smaller solid circle inside
#       i.   draw one circle
#       ii.  turn colour filler on
#       iii. draw a smaller circle
#       ii.  turn colour filler off
color('white')
fill(1)
circle(20)
fill(0)

#    c. Lift the pen, relocate it, then set the pen down at new location
#    d. Draw one circle with another smaller solid circle inside
color('black')
fill(1)
circle(10)
fill(0)

# and again for the right eye
up()
goto(130,190)
down()
color('white')
fill(1)
circle(20)
fill(0)

color('black')
fill(1)
circle(10)
fill(0)

# 5. Draw a mouth
#    a. Lift the pen, relocate it, then set the pen down at new location
up()
goto(80,150)
right(90)

down()
color('red')
fill(1)
circle(20, 180)
fill(0)
color('black')
circle(20,-180)

# 6. Draw the eyebrows
#    a. Lift the pen, relocate it, then set the pen down at new location
up()
goto(50,250)
left(110)
down()
color('brown')
pensize(10)
forward(30)
# end for

# now the right eyebrow
up()
right(20)
forward(45)
right(20)
down()
forward(30)


#    b. Draw first eyebrow
#    c. Lift the pen, relocate it, then set the pen down at new location
#    d. Draw second eyebrow


# 7. Draw some spikey hair
#    a. Lift the pen, relocate it, then set the pen down at new location
#    b. draw a spike of hair
#    c. Lift the pen, relocate it, then set the pen down at new location
#    d. draw a spike of hair
#    e. Lift the pen, relocate it, then set the pen down at new location
#    f. draw a spike of hair
#    g. Lift the pen, relocate it, then set the pen down at new location
#    h. draw a spike of hair
#    i. Lift the pen, relocate it, then set the pen down at new location
#    j. draw a spike of hair

# 8. Draw an earring
#    a. Lift the pen, relocate it, then set the pen down at new location
#    b. Draw a circle


# 9. Draw a nose
#    a. Lift the pen, relocate it, then set the pen down at new location
#    b. draw a circle

# move the turtle out of the way
up()
goto(0,0)
# allow user to view picture before terminating with a return.
myValue = raw_input("Press return to end")


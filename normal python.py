#Created by Afranio Costa

import turtle
import numpy as np

t = turtle.Turtle()

# Creating 1000 random numbers with mean = 0 and sd = 50
x = np.random.normal(loc=0.0, scale=50.0, size=1000)
x = np.sort(x)

#Normal Distribution Function
def normal(x , mean , sd):
    density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return density

#Apply function to the data.
pdf = normal(x,0.0,50)

t.penup()
t.goto(x[0],pdf[0])
t.pendown()
t.screen.setup (startx=680, starty=100)

#Draw a curve
for a,b in zip(x,pdf):
    t.goto(a,b)
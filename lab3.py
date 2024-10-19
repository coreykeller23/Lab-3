"""
Corey Keller
File Name: lab3
Version 1.0
Creation: 2.05.24
Updated: 2.05.24
Purpose: 
"""

#import math.py to use the pi variable
import math

#create varibales for the formulas
circleRad=5
cylinderRad=6
cylinderHeight=8
rectangleLength=4
rectangleWidth=9

#define functions for the associated shapes
def areaCircle(r):
    area=math.pi*r**2
    return area
print("The circle's area is " + str(round(areaCircle(circleRad), 2)) + " units.")

def volCylinder(r, h):
    vol=areaCircle(r)*h
    return vol
print("The cylinder's volume is " + str(round(volCylinder(cylinderRad,cylinderHeight), 2)) + " units.")

def areaRectangle(l, w):
    area=l*w
    return area
print("The rectangle's area is " + str(areaRectangle(rectangleLength, rectangleWidth)) + " units.")
 
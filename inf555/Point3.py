'''
	Point3.py
	inf555

	- Converted to Python Source by Jinay Patel on 03/03/2017
	- Created by Camille MASSET on 18/11/2015.

	Copyright 2015 Basile Camille. All rights reserved.
'''

import math

class Point3:
    x = 0
    y = 0
    z = 0

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def distanceFrom(self, b):
        return math.sqrt(self.x * b.x + self.y * b.y + self.z * b.z)

    def distance2From(self, b):
        return (self.x * b.x + self.y * b.y + self.z * b.z)

    def __add__(self, b):
        return Point3(self.x + b.x, self.y + b.y, self.z + b.z)

    def __mul__(self, a):
        return Point3(self.x * a, self.y * a, self.z * a)

if __name__ == '__main__':
    pt = Point3(1, 1, 1)
    print "Point pt: ", pt.x, pt.y, pt.z
    print "distance2From(Point3(2,0,0)): ", pt.distance2From(Point3(2, 0, 0))
    print "distanceFrom(Point3(2,0,0)): ", pt.distanceFrom(Point3(2, 0, 0))
    pt_1 = pt + Point3(2, 0, 0)
    print "pt + Point3(2,0,0): ", pt_1.x, pt_1.y, pt_1.z
    pt_2 = pt * 2
    print "pt * 2: ", pt_2.x, pt_2.y, pt_2.z

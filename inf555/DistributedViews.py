'''
    DistributedViews.py
    inf555

    - Converted to Python Source by Jinay Patel on 03/03/2017
    - Created by Camille MASSET on 17/11/2015.
    Copyright (C) 2015 Basile Camille. All rights reserved.
'''

import random
import math
from Point3 import Point3

class DistributedViews:
    __d = 0
    __MSE = 0
    __centroids = 0
    __vertices = []

    def __initSeeds():
        self.__MSE = 0
        d = self.getNum()
        # seed = 0
        random.seed()
        indexes = []
        for i in range(d):
            indexes[i] = random.randint(0, len(self.__vertices))
            self.__centroids[i] = self.__vertices[indexes[i]]

        # calculer MSE
        for i in vertices:
            l = i.distance2From(self.__centroids[0])
            i0 = 0
            for i in range(d):
                ll = i.distance2From(self.__centroids[i])
                if (ll < l):
                    l = ll
                    i0 = i
            self.__MSE = self.__MSE + l

    def initSphere(self, filename):
        File = open(filename, 'r')
        Line = ""
        Name = ""
        Line = File.readline()
        while Line:
            Vertex = [0., 0.,  0.]
            floats = Line.split(string.whitespace)
            print "floats are: " ,floats
            # sscanf(Line.c_str(), "%f %f %f", &Vertex[0], &Vertex[1], &Vertex[2]);
            p = Point3(Vertex[0], Vertex[1], Vertex[2])
            self.__vertices.insert(p)
            Line = File.readline()
        File.close()


    def __init__(self, d_):
        self.__d = d_
        self.__MSE = 0.
        self.__centroids = [ Point3() for i in range(d_) ]
        filename = "/home/jinay/workspace/git-repos/upwork/inf555/sphere2.off"
        self.initSphere(filename)

    def __del__(self):
        del self.__centroids

    def getNum(self):
        return self.__d

    def getDirections(self):
        self.__initSeeds()
        d = self.getNum()
        MSEa = 0
        while (MSEa != self.__MSE):
            MSEa = self.__MSE
            MSEp = 0.
            new_centroids = [ Point3() for i in range(d) ]
            classes_sizes = []
            for i in range(d):
                new_centroids[i] = Point3()
                classes_sizes[i] = 0

            # We find the closest centroid for each vertex
            for i in vertices:
                l = i.distance2From(self.__centroids[0])
                i0 = 0
                for i in range(d):
                    ll = i.distance2From(centroids[i])
                    if (ll < l):
                        l = ll
                        i0 = i
                new_centroids[i0] = new_centroids[i0] + i
                classes_sizes[i0] = classes_sizes[i0] + 1
                MSEp = MSEp + l

            for i in range(d):
                classes_sizes[i] = math.max(classes_sizes[i], 1)
                self.__centroids[i] = new_centroids[i] * (1./classes_sizes[i])

            self.__MSE = MSEp

        return self.__centroids

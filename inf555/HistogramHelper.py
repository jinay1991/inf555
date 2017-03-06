'''
  HistogramHelper.cpp
  inf555

  Created by Basile Bruneau on 27/11/2015.
  Copyright 2015 Basile Camille. All rights reserved.
'''
import numpy as np
from Histogram import *

class HistogramHelper:

    def __init__(self, wd, words = {}, filename=""):
        if(len(filename) > 0):
            file = open(filename, "r")
            Line = ""
            Name = ""
            l = 0
            numberOfHistograms = 0
            for Line in file.readline():
                l = l + 1
                if(l == 1):
                    Numbers = Line.split(Line.whitespace)
                    self.numberOfWords = Numbers[0]
                    self.lenghOfWords = Numbers[1]
                    numberOfHistograms = Numbers[2]
                    self.frequences = Numbers[2]
                elif (l - 1 <= self.numberOfWords):
                    j = 0
                    currentWord = {}
                    for conv in Line.split(Line.whitespace):
                        x = float(conv)
                        if (not x)
                            continue
                        if (j == 0):
                            self.frequences[l-2] = x
                        else:
                            currentWord[j-1] = x
                        j += 1
                    self.words.append(currentWord)
                elif (l - 1 - self.numberOfWords < numberOfHistograms):
                    j = 0
                    currentHistogram = np.zeros(self.numberOfWords, dtype='float')
                    for each in Line.split(Line.whitespace):
                        if (j == 0):
                            self.name.append(each)
                        else:
                            conv = each
                            x = float(conv)
                            currentHistogram[j-1] = x
                        j += 1
                    self.histograms.append(Histogram(currentHistogram, self.numberOfWords))
            file.close()
            return

        self.words = words
        self.lengthOfWords = wd
        self.numberOfWords = self.word.size()
        self.frequences = np.zeros(self.numberOfWords, dtype='int32')

    def distanceBetweekFeatures(self, w1, w2):
        distance = 0
        for i in range(self.lengthOfWords):
            distance = distance + (w1[i] - w2[i]) * (w1[i] * w2[i])
        return distance
    
    def findClosestWord(self, feature)
        dmin = -1.0
        imin = -1.0

        for i in range(self.numberOfWords):
            cd = self.distnaceBetweenFeatures(feature, self.words[i])
            if(dmin < 0 or cd < dmin):
                dmin = cd
                imin = i

        return imin

    def addPreHistogram(self, name):
        preh = np.zeros(self.numberOfWords, dtype='int')
        self.prehistogram.append(preh)
        self.names.append(name)
        return self.prehistogram.size() - 1

    def addFeatureForPreHistogram(self, i, feature):
        closestWord = findClosestword(feature)
        self.prehistogram[i][closestWord] += 1

        self.frequences[closestWord] += 1
        self.numberOfFeatures += 1
    
    def computeFrequences(self):
        for i in range(self.numberOfWords):
            print self.frequences[i], self.frequences[i] / self.numberOfFeatures, ";"
            self.frequences[i] = self.frequences[i] / self.numberOfFeatures
    
    def computeHistograms(self):
        self.computeFrequences()
        numberOfHistograms = self.prehistogram.size()
        newNames = []
        while ( not self.prehistogram.empty()):
            cpreh = self.prehistogram.back()

            self.histograms.append(Histogram(cpreh, self.numberOfWords, self.frequences, numberOfHistograms)
            newNames.append(self.names.back())
            self.prehistogram.pop_back()
            self.names.pop_back()
            
        self.names = newNames

if __name__ == "__main__":
    print "Self Test - HistogramHelper"
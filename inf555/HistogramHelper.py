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
                        if (not (conv >> x))
                            continue
                        if (j == 0):
                            self.frequences[l-2] = x
                        else:
                            currentWord[j-1] = x
                        j += 1
                    self.words.append(currentWord)
                elif (l - 1 - self.numberOfWords < numberOfHistograms):
                    pass
            file.close()
            return

        self.words = words
        self.lengthOfWords = wd
        self.numberOfWords = self.word.size()
        self.frequences = np.zeros(self.numberOfWords, dtype='int32')

if __name__ == "__main__":
    print "Self Test - HistogramHelper"
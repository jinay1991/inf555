'''
  Histogram.cpp
  inf555

  Created by Camille MASSET on 26/11/2015.
  Copyright  2015 Basile Camille. All rights reserved.
'''
import math

class Histogram:

    size = 0
    coords = []

    def __init__(self, counts, vocab_size, freq, coll_size, coords=[]):
        self.size = vocab_size
        s = 0
        for i in range(vocab_size):
            s = s + counts[i]
        
        if coords.count() > 0:
            for i in range(vocab_size):
                self.coords[i] = coords[i]
            print self.norm()
            return

        for i in range(vocab_size):
            if(freq[i] == 0):
                self.coords[i] = 0
            else:
                self.coords[i] = counts[i] / s * math.log(10, coll_size / freq[i])
    
    def __del__(self):
        pass

    def norm(self):
        n = 0
        for i in range(self.size):
            n = n + self.coords[i] * self.coords[i]
        
        return math.sqrt(n)

    def similarity(self, a):
        assert (selt.size == a.size)
        thisNorm = self.norm()
        aNorm = a.norm()
        assert (thisNorm > 0)
        assert (aNorm > 0)

        s = 0
        for i in range(self.size):
            s = s + self.coords[i] * self.coords[i]

        return s / (thisNorm * aNorm)
    
if __name__ == "__main__":
    print "self test - Histogram"
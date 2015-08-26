'''
Created on Aug 26, 2015

@author: szw0069
'''
import os, re

class StarCatalog:

    def __init__(self):
        self.catalog = []
    
    def loadCatalog(self, starFile=None):
        try:
            if(starFile==None):
                raise ValueError
        except ValueError:
            print("")
                
        try:
            if(os.path.isfile(starFile)):
                content = open(starFile, 'r')
            else:
                raise ValueError
        
        except ValueError:
            print("")
            
        for stars in content:
            line = re.split("\s+", stars)
            
            if(len(line) != 4):
                line.pop(4)
            self.catalog.append(line)
        return len(self.catalog)    
                                                   
                    
    
    def emptyCatalog(self):
        Length = len(self.catalog)
        self.catalog = []
        return Length
    
    def getStarCount(self, lowerMagnitude=None, upperMagnitude=None):
        return self.count
    
    def getMagnitude(self, rightAscentionCenterPoint=None,
                     declinationCenterPoint=None,
                     fieldOfView=None):
        pass
        
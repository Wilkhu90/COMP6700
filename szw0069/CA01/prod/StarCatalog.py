'''
Created on Aug 26, 2015

@author: szw0069
'''
import os, re

class StarCatalog(object):

    def __init__(self):
        self.catalog = []
    
    def loadCatalog(self, starFile=None):
        try:
            if(starFile==None):
                raise ValueError
        except ValueError:
            print("StarCatalog.loadCatalog:  An input text file is required to load stars.")
                
        try:
            if(os.path.isfile(starFile)):
                content = open(starFile, 'r')
            else:
                raise ValueError
        
        except ValueError:
            print("StarCatalog.loadCatalog:  No such file exist. Please check whether the name is correct.")
            
        for stars in content:
            line = re.split('\s+', stars)
            
            if(len(line) != 4):
                line.pop(4)
            for num in line:
                if not num.isdigit():
                    ex = ValueError("StarCatalog.loadCatalog:  File contains invalid data. Data must contain numbers.")
                    raise ex
            
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
    
    def getCurrentCount(self):
        return len(self.catalog)
        
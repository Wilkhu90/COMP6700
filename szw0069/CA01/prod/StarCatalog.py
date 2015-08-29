'''
Created on Aug 26, 2015

@author: szw0069
'''
import os
import re

class StarCatalog(object):

    def __init__(self):
        self.catalog = {}
    
    def loadCatalog(self, starFile=None):
        if(starFile==None)|(type(starFile) is not str):
            raise ValueError("StarCatalog.loadCatalog:  An input text file is required to load stars.")
            
        if(os.path.isfile(starFile)):
            content = open(starFile, 'r')
        else:
            raise ValueError("StarCatalog.loadCatalog:  No such file exist. Please check whether the name is correct.")
         
        for stars in content:
            line = re.split('\s+', stars)
            if(len(line) != 4):
                line.pop(4)
            for num in line:
                try:
                    if float(num):
                        pass
                except ValueError:
                    raise ValueError("StarCatalog.loadCatalog:  File contains invalid data. Data must contain numbers.")
            
            if int(line[0]) in self.catalog.keys():
                raise ValueError("StarCatalog.loadCatalog:  An attempt to add a duplicate star.")
            else:
                self.catalog[int(line[0])]= [float(x) for x in line[1:]]
            
        return len(self.catalog)           
    
    def emptyCatalog(self):
        Length = len(self.catalog)
        self.catalog = {}
        return Length
    
    def getStarCount(self, lowerMagnitude=None, upperMagnitude=None):
        return self.count
    
    def getMagnitude(self, rightAscentionCenterPoint=None,
                     declinationCenterPoint=None,
                     fieldOfView=None):
        pass
    
    def getCurrentCount(self):
        return len(self.catalog)
    
    def getStar(self, star):
        return self.catalog.get(star)
        
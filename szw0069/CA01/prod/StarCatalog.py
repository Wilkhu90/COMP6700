'''
Created on Aug 26, 2015

@author: szw0069
'''
import os
import re
import math

class StarCatalog(object):

    def __init__(self):
        self.catalog = {}
    
    def loadCatalog(self, starFile=None):
        #Handling Exception for irregularity in the file name.
        if(starFile==None)|(type(starFile) is not str):
            raise ValueError("StarCatalog.loadCatalog:  An input text file is required to load stars.")
        #Handling Exception when file doesn't exist.
        if(os.path.isfile(starFile)):
            content = open(starFile, 'r')
        else:
            raise ValueError("StarCatalog.loadCatalog:  No such file exist. Please check whether the name is correct.")
        #Logic for Reading file and creating a catalog.  
        for stars in content:
            line = re.split('\s+', stars)
            if(len(line) != 4):
                line.pop(4)
        #Handling exception if the data in the file has irregularity.        
            for num in line:
                try:
                    if float(num):
                        pass
                except ValueError:
                    raise ValueError("StarCatalog.loadCatalog:  File contains invalid data. Data must contain numbers.")
        #Checking for the star existence in the catalog.    
            if int(line[0]) in self.catalog.keys():
                raise ValueError("StarCatalog.loadCatalog:  An attempt to add a duplicate star.")
            else:
                self.catalog[int(line[0])]= [float(x) for x in line[1:]]
        content.close()    
        return len(self.catalog)           
    
    def emptyCatalog(self):
        Length = len(self.catalog)
        self.catalog = {}
        return Length
    
    def getStarCount(self, lowerMagnitude=None, upperMagnitude=None):
        #If the catalog is empty, the operation won't continue.
        try:
            if(self.catalog == None):
                raise ValueError
        except  ValueError:
            print("StarCatalog.getStarCount:  Must load a star catalog first.")
        #Setting up default values, if found to be None.    
        if (lowerMagnitude == None):
            lowerMagnitude = min(data[0] for data in self.catalog.values())
        #Setting up default values, if found to be None.    
        if (upperMagnitude == None):
            upperMagnitude = max(data[0] for data in self.catalog.values())
        #Handling exception for Non-Numeric parameters.
        if (isinstance(lowerMagnitude, (float, int)) == False) | (isinstance(upperMagnitude, (float, int)) == False):
            raise ValueError("StarCatalog.getStarCount:  Please Input an appropriate numeric value.")
        #Handling exception when Lower Magnitude is greater than Upper Magnitude.
        if (lowerMagnitude>upperMagnitude):
            raise ValueError("StarCatalog.getStarCount:  Lower magnitude is higher than Upper Magnitude.")
        
        # Calculation logic for counting the stars in range. 
        count = 0
        for catalog in self.catalog.values():
            if(catalog[0] >= lowerMagnitude and catalog[0] <= upperMagnitude):
                count = count + 1      
        return count
    
    def getMagnitude(self, rightAscentionCenterPoint=None,
                     declinationCenterPoint=None,
                     fieldOfView=None):
        #Handling exception for empty catalog.
        try:
            if(self.catalog == None):
                raise ValueError
        except ValueError:
            print("StarCatalog.getMagnitude:  Catalog is empty.")
        
        validStars = []
        #Handling exception for checking the boundaries.
        if(rightAscentionCenterPoint < 0 or rightAscentionCenterPoint > 2 * math.pi):
            raise ValueError("StarCatalog.getMagnitude:  rightAscentionCenterPoint isn't in the proper range of 0 to 2pi")
        
        if(declinationCenterPoint < -math.pi/2 or declinationCenterPoint > math.pi/2):
            raise ValueError("StarCatalog.getMagnitude:  declinationCenterPoint isn't in the proper range of -pi/2 to pi/2")
        
        if(fieldOfView < 0 or fieldOfView > 2 * math.pi):
            raise ValueError("StarCatalog.getMagnitude:  fieldOfView isn't in the proper range of 0 to 2pi")
        #Logic for calculating the magnitude of the brightest star in given FOV.
        fov = float(fieldOfView/2)
        for catalog in self.catalog.values():
            ra = float(catalog[1])
            dec = float(catalog[2])
            
            if(((ra >= (rightAscentionCenterPoint - fov)) and (ra <= (rightAscentionCenterPoint + fov))) 
               and ((dec >= (declinationCenterPoint - fov)) and (dec <= (declinationCenterPoint + fov)))):
                validStars.append(catalog[0])
        
        validStars.sort()
        if(len(validStars) == 0):
            return None
        
        return validStars[0]
    
    def getCurrentCount(self):
        return len(self.catalog)
    
    def getStar(self, star):
        return self.catalog.get(star)
        
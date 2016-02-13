'''
Created on Sep 23, 2015

@author: sum
'''
import math
import os
import CA01.prod.StarCatalog as StarCatalog
from CA02.prod import Environment

class StarSensor(object):
    '''
    classdocs
    '''


    def __init__(self, fieldOfView=None):
        
        if(fieldOfView == None):
            raise ValueError("StarSensor.__init__:  fieldOfView is Mandatory.")
        if(fieldOfView <= 0 or fieldOfView > math.pi/4):
            raise ValueError("StarSensor.__init__:  fieldOfView isn't in the proper range of 0 to pi/4.")
        
        self.fov = fieldOfView
        self.isConfigured = False
        self.isInitialized = False
        self.env = None
    
    def initializeSensor(self, starFile=None):
        if(starFile==None)|(type(starFile) is not str):
            raise ValueError("StarSensor.initializeSensor:  An input text file is required to load stars.")
        #Handling Exception when file doesn't exist.
        if(os.path.isfile(starFile)):
            pass
        else:
            raise ValueError("StarSensor.initializeSensor:  No such file exist. Please check whether the name is correct.")
        
        self.starsCatalog = StarCatalog.StarCatalog()
        count = self.starsCatalog.loadCatalog(starFile)
        self.isInitialized = True
        return count
    
    def configure(self, environment=None):
        if (environment == None):
            raise ValueError("StarSensor.configure:  Input for environment is Mandatory.")
        if (isinstance(environment, Environment.Environment) == False):
            raise ValueError("StarSensor.configure:  Please Input an appropriate Environment.")
        
        self.env = environment
        self.isConfigured = True
        return self.isConfigured
    
    def getSensorPosition(self):
        if (self.isConfigured == True):
            microsecondsInDay = 24*60*60*1000000 #23*60*60*1000000 + 56*60*1000000 + 41*100000
            timeElapsed = self.env.getTime()
            
            numberOfOrbits = (float(timeElapsed)/float(microsecondsInDay))
            amountOfOrbits = numberOfOrbits - int(numberOfOrbits)
            rightAscentionSatellite = 2.0*math.pi * amountOfOrbits
            
            numberOfRotation = (float(timeElapsed)/float(self.env.getRotationalPeriod()))
            amountOfRotation = numberOfRotation - int(numberOfRotation)
            rotationalSatellite = 2.0 * math.pi * amountOfRotation
            offset = math.pi /2.0
            if (rotationalSatellite <= math.pi/2.0):
                declinationSensor = rotationalSatellite
            else:
                if (rotationalSatellite <= 3.0*math.pi/2):
                    declinationSensor = math.pi - rotationalSatellite
                    offset = offset + math.pi
                else:
                    declinationSensor = rotationalSatellite - (2.0 * math.pi)
                        
            rightAscentionSensor = math.fmod((rightAscentionSatellite + offset), 2.0*math.pi)          
        else:
            rightAscentionSensor = None
            declinationSensor = None
        return [rightAscentionSensor, declinationSensor]        
    
    def serviceRequest(self):
        if (self.isConfigured == False) or (self.isInitialized == False):
            return None        
        else:
            starInfo = self.getSensorPosition()   
            if(starInfo[0] == None) | (starInfo[1] == None):
                self.brightestStar = None
            elif (starInfo[0] == 0) and (starInfo[1] == 0):
                return '8000'
            else:
                self.brightestStar = self.starsCatalog.getMagnitude(starInfo[0], starInfo[1], self.fov)
            
            self.env.incrementTime(40)
            return self.convertHexadecimal(self.brightestStar)
            
    
    def convertHexadecimal(self, brightestStar=None):
        if (brightestStar == None):
            return None
        
        elif (brightestStar>=0):
            return format(int(brightestStar*10), '04x')
        
        else:
            newString = ''
            binString = format(int(abs(brightestStar*10)), '016b')
            for i in range(len(binString)):
                if binString[i] == '1':
                    newString = newString + '0'
                elif binString[i] == '0':
                    newString = newString + '1'
                
            return format(int(newString, 2), '04x')
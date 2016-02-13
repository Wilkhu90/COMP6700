'''
Created on Nov 21, 2015

@author: sum
'''
import CA02.prod.Environment as Environment
import math

class SolarCollector(object):
    '''
    Collects Solar enery to run the satellite.
    '''


    def __init__(self):
        self.isConfigured = False
        self.env = None
        self.upperBlindSpot = 8.6
        self.lowerBlindSpot = 351.4
        self.blindSpotUpperRadians = self.upperBlindSpot * (math.pi / 180)
        self.blindSpotlowerRadians = self.lowerBlindSpot * (math.pi / 180)
    
    def configure(self, environment=None):
        if (environment == None):
            raise ValueError("SolarCollector.configure:  Input for environment is Mandatory.")
        if (isinstance(environment, Environment.Environment) == False):
            raise ValueError("SolarCollector.configure:  Please Input an appropriate Environment.")
        
        self.env = environment
        self.isConfigured = True
        return self.isConfigured
    
    def getSatellitePosition(self):
        microsecondsInDay = 24*60*60*1000000 #23*60*60*1000000 + 56*60*1000000 + 41*100000
        timeElapsed = self.env.getTime()
            
        numberOfOrbits = (float(timeElapsed)/float(microsecondsInDay))
        amountOfOrbits = numberOfOrbits - int(numberOfOrbits)
        rightAscensionSatellite = 2.0*math.pi * amountOfOrbits
        
        return rightAscensionSatellite
    
    def serviceRequest(self):
        if (self.isConfigured == False):
            raise ValueError("SolarCollector.serviceRequest:  Please Configure with appropriate Environment.")

        rightAscension = self.getSatellitePosition()
        self.env.incrementTime(40)
        if (rightAscension < self.blindSpotUpperRadians):
            return '0000'
        elif (rightAscension > self.blindSpotlowerRadians):
            return '0000'
        else:
            return format(32767*(100-self.env.getDegradation())/100, '04x')
        
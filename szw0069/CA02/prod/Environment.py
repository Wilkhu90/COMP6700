'''
Created on Sep 23, 2015

@author: sum
'''

class Environment(object):
    '''
    classdocs
    '''


    def __init__(self):
        self.clockTime = 0
        self.rotationalPeriod = None
        self.degradation = 0
    
    def getTime(self):
        return self.clockTime
    
    def incrementTime(self, microseconds=None):
        if (microseconds == None):
            raise ValueError("Environment.incrementTime:  Input for microseconds is Mandatory.")
        if (isinstance(microseconds, int) == False) | (microseconds<0):
            raise ValueError("Environment.incrementTime:  Please Input an appropriate integer value.")
        
        self.clockTime = self.clockTime + microseconds
        return self.clockTime
            
    
    def setRotationalPeriod(self, microseconds=None):
        if (microseconds == None):
            raise ValueError("Environment.setRotationalPeriod:  Input for microseconds is Mandatory.")
        if (isinstance(microseconds, int) == False) | (microseconds<1000000):
            raise ValueError("Environment.setRotationalPeriod:  Please Input an appropriate integer value GE 1,000,000.")
        
        self.rotationalPeriod = microseconds
        return self.rotationalPeriod
    
    def getRotationalPeriod(self):
        if (self.rotationalPeriod == None):
            raise ValueError("Environment.getRotationalPeriod:  Rotation period has not been previously set.")
        
        return self.rotationalPeriod
    
    def setStartTime(self, startTime=None):
        if (isinstance(startTime, int) == False) | (startTime<0):
            raise ValueError("Environment.setStartTime:  Please Input an appropriate integer value.")
        
        if startTime != None:
            self.incrementTime(startTime)
        
        return self.clockTime

    
    def setDegradation(self, degradation=None):
        if (isinstance(degradation, int) == False) | (degradation<0) | (degradation>100):
            raise ValueError("Environment.setDegradation:  Please Input an appropriate integer value.")
        
        if degradation != None:
            self.degradation = degradation
        
        return self.degradation
    
    def getDegradation(self):
        return self.degradation
    
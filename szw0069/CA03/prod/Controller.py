'''
Created on Oct 20, 2015

@author: sum
'''
import os
import CA03.prod.ComponentFactory as cFactory
import CA03.prod.Architecture as Architecture

class Controller(object):
    
    def __init__(self):
        self.deviceList = []
        self.frameTime = None
        self.env = None
        self.isInitialized = False
        self.runtime = None
        self.DEVICE_LIST = ['StarSensor', 'Device', 'SolarCollector']
    
    def initialize(self, architectureFile=None):
        if(architectureFile==None)|(type(architectureFile) is not str):
            raise ValueError("Controller.initialize:  An input text file name is required for Controller function to run.")
        
        if (architectureFile.endswith('.xml') == False) | (len(architectureFile.split('.')) < 2) | (len(architectureFile.split('.')[0]) == 0):
            raise ValueError("Controller.initialize:  The file name is incorrect. Please try another name.")
            
        if(os.path.isfile(architectureFile)):
            xmlArchitecture = Architecture.Architecture(architectureFile)
            components = xmlArchitecture.getComponentDefinition()
            
            self.instanceObjects = self.createInstances(components)
            
            frame = xmlArchitecture.getFrameInformation()
            try:
                self.frameTime = (int) (frame[0][0])
                if self.frameTime >= 0:
                    for index in range(1,len(frame[0])):
                        if (frame[0][index] in self.DEVICE_LIST):
                            self.deviceList.append(str(frame[0][index]))
                        else:
                            raise ValueError("Controller.initialize:  The frame is invalid.")        
                else:
                    raise ValueError("Controller.initialize:  The frame is invalid.")   
            except:
                raise ValueError("Controller.initialize:  The frame is invalid.")
            self.isInitialized = True
            output = []
            for x in self.deviceList:
                if x not in output:
                    output.append(x)
            return output
        else:
            raise ValueError("Controller.initialize:  The file doesn't exist. Please check the name of file.")
     
    def createInstances(self, components):
        objectDict = {}
        for component in components:
            instance = cFactory.ComponentFactory(component)
            objectDict[component['component']] = (instance.getComponent())
    
        return objectDict
     
    def run(self, microseconds=None):
        if (microseconds == None):
            raise ValueError("Controller.run:  Input for microseconds is Mandatory.")
        if (isinstance(microseconds, int) == False) | (microseconds<=0):
            raise ValueError("Controller.run:  Please Input an appropriate integer value.")
        if (self.isInitialized == False):
            raise ValueError("Controller.run:  Please Initialize the Controller with architecture File.")
        totalTimeSpent = 0
        if (len(self.deviceList) > 0):
            self.env = self.instanceObjects.get('Environment')
            self.myMonitor = self.instanceObjects.get('Monitor')
            self.myMonitor.configure(self.env)
            
            self.pollingDevice(self.deviceList)
            
            totalTimeSpent = self.env.getTime()
            activityTime = totalTimeSpent
            if self.frameTime > activityTime:
                totalTimeSpent = self.env.incrementTime(self.frameTime - activityTime)
                if microseconds - totalTimeSpent > 0:
                    while(microseconds - totalTimeSpent > 0):     
                        #print totalTimeSpent
                        if activityTime <  self.frameTime:
                            self.pollingDevice(self.deviceList)
                            totalTimeSpent = self.env.incrementTime(self.frameTime - activityTime)              
                        else:
                            self.pollingDevice(self.deviceList)
                            totalTimeSpent = self.env.incrementTime(activityTime)
                else:
                    return activityTime  
            else:
                while(microseconds - self.env.getTime() > 0):
                    self.pollingDevice(self.deviceList)
                totalTimeSpent = self.env.getTime()                
        return totalTimeSpent
    
    
    def request(self, CurrentDevice):
        myDevice = self.instanceObjects.get(CurrentDevice)
        myDevice.configure(self.env)
        result = myDevice.serviceRequest() 
        return result    
    
    def pollingDevice(self, deviceList):
        for device in deviceList:
            self.myMonitor.serviceRequest("Controller", device)
            response = self.request(device)    
            self.myMonitor.serviceRequest(device, "Controller", response)
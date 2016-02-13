'''
Created on Oct 20, 2015

@author: sum
'''
import os
import CA02.prod.Environment as Environment

class Monitor(object):
    
    def __init__(self):
        self.isInitialized = None
        self.isConfigured = False
        self.env = None
        self.logger = None
    
    def initialize(self, logFile=None):
        if(logFile==None)|(type(logFile) is not str):
            raise ValueError("Monitor.initialize:  An input text file name is required to log information.")
        
        if (logFile.endswith('.txt') == False) | (len(logFile.split('.')) < 2) | (len(logFile.split('.')[0]) == 0):
            raise ValueError("Monitor.initialize:  The file name is incorrect. Please try another name.")
            
        if(os.path.isfile(logFile)):
            self.logger = logFile
            self.isInitialized = False
            return self.isInitialized
        else:
            open(logFile, 'a').close()
            self.logger = logFile
            self.isInitialized = True
            return self.isInitialized
    
    def configure(self, environment=None):
        if (environment == None):
            raise ValueError("Monitor.configure:  Input for environment is Mandatory.")
        if (isinstance(environment, Environment.Environment) == False):
            raise ValueError("Monitor.configure:  Please Input an appropriate Environment.")
        
        self.env = environment
        self.isConfigured = True
        return self.isConfigured
    
    def serviceRequest(self, source=None, target=None, event='serviceRequest'):
        if (source == None) or (target == None):
            raise ValueError("Monitor.serviceRequest:  Please Initialize with source/target.")
        if (self.logger == None):
            raise ValueError("Monitor.serviceRequest:  Please Initialize with logFile.")
        serviceTime = self.env.getTime()
        if (self.isConfigured == False) or (self.logger != None):
            fileInput = open(self.logger, 'a')
            inputLine = "%d\t%s\t%s\t%s\n"%(serviceTime, source, target, event)
            fileInput.write(inputLine)
            fileInput.close()
            
        return serviceTime
    
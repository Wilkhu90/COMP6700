'''
Created on Oct 20, 2015

@author: sum
'''
import unittest
import os
import CA03.prod.Monitor as Monitor
import CA02.prod.Environment as Environment

class Test(unittest.TestCase):

    def test100_010_ShouldConstruct(self):
        self.assertIsInstance(Monitor.Monitor(), Monitor.Monitor)
        
    def test200_010_ShouldInitializeWithLogFile(self):
        myMonitor = Monitor.Monitor()
        logFile="logfile.txt"
        result = not os.path.isfile(logFile)
        self.assertEquals(myMonitor.initialize(logFile), result) 
        
    def test200_910ShouldRaiseExceptionOnIncorrectFileName(self):
        with self.assertRaises(ValueError) as context:
            myMonitor = Monitor.Monitor()
            myMonitor.initialize(logFile="logfile") 
    
    def test200_920ShouldRaiseExceptionOnIncorrectFileExtension(self):
        with self.assertRaises(ValueError) as context:
            myMonitor = Monitor.Monitor()
            myMonitor.initialize(logFile="logfile.csv")     
            
    def test200_930ShouldRaiseExceptionOnFileNameLessThanOne(self):
        with self.assertRaises(ValueError) as context:
            myMonitor = Monitor.Monitor()
            myMonitor.initialize(logFile=".txt")     
     
    def test200_940ShouldRaiseExceptionOnMissingFileName(self):
        with self.assertRaises(ValueError) as context:
            myMonitor = Monitor.Monitor()
            myMonitor.initialize()                   

    def test200_950ShouldRaiseExceptionOnFileNotString(self):
        with self.assertRaises(ValueError) as context:
            myMonitor = Monitor.Monitor()
            myMonitor.initialize(logFile=2)  
            
    def test300_010_ShouldConfigureWithEnvironment(self):
        myMonitor = Monitor.Monitor()
        env = Environment.Environment()
        env.setRotationalPeriod(1000000)
        self.assertEquals(myMonitor.configure(env), True) 
        
    def test300_910ShouldRaiseExceptionOnMissingEnvironment(self):
        with self.assertRaises(ValueError) as context:
            myMonitor = Monitor.Monitor()
            myMonitor.configure()   
    
    def test300_920ShouldRaiseExceptionOnPassingNonEnvironmentInstance(self):
        with self.assertRaises(ValueError) as context:
            myMonitor = Monitor.Monitor()
            env = 2
            myMonitor.configure(env)  
            
    def test400_010_ShouldRunServiceRequest(self):
        myMonitor = Monitor.Monitor()
        env = Environment.Environment()
        env.setRotationalPeriod(1000000)
        myMonitor.configure(env)
        myMonitor.initialize(logFile="logfile.txt")
        self.assertEquals(myMonitor.serviceRequest(source="Controller", target="Device"), 0) 
        
    def test400_910ShouldRaiseExceptionOnMissingInitialization(self):
        with self.assertRaises(ValueError) as context:
            myMonitor = Monitor.Monitor()
            env = Environment.Environment()
            env.setRotationalPeriod(1000000)
            myMonitor.configure(env)  
            self.assertEquals(myMonitor.serviceRequest(source="Controller", target="Device"), 0)
  
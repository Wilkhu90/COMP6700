'''
Created on Sep 26, 2015

@author: sum
'''
import unittest
import CA02.prod.Environment as Environment

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def test100_010_ShouldConstruct(self):
        self.assertIsInstance(Environment.Environment(), Environment.Environment)
        
        
        
    def test200_010_ShouldReturnCurrentTimeOfSimulatedClock(self):
        myEnv = Environment.Environment()
        self.assertEquals(myEnv.getTime(), 0)
        
    def test200_020_ShouldReturnCurrentTimeOfSimulatedClockAfterIncrement(self):
        myEnv = Environment.Environment()
        myEnv.incrementTime(10000000)
        self.assertEquals(myEnv.getTime(), 10000000)
        
    def test300_010_ShouldReturnIncrementTimeOfSimulatedClock(self):
        myEnv = Environment.Environment()
        self.assertEquals(myEnv.incrementTime(10000000), 10000000)  
        
    def test300_910_ShouldRaiseExceptionOnTimeInFloat(self):
        with self.assertRaises(ValueError) as context:
            myEnv = Environment.Environment()
            myEnv.incrementTime(10000000.00)    
            
    def test300_920_ShouldRaiseExceptionOnTimeLessThanZero(self):
        with self.assertRaises(ValueError) as context:
            myEnv = Environment.Environment()
            myEnv.incrementTime(-1)    
            
    def test300_930_ShouldRaiseExceptionOnTimeAbsent(self):
        with self.assertRaises(ValueError) as context:
            myEnv = Environment.Environment()
            myEnv.incrementTime() 
            
    def test400_010_ShouldSetAndReturnRotationalPeriod(self):
        myEnv = Environment.Environment()
        self.assertEquals(myEnv.setRotationalPeriod(1000001), 1000001)
    
    def test400_020_ShouldSetAndReturnRotationalPeriodBoundaryCase(self):
        myEnv = Environment.Environment()
        self.assertEquals(myEnv.setRotationalPeriod(1000000), 1000000)                        
        
    def test400_910_ShouldRaiseExceptionOnRotationalPeriodInFloat(self):
        with self.assertRaises(ValueError) as context:
            myEnv = Environment.Environment()
            myEnv.setRotationalPeriod(10000001.00)    
            
    def test400_920_ShouldRaiseExceptionOnRotationalPeriodLessThanMillion(self):
        with self.assertRaises(ValueError) as context:
            myEnv = Environment.Environment()
            myEnv.setRotationalPeriod(999999)     
     
    def test400_930_ShouldRaiseExceptionOnRotationalPeriodAbsent(self):
        with self.assertRaises(ValueError) as context:
            myEnv = Environment.Environment()
            myEnv.setRotationalPeriod()   
            
    def test500_010_ShouldGetRotationalPeriod(self):
        myEnv = Environment.Environment()
        myEnv.setRotationalPeriod(1000001)
        self.assertEquals(myEnv.getRotationalPeriod(), 1000001)
    
    def test500_020_ShouldGetRotationalPeriodBoundaryCase(self):
        myEnv = Environment.Environment()
        myEnv.setRotationalPeriod(1000000)
        self.assertEquals(myEnv.getRotationalPeriod(), 1000000)                        
        
    def test500_910_ShouldRaiseExceptionOnRotationalPeriodAbsent(self):
        with self.assertRaises(ValueError) as context:
            myEnv = Environment.Environment()
            myEnv.getRotationalPeriod()   
            
    def test600_010_ShouldSetAndReturnStartTime(self):
        myEnv = Environment.Environment()
        self.assertEquals(myEnv.setStartTime(500), 500)    
    
    def test600_910_ShouldRaiseExceptionOnStartTimeLessThanZero(self):
        with self.assertRaises(ValueError) as context:
            myEnv = Environment.Environment()
            myEnv.setStartTime(-1)   
            
    def test600_920_ShouldRaiseExceptionOnStartTimeFloat(self):
        with self.assertRaises(ValueError) as context:
            myEnv = Environment.Environment()
            myEnv.setStartTime(500.50) 
            
    def test700_010_ShouldSetAndReturnDegradation(self):
        myEnv = Environment.Environment()
        self.assertEquals(myEnv.setDegradation(0), 0) 
    
    def test700_020_ShouldSetAndReturnDegradation(self):
        myEnv = Environment.Environment()
        self.assertEquals(myEnv.setDegradation(100), 100)  
    
    def test700_030_ShouldSetAndReturnDegradation(self):
        myEnv = Environment.Environment()
        self.assertEquals(myEnv.setDegradation(50), 50)     
    
    def test700_910_ShouldRaiseExceptionOnDegradationLessThanZero(self):
        with self.assertRaises(ValueError) as context:
            myEnv = Environment.Environment()
            myEnv.setDegradation(-1)  

    def test700_920_ShouldRaiseExceptionOnDegradationGT100(self):
        with self.assertRaises(ValueError) as context:
            myEnv = Environment.Environment()
            myEnv.setDegradation(101) 
            
    def test700_930_ShouldRaiseExceptionOnDegradationFloat(self):
        with self.assertRaises(ValueError) as context:
            myEnv = Environment.Environment()
            myEnv.setDegradation(50.50) 
                        
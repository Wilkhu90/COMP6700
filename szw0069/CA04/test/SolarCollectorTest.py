'''
Created on Nov 28, 2015

@author: sum
'''
import unittest
import CA04.prod.SolarCollector as SolarCollector
import CA02.prod.Environment as Environment

class Test(unittest.TestCase):

    def test100_010_ShouldConstruct(self):
        self.assertIsInstance(SolarCollector.SolarCollector(), SolarCollector.SolarCollector)

    def test200_010_ShouldConfigureWithEnvironment(self):
        mySc = SolarCollector.SolarCollector()
        env = Environment.Environment()
        env.setRotationalPeriod(1000000)
        self.assertEquals(mySc.configure(env), True) 
        
    def test200_910ShouldRaiseExceptionOnMissingEnvironment(self):
        with self.assertRaises(ValueError) as context:
            mySc = SolarCollector.SolarCollector()
            mySc.configure()   
    
    def test200_920ShouldRaiseExceptionOnPassingNonEnvironmentInstance(self):
        with self.assertRaises(ValueError) as context:
            mySc = SolarCollector.SolarCollector()
            env = 2
            mySc.configure(env)
            
    def test300_010_ShouldRunWithEnvironmentReturningZero(self):
        mySc = SolarCollector.SolarCollector()
        env = Environment.Environment()
        env.setRotationalPeriod(1000000)
        env.setDegradation(50)
        mySc.configure(env)
        self.assertEquals(mySc.serviceRequest(), '0000') 
    def test300_020_ShouldRunWithinUpperBoundReturningZero(self):
        mySc = SolarCollector.SolarCollector()
        env = Environment.Environment()
        env.setRotationalPeriod(1000000)
        env.setDegradation(50)
        env.incrementTime(10000000)
        mySc.configure(env)
        self.assertEquals(mySc.serviceRequest(), '0000') 
    
    def test300_030_ShouldRunOutsideUpperBoundReturningZero(self):
        mySc = SolarCollector.SolarCollector()
        env = Environment.Environment()
        env.setRotationalPeriod(1000000)
        env.setDegradation(50)
        env.incrementTime(10*60*60*1000000)
        mySc.configure(env)
        self.assertEquals(mySc.serviceRequest(), '3fff') 
        
    def test300_040_ShouldRunWithinLowerBoundReturningZero(self):
        mySc = SolarCollector.SolarCollector()
        env = Environment.Environment()
        env.setRotationalPeriod(1000000)
        env.setDegradation(50)
        env.incrementTime(23*60*60*1000000+37*60*1000000)
        mySc.configure(env)
        self.assertEquals(mySc.serviceRequest(), '0000')    
    
    def test300_910_ShouldNotRunWithoutConfiguration(self):
        with self.assertRaises(ValueError) as context:
            mySc = SolarCollector.SolarCollector()
            mySc.serviceRequest()       
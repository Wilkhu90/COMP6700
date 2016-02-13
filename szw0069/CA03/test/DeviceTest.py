'''
Created on Oct 20, 2015

@author: sum
'''
import unittest
import CA03.prod.Device as Device
import CA02.prod.Environment as Environment

class Test(unittest.TestCase):


    def test100_010_ShouldConstruct(self):
        self.assertIsInstance(Device.Device(), Device.Device)

    def test200_010_ShouldConfigureWithEnvironment(self):
        myDevice = Device.Device()
        env = Environment.Environment()
        env.setRotationalPeriod(1000000)
        self.assertEquals(myDevice.configure(env), True) 
        
    def test200_910ShouldRaiseExceptionOnMissingEnvironment(self):
        with self.assertRaises(ValueError) as context:
            myDevice = Device.Device()
            myDevice.configure()   
    
    def test200_920ShouldRaiseExceptionOnPassingNonEnvironmentInstance(self):
        with self.assertRaises(ValueError) as context:
            myDevice = Device.Device()
            env = 2
            myDevice.configure(env)    
            
    def test300_010_ShouldGenerateZeroWith25PercentPrabability(self):
        myDevice = Device.Device()
        env = Environment.Environment()
        env.setRotationalPeriod(1000000)
        myDevice.configure(env)
        result = []
        for _ in range(100000):
            result.append(myDevice.serviceRequest())
        output = (float) (result.count('0000'))/len(result)          
        self.assertAlmostEquals(output, 0.250000000000000, 2)
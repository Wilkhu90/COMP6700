'''
Created on Sep 26, 2015

@author: sum
'''
import unittest
import CA02.prod.StarSensor as StarSensor
import CA02.prod.Environment as Environment


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def test100_010_ShouldConstruct(self):
        self.assertIsInstance(StarSensor.StarSensor(0.1), StarSensor.StarSensor)
        
    def test100_910ShouldRaiseExceptionOnInvalidFOV(self):
        with self.assertRaises(ValueError) as context:
            StarSensor.StarSensor(0)
    
    def test100_920ShouldRaiseExceptionOnMissingFOV(self):
        with self.assertRaises(ValueError) as context:
            StarSensor.StarSensor()        
            
    def test200_010_ShouldInitializeStarSensorWithStarFile(self):
        mySensor = StarSensor.StarSensor(0.1)
        self.assertEquals(mySensor.initializeSensor(starFile="SaoChart.txt"), 9040) 
        
    def test200_910ShouldRaiseExceptionOnMissingFileName(self):
        with self.assertRaises(ValueError) as context:
            mySensor = StarSensor.StarSensor(0.1)
            mySensor.initializeSensor()
            
    def test200_920ShouldRaiseExceptionOnIncorrectFileName(self):
        with self.assertRaises(ValueError) as context:
            mySensor = StarSensor.StarSensor(0.1)  
            mySensor.initializeSensor(starFile="Sao")
    
    def test200_930ShouldRaiseExceptionOnFileWithInvalidData(self):
        with self.assertRaises(ValueError) as context:
            mySensor = StarSensor.StarSensor(0.1)  
            mySensor.initializeSensor(starFile="SaoChartInvalid.txt")  
            
           
    def test200_940ShouldRaiseExceptionOnFileWithDuplicateData(self):
        with self.assertRaises(ValueError) as context:
            mySensor = StarSensor.StarSensor(0.1)  
            mySensor.initializeSensor(starFile="SaoChartDuplicate.txt")     
            
    def test200_950ShouldRaiseExceptionOnFileNameNotString(self):
        with self.assertRaises(ValueError) as context:
            mySensor = StarSensor.StarSensor(0.1)  
            mySensor.initializeSensor(starFile=2)     
            
            
    def test300_010_ShouldConfigureWithEnvironment(self):
        mySensor = StarSensor.StarSensor(0.1)
        env = Environment.Environment()
        env.setRotationalPeriod(1000000)
        self.assertEquals(mySensor.configure(env), True) 
        
    def test300_910ShouldRaiseExceptionOnMissingEnvironment(self):
        with self.assertRaises(ValueError) as context:
            mySensor = StarSensor.StarSensor(0.1)
            mySensor.configure()   
    
    def test300_920ShouldRaiseExceptionOnPassingNonEnvironmentInstance(self):
        with self.assertRaises(ValueError) as context:
            mySensor = StarSensor.StarSensor(0.1)
            env = 2
            mySensor.configure(env)    
            
    def test400_010_ShouldCalculateMagnitudeHexValueInitiallyWithDECAndRAZero(self):
        myEnv = Environment.Environment()
        myEnv.setRotationalPeriod(1000000)
        mySensor = StarSensor.StarSensor(0.1)
        mySensor.initializeSensor(starFile="SaoChart.txt")
        mySensor.configure(myEnv)
        self.assertEquals(mySensor.serviceRequest(), '0032')
        
    def test400_020_ShouldCalculateMagnitudeHexValueInitiallyWithDifferentFOV(self):
        myEnv = Environment.Environment()
        myEnv.setRotationalPeriod(1000000)
        mySensor = StarSensor.StarSensor(0.034906585)
        mySensor.initializeSensor(starFile="SaoChart.txt")
        mySensor.configure(myEnv)
        self.assertEquals(mySensor.serviceRequest(), '0035') 
        
    def test400_030_ShouldCalculateNoneMagnitudeHexValueIfNotConfigured(self):
        myEnv = Environment.Environment()
        myEnv.setRotationalPeriod(1000000)
        mySensor = StarSensor.StarSensor(0.034906585)
        mySensor.initializeSensor(starFile="SaoChart.txt")
        self.assertEquals(mySensor.serviceRequest(), None)    
    
    def test400_040_ShouldCalculateMagnitudeHexValueAtTwelthHour(self):
        myEnv = Environment.Environment()
        myEnv.setRotationalPeriod(1000000)
        myEnv.incrementTime(microseconds=43200000000)
        mySensor = StarSensor.StarSensor(0.034906585)
        mySensor.initializeSensor(starFile="SaoChart.txt")
        mySensor.configure(myEnv)
        self.assertEquals(mySensor.serviceRequest(), '0039')
    
    def test400_050_ShouldCalculateMagnitudeHexValueAtEighteenthHour(self):
        myEnv = Environment.Environment()
        myEnv.setRotationalPeriod(1000000)
        myEnv.incrementTime(microseconds=43200000000 + 21600000000)
        mySensor = StarSensor.StarSensor(0.034906585)
        mySensor.initializeSensor(starFile="SaoChart.txt")
        mySensor.configure(myEnv)
        self.assertEquals(mySensor.serviceRequest(), '8000')
                
    def test500_010_ShouldCalculateHexValueOfZero(self):
        mySensor = StarSensor.StarSensor(0.1)
        self.assertEquals(mySensor.convertHexadecimal(brightestStar=0), '0000') 
    
    def test500_020_ShouldCalculateHexValueOfOne(self):
        mySensor = StarSensor.StarSensor(0.1)
        self.assertEquals(mySensor.convertHexadecimal(brightestStar=1), '000a') 
        
    def test500_030_ShouldCalculateHexValueOfSixPointFiftyFive(self):
        mySensor = StarSensor.StarSensor(0.1)
        self.assertEquals(mySensor.convertHexadecimal(brightestStar=6.55), '0041') 
    
    def test500_040_ShouldCalculateHexValueOfNegativeTwenty(self):
        mySensor = StarSensor.StarSensor(0.1)
        self.assertEquals(mySensor.convertHexadecimal(brightestStar=-20), 'ff37')   
    
    def test500_050_ShouldCalculateHexValueOfNoStar(self):
        mySensor = StarSensor.StarSensor(0.1)
        self.assertEquals(mySensor.convertHexadecimal(brightestStar=None), None)  
        
    def test600_010_ShouldCalculateRAAndDECOfSensor(self):
        myEnv = Environment.Environment()
        myEnv.setRotationalPeriod(1000000)
        mySensor = StarSensor.StarSensor(0.034906585)
        mySensor.initializeSensor(starFile="SaoChart.txt")
        mySensor.configure(myEnv)
        output = [1.5707963267948966, 0.0]
        self.assertEquals(mySensor.getSensorPosition(), output)
        
    def test600_020_ShouldCalculateRAAndDECOfSensorAtTwelthHour(self):
        myEnv = Environment.Environment()
        myEnv.setRotationalPeriod(1000000)
        myEnv.incrementTime(microseconds=43200000000)
        mySensor = StarSensor.StarSensor(0.034906585)
        mySensor.initializeSensor(starFile="SaoChart.txt")
        mySensor.configure(myEnv)
        output = [4.71238898038469, 0.0]
        self.assertEquals(mySensor.getSensorPosition(), output)    
        
    def test600_030_ShouldCalculateRAAndDECAsNoneWhenNotConfigured(self):
        myEnv = Environment.Environment()
        myEnv.setRotationalPeriod(1000000)
        mySensor = StarSensor.StarSensor(0.034906585)
        output = [None, None]
        self.assertEquals(mySensor.getSensorPosition(), output)    
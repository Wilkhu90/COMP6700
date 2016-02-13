'''
Created on Oct 20, 2015

@author: sum
'''
import random
import bisect
import CA02.prod.Environment as Environment

class Device(object):
    
    def __init__(self):
        self.isConfigured = False
        self.env = None
    
    def configure(self, environment=None):
        if (environment == None):
            raise ValueError("Device.configure:  Input for environment is Mandatory.")
        if (isinstance(environment, Environment.Environment) == False):
            raise ValueError("Device.configure:  Please Input an appropriate Environment.")
        
        self.env = environment
        self.isConfigured = True
        return self.isConfigured
    
    def serviceRequest(self):
        if (self.isConfigured == False):
            raise ValueError("Device.serviceRequest:  Please Configure with appropriate Environment.")
        probabilities = [0.25, 0.5, 0.25]
        choice = self.probableChoice(probabilities)
        self.env.incrementTime(40)
        if choice == 0:
            return self.convertHexadecimal(0)
        elif choice == 1:
            return self.convertHexadecimal((int)(random.uniform(0, 32767)))
        elif choice == 2:
            return self.convertHexadecimal((int)(random.uniform(32767, 65535)))          
        
    
    def probableChoice(self, probabilities):
        localSum = []
        runningSum = 0
        
        for probability in probabilities:
            runningSum += probability
            localSum.append(runningSum)
    
        randomNumber = random.random() * runningSum
        return bisect.bisect_right(localSum, randomNumber)
    
    def convertHexadecimal(self, brightestStar=None):
        if (brightestStar == None):
            return None
        
        elif (brightestStar>=0):
            return format(int(brightestStar), '04x')
        
        else:
            newString = ''
            binString = format(int(abs(brightestStar)), '016b')
            for i in range(len(binString)):
                if binString[i] == '1':
                    newString = newString + '0'
                elif binString[i] == '0':
                    newString = newString + '1'
                
            return format(int(newString, 2), '04x')
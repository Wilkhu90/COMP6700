'''
Created on Sep 27, 2015

@author: sum
'''
import CA02.prod.StarSensor as StarSensor                
from CA02.prod import Environment
import CA01.prod.StarCatalog as StarCatalog
import math

ss = StarSensor.StarSensor(0.034906585)
a = ss.initializeSensor(starFile='SaoCharts.txt')

env = Environment.Environment()
a = env.getTime()
env.setRotationalPeriod(microseconds=1000000)


c = ss.configure(env)


sCat = StarCatalog.StarCatalog()
sCat.loadCatalog(starFile='SaoCharts.txt')
s = sCat.getMagnitude(0, math.pi/2, 0.034906585)
print 24*60*60*1000000/2
print env.getTime()
print 'yo'
x = ss.serviceRequest()
print 'yo'
print x
print env.getTime()
env.incrementTime(21600000000*3 - env.getTime())
print 'yo'
print env.getTime()
x = ss.serviceRequest()
print x


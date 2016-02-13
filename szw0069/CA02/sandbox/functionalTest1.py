import CA02.prod.StarSensor as StarSensor                
import CA02.prod.Environment as Environment                
import math                
                
# instantiate the simulation environment                
simEnv = Environment.Environment()                
                
# rotate the satellite 6 times per minute                 
# = 10 seconds per rotation = 10000000 microseconds per rotation             
simEnv.setRotationalPeriod(int(60 / 6 * 1000000))                
                
# instantiate the star sensor with a 2-degree field of view                
# 2 degrees = 2*pi*2/360 radians                
fov = (10.0 / 360.0) * 2.0 * math.pi                # convert to radians
sensor = StarSensor.StarSensor(fov)                
sensor.initializeSensor(starFile='SaoCharts.txt')                
# give the star sensor access to environmental information                
sensor.configure(simEnv)                
a = sensor.getSensorPosition()        
print a        
# build a list of the brightest magnitudes detected at 10 second intervals for 5 minutes of simulated time                
# note 1:    Times are expressed in microseconds                
# note 2:    Since we are simulating a physical sensor, we have to account for the amount of                
#            time the sensor takes to respond with a result.  When we get get a response                
#            from the sensor, the simulated time has been advanced by the response time.                
#            We have to take account this latency if we want to take a star sighting                 
#            at specific intervals.                   
simEnv.incrementTime(42)
a = sensor.getSensorPosition()        
print a  
amountOfRotation = int(simEnv.getRotationalPeriod() / 4.0) + 1
simEnv.incrementTime(amountOfRotation)
sensor.configure(simEnv)                
a = sensor.getSensorPosition()        
print a     

amountOfRotation = int(simEnv.getRotationalPeriod() / 2.0) + 1
simEnv.incrementTime(amountOfRotation)
sensor.configure(simEnv)                
a = sensor.getSensorPosition()        
print a     
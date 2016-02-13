'''
Created on Oct 31, 2015

@author: sum
'''
import CA03.prod.Monitor as Monitor
import CA03.prod.Device as Device
import CA02.prod.StarSensor as StarSensor
import CA02.prod.Environment as Environment
import CA04.prod.SolarCollector as SolarCollector

class ComponentFactory(object):
    
    def __init__(self, component):
        self.component = component
        self.instance = None
        
    def getComponent(self):
        if(self.component['component'] == "Environment"):
            self.instance = Environment.Environment()
            parms = self.component['parms']
            if len(parms) == 0:
                raise ValueError("Controller.initialize:  Environment requires additional information.")
            for parm in parms:
                if (str(parm['name']) == 'rotationalPeriod') and (parm['value'] != None):
                    self.instance.setRotationalPeriod((int) (parm['value']))
                elif (str(parm['name']) == 'startTime') and (parm['value'] != None):
                    self.instance.setStartTime((int) (parm['value']))
                elif (str(parm['name']) == 'degradation') and (parm['value'] != None):
                    self.instance.setDegradation((int) (parm['value']))
                else:
                    raise ValueError("Controller.initialize:  Environment requires additional information.")
            return self.instance
            
        elif(self.component['component'] == "Monitor"):
            self.instance = Monitor.Monitor()
            parms = self.component['parms']
            if len(parms) == 0:
                raise ValueError("Controller.initialize:  Monitor requires additional information.")
            for parm in parms:
                if (str(parm['name']) == 'logFile'):
                    self.instance.initialize(str(parm['value']))
                else:
                    raise ValueError("Controller.initialize:  Monitor requires additional information.")
            return self.instance
        
        elif(self.component['component'] == "StarSensor"):
            parms = self.component['parms']
            if len(parms) != 2:
                raise ValueError("Controller.initialize:  StarSensor requires additional information.")
            for parm in parms:
                if (str(parm['name']) == 'fieldOfView'):
                    self.instance = StarSensor.StarSensor((float)(parm['value']))
                elif (str(parm['name']) == 'starFile'):
                    pass    
                else:
                    raise ValueError("Controller.initialize:  StarSensor requires additional information.")
            for parm in parms:
                if (str(parm['name']) == 'starFile'):
                    self.instance.initializeSensor(str(parm['value']))
                elif (str(parm['name']) == 'fieldOfView'):
                    pass
                else:
                    raise ValueError("Controller.initialize:  StarSensor requires additional information.")
            return self.instance
        
        elif(self.component['component'] == "Device"):
            self.instance = Device.Device()
            return self.instance
        elif(self.component['component'] == "SolarCollector"):
            self.instance = SolarCollector.SolarCollector()
            return self.instance
        else:
            raise ValueError("Controller.initialize:  The device(s) mentioned in XML is incorrect.")  
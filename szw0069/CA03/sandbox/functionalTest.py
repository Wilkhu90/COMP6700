
import CA03.prod.Controller as Controller



theController = Controller.Controller()
deviceList = theController.initialize("frameConfiguration.xml")
for device in deviceList:
    print(device)
runTime = theController.run(1000)
print('The simulation ran for {0} microseconds'.format(runTime))    

'''
Created on Oct 31, 2015

@author: sum
'''
from xml.dom.minidom import  parse

class Architecture(object):

    def __init__(self, fileName):
        self.fileName = fileName
        source = open(fileName)
        try:
            self.domTree = parse(source)
        except:
            raise ValueError("Controller.initialize:  invalid XML")
        
    def getComponentDefinition(self):
        components = self.parseDefinitionTags(self.domTree)
        return components
        
    def parseDefinitionTags(self, domTree):
        components = []
        definitionTags = domTree.getElementsByTagName("definition")
        for tag in definitionTags:
            components.append(self.parseDefinitionTag(tag))
        return components
 
    def parseDefinitionTag(self, definitionTag):
        component = {}
        if (not (definitionTag.hasAttribute('component'))):
            raise ValueError("Controller.initialize: definitionTag tag has no component attribute")
        component['component'] = definitionTag.getAttribute('component')
        parmTags = definitionTag.getElementsByTagName('parm')
        component['parms'] = self.parseParmTags(parmTags)
        return component 
        
    def parseParmTags(self, parmTags):
        parameters = []
        for tag in parmTags:
            parameters.append(self.parseParmTag(tag))
        return parameters
    
    def parseParmTag(self, parmTag):
        if (not (parmTag.hasAttribute('name'))):
            raise ValueError("Controller.initialize: tag tag has no name attribute")
        parmName = parmTag.getAttribute('name')
        parmValue = self.parseContent(parmTag.childNodes)
        return({'name': parmName, 'value': parmValue})
        
            
    def parseContent(self, domSubTree):
        for node in domSubTree:
            if node.nodeType == node.TEXT_NODE:
                return node.data
        return None   
    
    def getFrameInformation(self):
        frame = self.parseFrameTags(self.domTree)
        return frame
        
    def parseFrameTags(self, domTree):
        frames = []
        frameTags = domTree.getElementsByTagName("frame")
        for tag in frameTags:
            frames.append(self.parseFrameTag(tag))
        return frames
    
    def parseFrameTag(self, frameTag):
        devices = []
        if (not (frameTag.hasAttribute('rate'))):
            raise ValueError("Controller.initialize: frameTag tag has no rate attribute")

        rate = frameTag.getAttribute('rate')
        devices.append(rate)
        
        deviceTags = frameTag.getElementsByTagName('device')
        if (len(deviceTags) != (len(frameTag.childNodes)-1)/2):
            raise ValueError("Controller.initialize: frameTag has attributes other than device attribute")
        
        for deviceTag in deviceTags:
            devices.append(self.parseContent(deviceTag.childNodes))
        
        return devices 
    
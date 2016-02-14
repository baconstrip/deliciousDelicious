class Display:
    def __init__(self, name, data):
        self.layout = []
        self.data = data
        self.name = name

    def getData(self):
        return self.data
    
    def getLayout(self):
        return self.layout
    
    def getName(self):
        return self.name

    def addElement(self,element):
        self.layout.append(element)

    # Override me!
    # Should return a tuple, (status_summary, code)
    # where status_summary is a short, human readable status report
    # and code is 0, 1, 2, or 3
    # None or 0 makes the background green, 3 makes the background Red
    def update(self, delta):
        pass

    def updateLayout(self, name, field):
        for element in self.layout:
            if element.name == name:
                if element.elementType == 'label':
                    element.text = field
                elif element.elementType == 'value':
                    element.value = field
                elif element.elementType == 'percentBar':
                    element.percentage = field
                elif element.elementType == 'container':
                    element.removeAll()
                    element.elements = field

        return

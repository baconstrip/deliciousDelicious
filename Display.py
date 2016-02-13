class Display:
    def __init__(self):
        self.layout = []

    def getLayout(self):
        return self.layout

    def addElement(self,element):
        self.layout.append(element)

    def updateLayout(self, name, field):
        for element in self.layout:
            if element.name == name:
                if element.elementType == 'label':
                    element.text = field
                elif element.elementType == 'value':
                    element.value = field
                elif element.elementType == 'percentageBar':
                    element.percentage = field
                elif element.elementType == 'container':
                    element.removeAll()
                    element.elements = field

        return

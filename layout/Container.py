from layout.LayoutElement import LayoutElement as Element

class Container(Element):
    def __init__(self, name, index):
        Element.__init__(self, name,index)
        self.elements=[]
        elementType='container'

    def getLayout(self):
        return self.elements

    def addElement(self, element):
        self.elements.append(element)

    def removeElement(self, name):
        for element in self.elements:
            if name == element.getName():
                self.elements.remove(element)
                return
    def removeAll(self):
        for element in self.elements:
            self.elements.remove(element)
        return

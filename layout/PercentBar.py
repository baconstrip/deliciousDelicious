from layout.LayoutElement import LayoutElement as Element

class PercentBar(Element):

    def __init__(self, name, index, percent= None, newColor= "blue"):
        Element.__init__(self,name, index)
        self.percentage = percent
        self.elementType = 'percentBar'
        self.color = newColor

    def getPercentage(self):
        return self.percentage

    def getColor(self):
        return self.color


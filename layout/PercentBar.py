from layout.LayoutElement import LayoutElement as Element

class PercentBar(Element):

    def __init__(self, name, index, percent= None):
        Element.__init__(self,name, index)
        self.percentage = percent

    def getPercentage():
        return self.percentage


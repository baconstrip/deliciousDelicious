from layout.LayoutElement import LayoutElement as Element

class Value(Element):
    def __init__(self, name, index, value = None):
        Element.__init__(self, name,index)
        self.value = value
        self.elementType = 'Value'


    def getValue(self):
        return self.value


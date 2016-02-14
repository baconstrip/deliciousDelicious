from layout.LayoutElement import LayoutElement as Element

class Label(Element):
    def __init__(self, name, index, text = None, newColor="white"):
        Element.__init__(self, name, index)
        self.text = text
        self.elementType = 'label'
        self.color = newColor

    def getText(self):
        return self.text	

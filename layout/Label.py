from layout.LayoutElement import LayoutElement as Element

class Label(Element):
    def __init__(self, name, index, text = None):
        Element.__init__(self, name, index)
        self.text = text
        
    def getText():
        return self.text

	

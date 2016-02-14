class LayoutElement:
    def __init__(self, initName, initIndex):
        self.name = initName
        self.index = initIndex
        self.elementType = 'default'
    def getIndex(self):
        return self.index
    def getName(self):
        return self.name

from Display import Display
from layout.Container import Container
from layout.Label import Label
from layout.PercentBar import PercentBar
from layout.Value import Value

class Test(Display):
    name = "test"

    def __init__(self): 
        Display.__init__(self)
        self.addElement(Container("Container", 0))	
        self.addElement(Label("Label", 1))
        self.addElement(PercentBar("PercentageBar", 2))
        self.addElement(Value("Value", 3))
		

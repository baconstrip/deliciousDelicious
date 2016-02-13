from Display import Display
from layout.Container import Container
from layout.Label import Label
from layout.PercentBar import PercentBar
from layout.Value import Value

class Test(Display):
    name = "test"

    def __init__(self, data): 
        Display.__init__(self, data)
        self.addElement(Container("Container", 0))	
        self.addElement(Label("Label", 1, "test"))
        self.addElement(PercentBar("PercentageBar", 2, 10))
        self.addElement(Value("Value", 3, 5))
		

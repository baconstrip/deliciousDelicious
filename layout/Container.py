from layout.LayoutElement import LayoutElement as Element

class Container(Element):
	elements=[]
	def addElement(self, element):
		elements.append(element)
	def removeElement(self, name):
		for element in elements:
			if name == element.getName():
				elements.remove(element)
				return
		return



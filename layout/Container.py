class Container(LayoutElement):
	elements=[]
	def addElement(element):
		elements.append(element)
	def removeElement(name):
		for element in elements:
			if name == element.getName():
				elements.remove(element)
				return
		return



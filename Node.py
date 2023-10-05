class Node:
	name=str()
	pwd=str()
	children=list()
	isFolder=bool()
	isHidden=bool()
	def __init__(self,name,pwd,isFolder,isHidden):
		self.name=name
		self.pwd=pwd
		self.isFolder=isFolder
		self.isHidden=isHidden
		self.children=[]

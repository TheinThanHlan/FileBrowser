import os
from Node import Node

count=0
def parse(cwd):
	global count;
	pathLevel=[]
	if os.path.isdir(cwd):	
		tmp = os.listdir(cwd)
		pathLevel.append(Node(name=cwd.split('/')[-1],pwd=cwd,isFolder=os.path.isdir(cwd),isHidden=False))
		for a in tmp:
			pathLevel[-1].children.append(parse(cwd+'/'+a))
		return pathLevel.pop()

	
	else:	
		return Node(name=cwd.split('/')[-1],pwd=cwd,isFolder=os.path.isdir(cwd),isHidden=False)


def parseB(cwd):
	tmp  = os.listdir(cwd)
	root = Node(name=cwd.split('/')[-1],pwd=cwd,isFolder=os.path.isdir(cwd),isHidden=False)
	for a in tmp:
		print(a)
		root.children.append(Node(name=a,pwd=cwd+'/'+a,isFolder=os.path.isdir(cwd+'/'+a),isHidden=False))
	return root

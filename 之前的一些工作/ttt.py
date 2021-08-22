class Tree():
    _tree = [{}]
    root = _tree
    _tree[0]['name']='root'
    def __init__(self):
        pass
    def has_child(self,node):
        if len(node)>1:
            return True
        else:
            return False

    def has_brother():
        pass
    def get_childs(self,node):
        if len(node)==0:
            return
        return node
        pass

    def get_parent(self,node):
        pass

    def get_brothers(self,node):
        pass

    def add_child(self,node,child):
        child_node = [{}]
        child_node.append([child])
        node = node.append(child_node)
        pass

    def add_brother(self,node):
        pass

# exp = Tree()
# root = exp._tree
# print(exp.has_child(root))
# exp.add_child(root,'son')
# print(exp.has_child(root))
# exp.add_child(root,'son1')
# print(root)



class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children =[]
        self.parent= None
        
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
        print(child.parent.data,'parent')
        print(self.children[0].data,'children')
        

def build_product_tree():
    root = TreeNode('Electronics')
    laptop = TreeNode('Laptop')
    root.add_child(laptop)
    print(root.data,'rootNode')
    


if __name__ == '__main__':
    build_product_tree()
    
        
        
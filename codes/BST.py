class Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right == None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left == None:
                root.left = node
            else:
                insert(root.left, node)

def inorder(root):
    if root:
        print(root.data)
        inorder(root.left)
        inorder(root.right)
        print(root.data)

    
r = Node(50)
insert(r,Node(70)) 
insert(r,Node(20)) 
insert(r,Node(80)) 
insert(r,Node(30)) 
insert(r,Node(60)) 
insert(r,Node(40)) 

print(r)

inorder(r)
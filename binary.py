class BinaryTreeNode:
    
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

    def insert_left(self,value):
        self.left = BinaryTreeNode(value)
        return self.left    

    def insert_right(self,value):
        self.right = BinaryTreeNode(value)
        return self.right

root = BinaryTreeNode(1)
l1 = root.insert_left(2)
r1 = root.insert_right(3)

def is_balanced(tree_root):
    
    depths = []

    nodes = []
    nodes.append((tree_root,0))

    while(len(nodes)):

        node,depth = nodes.pop()

        if (not node.left) and (not node.right):
            depths.append(depth)

            if (len(depths) > 2) or (len(depths) ==2 and abs(depths[0]-depths[1])>1):
                return False

        else:
            if node.left:
                nodes.append((node.left,depth+1))
            elif node.right:
                nodes.append((node.right,depth+1))
    return True                            

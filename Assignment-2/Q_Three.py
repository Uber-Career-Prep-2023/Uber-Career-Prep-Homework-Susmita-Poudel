#Binary Seach Tree

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#Time complexity: 0(logn)
def min(root):
    if root is None:
        return None
    
    while root.left!= None:
        root = root.left
    return root.val

#Time complexity: 0(logn)
def max(root):
    if root is None:
        return None
    
    while root.right != None:
        root = root.right
    return root.val

#Time complexity: 0(logn)
def contains(root,val):
    bool_val_present = False

    while root != None:

        if val > root:
            root = root.right
        
        elif val < root:
            root = root.left

        else:
            return bool_val_present == True
        
    return bool_val_present

#Time complexity: 0(logn)
def insert(n, val):
    
    if n== None:
        return Node(n)
    elif val < n.val:
        n.left = insert(n.left, val)
    else:
        n.right = insert(n.right, val)

    return n

#Time complexity: 0(logn)
def delete(root, val):

    if root == None:
        return root
    
    if val < root.left:
        root.left = delete(root.left, val)
        return root

    elif val >= root.right:
        root.right = delete(root.right, val)
        
    
    if root.val == val:
        #If root  is a leaf node
        if root.left is None and root.right is None:
            return None
    
        #If one of the children is empty
        if root.left is None:
            temp = root.right
            root = None
            return root.right
    
        elif root.right is None:
            temp = root.left
            root = None
            return root.left
        
        #If root has both children
        successor = root.right
        while successor.left !=None:
            successor = root.left
            root.val = successor.val
            root.right = delete(root.right, root.val)

    return root

        
     
    
    



    

    

    



    



    

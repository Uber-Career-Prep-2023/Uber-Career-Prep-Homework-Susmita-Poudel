#Question 10: LeftView
#Given a binary tree, create an array of the left view (leftmost elements in each level) of the tr
#Breadth-first search
#Time-complexity: 0(n)     Space-complexity: 0(n), n = number of nodes
import queue
class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

left_nodes = []

def leftViewBFS(n):
    if n is None:
        return None
    
    if n.left is None and n.right is None:
        return n.val
    q = queue.Queue()
    level = 0
    q.put((n,0))
 
    while not q.empty():
        node, level = q.get()
     
        if level == len(left_nodes):
            left_nodes.append(node.val)
          
        if node.left is not None:
            q.put((node.left, level +1))
            
        if node.right is not None:
            q.put((node.right, level +1))

    return left_nodes
        

                

def main():
    #Testcase 1
    root = Node(7)
    root.left = Node(8)
    root.right = Node(3)
    root.right.left = Node(9)
    root.right.right = Node(13)
    root.right.left.left = Node(20)
    root.right.right.left = Node(14)
    root.right.right.left.right = Node (15)

    #print(leftViewBFS(root))
    #Testcase 2
    root = Node(7)
    root.left = Node(20)
    root.right = Node(4)
    root.left.left = Node(15)
    root.left.right = Node(4)
    root.right.left = Node(8)
    root.right.right = Node(11)

    #print(leftViewBFS(root))

    #Empty tree
    r= None
    #print(leftViewBFS(r))
    

    #Only has a root
    r1 = Node(100)
    #print(leftViewBFS(r1))

    #Tree with only one level
    r2 = Node(100)
    r2.left = Node(200)
    r2.right = Node(5)
    print(leftViewBFS(r2))






if __name__ == '__main__':
    main()


#Time-spent: 39 minutes   

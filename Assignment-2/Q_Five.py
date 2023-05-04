#Question 5: IsBST
#Given a binary tree, determine if it is a binary search tree.
#Time-complexity: 0(n); Space- complexity: 0(n)
#In-order traversal
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def isBST(root):
    all_nodes_sorted = []
    def inOrder(node):
        if node is None:
            return True
    
        inOrder(node.left)
        all_nodes_sorted.append(node.val)
        inOrder(node.right)

    inOrder(root)
    for i in range(len(all_nodes_sorted)-1):
        if all_nodes_sorted[i] >= all_nodes_sorted[i+1]:
            return False

    return True

def main():
    root = Node(10)
    root.left = Node(8)
    root.left.right = Node(9)
    root.right = Node(16)
    root.right.left = Node(13)
    root.right.right = Node(17)
    root.right.right.right = Node(20)

    print(isBST(root))

    root2 = Node(10)
    root2.left = Node(8)
    root2.left.right = Node(9)
    root2.right = Node(16)
    root2.right.left = Node(13)
    root2.right.right = Node(17)
    root2.right.right.right = Node(15)

    print(isBST(root2))
    #Only root
    root3 = Node(10)
    print(isBST(root3))

    #Empty tree
    root4 = None
    print(isBST(root4))

    #Not a binary tree
    root5 = Node(20)
    root5.left = Node(10)
    root5.right = Node(15)
    print(isBST(root5))




if __name__ == '__main__':
    main() 
    

#Time_taken: 30 minutes


  




   


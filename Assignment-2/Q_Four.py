#Given a binary tree, create a deep copy. Return the root of the new tree.
#Time complexity: 0(n), Spcae-complexity: 0(n)where n = number of nodes in the tree
#Technique used: Depth-First: Pre-order traversal
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

#This function is used for testcases to see if our cloned binary tree is same as the original tree
#In-order traversal
def inOrder(root):
    if root == None:
        return 
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)

#Function to create a deep copy
def cloneBinaryTree(root):

    if root == None:
        return
    copy_root = Node(root.val)
    copy_root.left = cloneBinaryTree(root.left)
    copy_root.right = cloneBinaryTree(root.right)

    return copy_root

 
#Test-cases
def main():

    #Binary tree with null nodes
    root = None
    new_root = cloneBinaryTree(root)
    assert new_root == None

    #Binary tree with only one node
    root1 = Node(5)
    new_root1 = cloneBinaryTree(root1)
    assert new_root1.val == root1.val
    assert new_root1.left == None
    assert new_root1.right == None


    #Binary tree with left and right nodes
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
    new_root = cloneBinaryTree(root2)
    print("Inorder traversal for original tree: ")
    inOrder(root2)
    print("Inorder traversal for cloned tree: ")
    inOrder((new_root))

    #Binary tree with only left child
    root3 = Node(1)
    root3.left = Node(2)
    root3.left.left= Node(3)
    root3.left.left.left = Node(4)
    new_root3 = cloneBinaryTree(root3)
    print("Inorder traversal for original tree: ")
    inOrder(root3)
    print("Inorder traversal for cloned tree: ")
    inOrder((new_root3))

     #Binary tree with only right children
    root4 = Node(10)
    root4.right = Node(20)
    root4.right.right= Node(20)
    root4.right.right.right = Node(40)
    new_root4 = cloneBinaryTree(root4)
    print("Inorder traversal for original tree: ")
    inOrder(root4)
    print("Inorder traversal for cloned tree: ")
    inOrder((new_root4))

    #Binary Search tree
    root5 = Node(100)
    root5.left = Node(50)
    root5.right = Node(200)
    new_root5 = cloneBinaryTree(root5)
    print("Inorder traversal for original tree: ")
    inOrder(root5)
    print("Inorder traversal for cloned tree: ")
    inOrder((new_root5))

if __name__ == '__main__':
    main()

#Time taken: 33 minutes
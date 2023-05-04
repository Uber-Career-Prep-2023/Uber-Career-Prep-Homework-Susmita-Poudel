#Question 11: FloorInBST
#Given a target numeric value and a binary search tree, return the floor (greatest element less than or equal to the target) in the BST.
#BST Search
#Time-complexity: 0(logn)       Space-complexity: 0(1)
class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def floorInBST(n, target):
    if n is None:
        return None
    
    if n.val == target:
        return n.val
    
    elif n.val > target:
        return floorInBST(n.left, target)
    
    else:
        right_subtree_floor = floorInBST(n.right, target)
        if right_subtree_floor is not None and right_subtree_floor <= target:
            return right_subtree_floor
        else:
            return n.val
    
  
def main():
    root = Node(10)
    root.left = Node(7)
    root.right = Node(16)
    root.left.right = Node(8)
    root.right.left = Node(13)
    root.right.right = Node(17)
    root.right.right.right = Node(20)

    print(floorInBST(root,13))
    print(floorInBST(root,15))
    print(floorInBST(root,11))
    print(floorInBST(root,9))
   

if __name__ == '__main__':
    main()

#Time-spent: 40 minutes
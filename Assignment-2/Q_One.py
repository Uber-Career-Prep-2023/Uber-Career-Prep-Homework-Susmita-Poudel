class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    #creates new Node with data val at front; returns new head
    #time-complexity: O(1)
    def insertAtFront(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            return self.head
        new_node.next = self.head
        self.head = new_node
        return self.head
    
    #creates new Node with data val at end
    #time-complexity:0(n), n = length of linked list
    def insertAtBack(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            return
        
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next

        curr_node.next = new_node

    #creates new Node with data val after Node loc
    #time-complexity: 0(n), n = length of linked list
    def insertAfter(self,val,loc):
        new_node = Node(val)
        curr = self.head
        while curr != loc and curr != None:
            curr = curr.next

        if curr == None:
            return
        new_node.next = curr.next
        curr.next = new_node

    #removes first Node; returns new head
    #time-complexity:0(1)
    def deleteFront(self):
        if self.head == None:
            return None
        if self.head.next == None:
            self.head = None
            return None

        self.head = self.head.next
        return self.head
    
    #removes last Node
    #time-complexity: 0(n), n = length of linked list
    def deleteBack(self):
        if self.head == None:
            return
        
        if  self.head.next == None:
            self.head = None
            return

        curr = self.head
        while curr.next.next != None:
            curr = curr.next
        curr.next = None

    #deletes Node loc; returns head
    #time-complexity:0(n), n = length of linked list
    def deleteAfter(self,loc):
        if self.head is None:
            return None
        
        curr = self.head
        while curr.next != loc and curr.next != None:
            curr = curr.next
        if curr.next != loc:
            return self.head
        
        curr.next = curr.next.next
        return self.head
    
    #returns length of the list
    #time-complexity: 0(n), n = length of linked list
    def length(self):
        if self.head is None:
            return 0
        
        i_count = 0
        curr = self.head
        while curr != None:
            i_count += 1
            curr = curr.next

        return i_count
    
    #reverses the linked list iteratively
    #time-complexity: 0(n)
    def reverseIterative(self): 
        if self.head == None or self.head.next == None:
            return self.head
        
        curr = self.head
        prev = None

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        return self.head

    #reverse the linked list recursively
    #time-complexity:0(n)
    def reverseRecursion(self):
        if self.head is None or self.head.next is None:
            return self.head

        #helper function
        def recursiveReverseHelper(prev, curr):

            if curr.next is None:
                curr.next = prev
                return curr
        
            next = curr.next
            curr.next = prev
            tail = recursiveReverseHelper(curr,next)
            return tail
     
        self.head = recursiveReverseHelper(None,self.head)



#Test-cases
import unittest

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.llist = LinkedList()

    def test_insertAtFront(self):
        self.llist.insertAtFront(1)
        self.assertEqual(self.llist.head.val, 1)

        self.llist.insertAtFront(2)
        self.assertEqual(self.llist.head.val, 2)
        self.assertEqual(self.llist.head.next.val, 1)

    def test_insertAtBack(self):
        self.llist.insertAtBack(1)
        self.assertEqual(self.llist.head.val, 1)

        self.llist.insertAtBack(2)
        self.assertEqual(self.llist.head.val, 1)
        self.assertEqual(self.llist.head.next.val, 2)

    def test_insertAfter(self):
        self.llist.insertAtBack(1)
        self.llist.insertAtBack(2)
        self.llist.insertAtBack(3)

        node_2 = self.llist.head.next
        self.llist.insertAfter(4, node_2)
        self.assertEqual(self.llist.head.val, 1)
        self.assertEqual(self.llist.head.next.val, 2)
        self.assertEqual(self.llist.head.next.next.val, 4)
        self.assertEqual(self.llist.head.next.next.next.val, 3)

    def test_deleteFront(self):
        self.llist.insertAtBack(5)
        self.llist.deleteFront()
        self.assertEqual(self.llist.head, None)

        self.llist.insertAtBack(1)
        self.llist.insertAtBack(2)
        self.llist.deleteFront()
        self.assertEqual(self.llist.head.val, 2)

    def test_deleteAfter(self):
        node_1 = self.llist.head
        self.llist.deleteAfter(node_1)
        self.assertEqual(self.llist.head, None)

        self.llist.insertAtBack(1)
        self.llist.insertAtBack(2)
        self.llist.insertAtBack(3)
        node_2 = self.llist.head.next
        self.llist.deleteAfter(node_2)
        self.assertEqual(self.llist.head.next.val, 3)

    def test_length(self):
    
        self.assertEqual(self.llist.length(), 0)

        self.llist.insertAtBack(1)
        self.llist.insertAtBack(2)
        self.llist.insertAtBack(3)
        self.assertEqual(self.llist.length(), 3)

    def test_reverseIterative(self):

        self.assertEqual(self.llist.head, None)
        self.llist.insertAtBack(1)
        self.assertEqual(self.llist.head.val, 1)
        self.llist.insertAtBack(2)
        self.llist.insertAtBack(3)
        self.llist.reverseIterative()
        self.assertEqual(self.llist.head.val, 3)
        self.llist.reverseRecursion()
        self.assertEqual(self.llist.head.val,1)



if __name__ == '__main__':
    unittest.main()
       

        
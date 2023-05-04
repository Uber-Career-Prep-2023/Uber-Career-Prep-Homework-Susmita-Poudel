#Question 6: DedupSortedList
#Given a sorted singly linked list, remove any duplicates so that no value appears more than once.
#Linked List fast-slow technique: However, I felt more comfortable with my way of using them which necessarily doesn't make two pointers instead just use next
#Time complexity: 0(n), where n = number of nodes Space-complexity: 0(1)
import queue
class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insertAtBack(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            return
        
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def deleteDuplicates(self):

        curr = self.head
       
        if curr is None:
            return  None
        
        while curr.next:

            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return self.head
      

    def printList(self):
        curr = self.head

        while curr is not None:
            print(curr.val, end = ' ')
            curr = curr.next
        print()
     
    

def main():
    llist = LinkedList()
    llist.insertAtBack(1)
    llist.insertAtBack(2)
    llist.insertAtBack(2)
    llist.insertAtBack(4)
    llist.insertAtBack(5)
    llist.insertAtBack(5)
    llist.insertAtBack(5)
    llist.insertAtBack(10)
    llist.insertAtBack(10)

    llist.deleteDuplicates()
    llist.printList()
    #Linked list with only repeating elements
    l1 = LinkedList()
    l1.insertAtBack(20)
    l1.insertAtBack(20)
    l1.insertAtBack(20)
    l1.insertAtBack(20)

    l1.deleteDuplicates()
    l1.printList()

    #only repeated at the end of linked list
    l2 = LinkedList()
    l2.insertAtBack(2)
    l2.insertAtBack(20)
    l2.insertAtBack(200)
    l2.insertAtBack(25)
    l2.insertAtBack(25)
    l2.insertAtBack(25)

    l2.deleteDuplicates()
    l2.printList()

    


if __name__ == '__main__':
    main()


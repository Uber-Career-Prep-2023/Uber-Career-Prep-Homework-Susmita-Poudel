#Question 7: MoveNthLastToFront
#Given a singly linked list, move the nth from the last element to the front of the list.
#Fixed-Distance two pointer technique
#Time-Complexity: 0(n), where n = number of nodes   Space- Complexity: 0(1)

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
class LinkedList():

    def length(self):
        if self.head is None:
            return 0
        
        i_count = 0
        curr = self.head
        while curr != None:
            i_count += 1
            curr = curr.next

        return i_count
    
    def moveNthLasttoFront(self, k):

        list_length = self.length()
        if k > list_length or k <= 0:
            return None
        
        if k == list_length:
            return self.head
        first_pointer = self.head
        second_pointer = self.head

        while list_length > k + 1:
            second_pointer = second_pointer.next
            list_length -=1

        temp = second_pointer.next
        if temp.next != None:
            second_pointer.next = second_pointer.next.next
        else:
            second_pointer.next = None

        temp.next = first_pointer
        self.head = temp

        return self.head
    
    def printList(self):
        curr = self.head

        while curr is not None:
            print(curr.val, end = ' ')
            curr = curr.next
        print()
    

def main():
    llist = LinkedList()
    llist.head = Node(15)
    llist.head.next = Node(2)
    llist.head.next.next = Node(8)
    llist.head.next.next.next = Node(7)
    llist.head.next.next.next.next = Node(20)
    llist.head.next.next.next.next.next = Node(9)
    llist.head.next.next.next.next.next.next = Node(11)
    llist.head.next.next.next.next.next.next.next = Node(6)
    llist.head.next.next.next.next.next.next.next.next = Node(19)
    #Prints original list

    llist.printList()
    #Test-case 1
    print(llist.moveNthLasttoFront(2))
    llist.printList()
    #Test-case 2
    print(llist.moveNthLasttoFront(7))
    llist.printList()
    #Additional test-case: Trying to move last element to the front
    print(llist.moveNthLasttoFront(1))
    llist.printList()

    #Test- case with only two elements
    l1 = LinkedList()
    l1.head = Node(15)
    l1.head.next = Node(2)
    print(l1.moveNthLasttoFront(1))
    l1.printList()
    #Test-case with only element with k > 1
    l = LinkedList()
    l.head = Node(100)
    l.moveNthLasttoFront(10)
    l.printList()

if __name__ == '__main__':
    main()

#Time-taken: 30 minutes
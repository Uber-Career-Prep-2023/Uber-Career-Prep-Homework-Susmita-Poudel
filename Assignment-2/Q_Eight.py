#Question 8: IsPalindrome
#Given a doubly linked list, determine if it is a palindrome.
#Doubly Linked List Forward- Backward Two-Pointer
#Time-Complexity: 0(n), where n is number of nodes     Space-Complexity: 0(1)

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
        self.head = None

    def traverse(self):
        curr = self.head
        length = 1
        while curr.next != None:
            curr = curr.next
            length += 1

        return curr, length
    
    def isPalindrome(self):
        if self.head is None or self.head.next is None:
            return True

        first_pointer = self.head
        first_pointer_index = 0
        l = self.traverse()
        second_pointer = l[0]
        second_pointer_index = l[1]-1
    
        while first_pointer_index < second_pointer_index:

            if first_pointer.val == second_pointer.val:
                first_pointer = first_pointer.next
                first_pointer_index +=1
                second_pointer = second_pointer.prev
                second_pointer_index -= 1
            else:
            
                return False

        return True
    

def main():
    #Palindrome
    llist = doubly_linked_list()
    llist.head = Node(9)
    llist.head.prev = None
    llist.head.next = Node(2)
    llist.head.next.prev = llist.head
    llist.head.next.next = Node(4)
    llist.head.next.next.prev = llist.head.next
    llist.head.next.next.next = Node(2)
    llist.head.next.next.next.prev = llist.head.next.next
    llist.head.next.next.next.next = Node(9)
    llist.head.next.next.next.next.prev = llist.head.next.next.next

    print(llist.isPalindrome()) 

    #Not palindrome 
    llist = doubly_linked_list()
    llist.head = Node(9)
    llist.head.prev = None
    llist.head.next = Node(2)
    llist.head.next.prev = llist.head
    llist.head.next.next = Node(4)
    llist.head.next.next.prev = llist.head.next
    llist.head.next.next.next = Node(3)
    llist.head.next.next.next.prev = llist.head.next.next
    llist.head.next.next.next.next = Node(9)
    llist.head.next.next.next.next.prev = llist.head.next.next.next
    print(llist.isPalindrome()) 

    #Empty list
    llist = doubly_linked_list()
    llist.head = None
    print(llist.isPalindrome()) 

    #Empty list
    llist = doubly_linked_list()
    llist.head = Node(4)
    llist.prev, llist.next = None, None
    print(llist.isPalindrome()) 


if __name__== '__main__':
    main()


#Time-spent: 22 minutes     
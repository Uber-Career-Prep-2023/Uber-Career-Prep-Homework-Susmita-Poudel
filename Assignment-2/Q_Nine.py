#Question 9: DisconnectCycle
#Given a singly linked list, disconnect the cycle, if one exists.
#Technique used: Hash the Nodes
#Time complexity: 0(n)          Space complexity: 0(n) n = number of nodes


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def disconnectCycle(self):

        if self.head is None:
            return

        curr = self.head
        prev = None
        node_map = {}

        while curr:
            if curr in node_map:
                prev.next = None
                return
            node_map[curr] = True
            prev = curr
            curr = curr.next



    def printList(self):
        curr = self.head

        while curr is not None:
            print(curr.val, end = ' ')
            curr = curr.next
        print()


def main():
    #test-case if the loop connects at the middle
    llist = LinkedList()
    llist.head = Node(10)
    llist.head.next = Node(18)
    llist.head.next.next = Node(12)
    llist.head.next.next.next = Node(9)
    llist.head.next.next.next.next = Node(11)
    llist.head.next.next.next.next.next = Node(4)
    llist.head.next.next.next.next.next.next =  llist.head.next.next
 

    llist.disconnectCycle()
    llist.printList()
    #loop at the end
    llist = LinkedList()
    llist.head = Node(10)
    llist.head.next = Node(18)
    llist.head.next.next = Node(12)
    llist.head.next.next.next = Node(9)
    llist.head.next.next.next.next = Node(11)
    llist.head.next.next.next.next.next = Node(4)
    llist.head.next.next.next.next.next.next = llist.head.next.next.next.next.next.next 
    llist.disconnectCycle()
    llist.printList()

    #repeating values in nodes 
    llist = LinkedList()
    llist.head = Node(10)
    llist.head.next = Node(10)
    llist.head.next.next = Node(12)
    llist.head.next.next.next = Node(9)
    llist.head.next.next.next.next = Node(11)
    llist.head.next.next.next.next.next = Node(4)
    llist.head.next.next.next.next.next.next = llist.head.next
    llist.disconnectCycle()
    llist.printList()

    #loop in a list with only head
    llist = LinkedList()
    llist.head = Node(10)
    llist.head.next = llist.head
    llist.disconnectCycle()
    llist.printList()


if __name__ == "__main__":
    main()


#Time-spent: 35 minutes

     


            
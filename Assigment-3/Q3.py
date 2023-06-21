#Priority Queue

#Heap

import math
class PriorityQueue:

    def __init__(self):
        self.arr = []
        self.arr.append(float('inf'))

    def top(self):
        if self.arr is None:
            return 
        return self.arr[1]
    
    def insert(self, x, weight):
        self.arr.append((x, weight))
        self.heapUp(len(self.arr)-1)

    def heapUp(self, index):
        parent_index = math.floor(index/2)
      
        while index > 0 and self.arr[index][-1] > self.arr[parent_index][-1]:
            self.arr[index], self.arr[parent_index] = self.arr[parent_index], self.arr[index]
            index = parent_index
            parent_index = math.floor(index/2)

    def remove(self):
        
        if len(self.arr) == 0:
            return "Empty"

        self.arr[1] = self.arr[-1]
        self.arr.pop()
        self.heapDown(1)

        

    def heapDown(self,index):
        size = len(self.arr)
        left_child_index = 2*index
        right_child_index = 2*index + 1
        max_val = index

        if left_child_index < size and self.arr[left_child_index][-1] > self.arr[max_val][-1]:
            max_val = left_child_index

        if right_child_index < size and self.arr[right_child_index][-1] > self.arr[max_val][-1]:
            max_val = right_child_index

        if max_val != index:
            self.arr[index], self.arr[max_val]= self.arr[max_val],self.arr[index]
            self.heapDown( max_val)
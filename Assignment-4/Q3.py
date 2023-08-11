
#Time-complexity: 0(logN)   Space-complexity: 0(N)
import heapq

class MedianFinder:
    def __init__(self):
        self.left_heap = []  # Max-heap for the left half (negated values)
        self.right_heap = []  # Min-heap for the right half

    def addNum(self, num):
        # Add the number to the appropriate heap
        if not self.left_heap or num <= -self.left_heap[0]:
            heapq.heappush(self.left_heap, -num)
        else:
            heapq.heappush(self.right_heap, num)

        # Balance the heaps if needed
        if len(self.left_heap) > len(self.right_heap) + 1:
            heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))
        elif len(self.right_heap) > len(self.left_heap):
            heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))

    def findMedian(self):
        if len(self.left_heap) == len(self.right_heap):
            # If the total count is even, take the average of the two middle elements
            return (-self.left_heap[0] + self.right_heap[0]) / 2
        else:
            # If the total count is odd, the middle element is in the left heap
            return -self.left_heap[0]

# Example usage:
medianFinder = MedianFinder()
inputs = [1, 11, 4, 15, 12]

for num in inputs:
    medianFinder.addNum(num)
    print(medianFinder.findMedian())

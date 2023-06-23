#Question 9: MergeKSortedArrays
#Given an array of k sorted arrays, merge the k arrays into a single sorted array.
#Heap
#Time-complexity: 0(n), Space-Complexity: O(n)
import heapq
def MergeSortedArrays(k, arr):

    min_heap = []
    result = []
    if k == 0:
        return
    if k == 1:
        return arr[0]
    for i in range(k):
        array = arr[i]
     
        if array:
            heapq.heappush(min_heap,(array[0],i,0))
    print(min_heap)

    while min_heap:
        min_element, arr_index, element_index = heapq.heappop(min_heap)
      
        result.append(min_element)
        if element_index + 1 < len(arr[arr_index]):
            heapq.heappush(min_heap,(arr[arr_index][element_index+1], arr_index, element_index+1))

    return result



def main():
    x,y= 2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]

    print(MergeSortedArrays(x,y))

#Output: [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]

    a, b = 3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]
    print(MergeSortedArrays(a,b))
#Output: [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]
    o,p = 1,[[2,4,6]]
    print(MergeSortedArrays(o,p))

    s,t = 3,[[1,2,3],[1,2,3],[1,2,3]]
    print(MergeSortedArrays(s,t))





if __name__ == "__main__":
    main()
        
#Time-spent: 38 minutes

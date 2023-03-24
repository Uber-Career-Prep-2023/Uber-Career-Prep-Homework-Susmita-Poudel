#Question 8: Given a list of integer pairs representing the low and high end of an interval, inclusive, return a list in which overlapping intervals are merged.
#Hash
#Time Complexity : O(nlogn).    Space Complexity: O(n)

def merge_intervals(arr):

    arr = merge_sort(arr)
    
    if len(arr) <= 1:
        return arr

    merged = []
    merged.append((arr[0]))
   
    for interval in arr[1:]:

        if interval[0] <= merged[-1][1]:    
            maximum_range = max((merged[-1][1], interval[1]))
            merged[-1] = (merged[-1][0], maximum_range)
        else:       
            merged.append((interval))

    return merged

#Merge_sort code   
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left_half, right_half):
    result = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i][0] < right_half[j][0]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

    result += left_half[i:]
    result += right_half[j:]

    return result

   





def main():
    

    arr1 = [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
    print(merge_intervals(arr1))
#Output: [(4, 8), (1, 3), (9, 12)]

    arr2 = [(5, 8), (6, 10), (2, 4), (3, 6)]
    print(merge_intervals(arr2))
#Output: [(2, 10)]

    arr3 = [(10, 12), (5, 6), (7, 9), (1, 3)]
    print(merge_intervals(arr3))
#Output: [(10, 12), (5, 6), (7, 9), (1, 3)]


if __name__ == "__main__":
    main()


#Time-spent: 34 mins




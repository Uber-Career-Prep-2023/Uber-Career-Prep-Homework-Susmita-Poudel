#Question 8: Given a list of integer pairs representing the low and high end of an interval, inclusive, return a list in which overlapping intervals are merged.

def merge_intervals(arr):

    arr = sorted(arr, key = lambda x:x[0])
    merged = []
    merged.append((arr[0]))
   
    for interval in arr[1:]:

        if interval[0] <= merged[-1][1]:    
            maximum_range = max((merged[-1][1], interval[1]))
            merged[-1] = (merged[-1][0], maximum_range)
        else:       
            merged.append((interval))

    return merged

   





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







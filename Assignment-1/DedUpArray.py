#Question 9: Given a sorted array of non-negative integers, modify the array by removing duplicates so each element only appears once. If arrays are static (aka, not dynamic/resizable) in your language of choice, the remaining elements should appear in the left-hand side of the array and the extra space in the right-hand side should be padded with -1s.
#Hash The Elements
#Time Complexity: O(n)      Space Complexity: 0(n)
def modifyArray(arr):

    hash_map_of_arr = {}
    copy_arr = arr.copy()
    
    for num in arr:

        if num in hash_map_of_arr:
            hash_map_of_arr[num] += 1

        else:
            hash_map_of_arr[num] = 1

    for num in copy_arr:
      
        if num in hash_map_of_arr and hash_map_of_arr[num]> 1:
            arr.remove(num)
            hash_map_of_arr[num] -= 1

        #print(arr, hash_map_arr)

    return arr

def main():

    arr1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    print(modifyArray(arr1))
    #Modified Array: [1, 2, 3, 4] 

    arr2 = [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]
    print(modifyArray(arr2))
    #Modified Array: [0, 1, 4, 5, 8, 9, 10, 11, 15]


    arr3 = [1, 3, 4, 8, 10, 12]
    print(modifyArray(arr3))
   #Modified Array: [1, 3, 4, 8, 10, 12]


if __name__ == "__main__":
    main()

#Time-Spent: 27 minutes

        
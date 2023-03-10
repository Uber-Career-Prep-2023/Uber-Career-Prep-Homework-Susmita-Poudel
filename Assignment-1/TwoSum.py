#Question10: Given an array of integers and a target integer, k, return the number of pairs of integers in the array that sum to k. In each pair, the two items must be distinct elements (come from different indices in the array).
#Hash the Elements
#Time-Complexity: O(n)          Space-Complexity:0(n)

def TwoSum(arr,k):

    dict_with_arr_elements = {}
    total_count = 0
    for num in arr:
        if num in dict_with_arr_elements:
            dict_with_arr_elements[num] += 1
        else:
            dict_with_arr_elements[num] = 1

    for num in arr:

        if k - num in dict_with_arr_elements:
            total_count += dict_with_arr_elements[k-num]

            if k-num == num:
                total_count -= 1

    return total_count//2

def main():
    #Test-Cases
    arr1= [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
    k = 10
    print(TwoSum(arr1,k))

    #Output: 3
    #(Pairs: (8, 2), (8, 2), (3, 7))

    arr2 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
    k = 8
    print(TwoSum(arr1,k))
    #Output: 4
    #(Pairs: (10, -2), (3, 5), (1, 7))

    arr3= [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
    k = 6
    print(TwoSum(arr3,k))
    #Output: 5
    #(Pairs: (4, 2), (0, 6), (3, 3), (3, 3), (3, 3))
    arr4= [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
    k = 1
    print(TwoSum(arr4,k))
    #Output : 0


if __name__ == "__main__":
    main()


#Time-spent: 38 minutes


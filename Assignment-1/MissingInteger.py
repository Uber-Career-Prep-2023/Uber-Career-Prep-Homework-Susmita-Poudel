#Question6: Given an integer n and a sorted array of integers of size n-1 which contains all but one of the integers in the range 1-n, find the missing integer.
#Binary Search Variation
#Time complexity: O(n)        Space complexity: O(1)

def MissingInteger(arr,n):

    left_pointer = 0
    right_pointer = n - 2

    while left_pointer <= right_pointer:
        mid_value = (left_pointer+right_pointer)//2

        if arr[mid_value] == mid_value + 1:
            left_pointer = mid_value + 1

        else:
            right = mid_value - 1

    missing_integer = left_pointer + 1
    return missing_integer

def main():
    a1 = [1, 2, 3, 4, 6, 7]
    n1 =  7
    print(MissingInteger(a1,n1))
    #Output: 5

    a2 = [1]
    n2 =  2
    print(MissingInteger(a2,n2))
    #Output: 2

    a3 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
    n3 =  12
    print(MissingInteger(a3,n3))
    #Output: 9



if __name__ == '__main__':
    main()

#Time Spent: 30 minutes
    


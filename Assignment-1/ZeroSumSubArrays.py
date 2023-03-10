#Question3: Given an array of integers, count the number of subarrays that sum to zero.
#Hashing Technique: One Directional Running Computation
#Time complexity: O(n)     Space complexity: O(n)

def ZeroSumSubArray(arr):

    dict_with_possible_sums = {0:1}
    count_of_subarrays_with_sumZero = 0
    curr_sum = 0

    for num in arr:
        curr_sum += num

        if curr_sum in dict_with_possible_sums:
            count_of_subarrays_with_sumZero += dict_with_possible_sums[curr_sum]
            dict_with_possible_sums[curr_sum] += 1
        
        else:
            dict_with_possible_sums[curr_sum] = 1

    return count_of_subarrays_with_sumZero

        
def main():
    #Test-Cases
    l = [4, 5, 2, -1, -3, -3, 4, 6, -7]
    
    print(ZeroSumSubArray(l))

    l2 = [8, -5, 0, -2, 3, -4]
    print(ZeroSumSubArray(l2))

    arr = [1, 8, 7, 3, 11, 9]
    print(ZeroSumSubArray(arr))
   

if __name__ == '__main__':
    main()

#Time-spent: 40 minutes [Brute-force algorithm seemed appealing; Took a long time to identify hashing technique]


#Question1: Given an array of integers and an integer, k, find the maximum mean of a subarray of size k.
#Two-pointer technique [Fixed Sliding Window]
#Time-Complexity: O(n)   Space-Complexity: O(1)

def MaxMeanSubArray(arr, k):

    if k > len(arr):
        return 0
    
    first_pointer = 0
    second_pointer = 0
    curr_sum_of_subarry = arr[0]
 
    while second_pointer < k - 1:
        second_pointer +=1
        curr_sum_of_subarry += arr[second_pointer]
        

    max_mean = curr_sum_of_subarry/k
  
    
    while first_pointer < len(arr) - k and second_pointer < len(arr):
        
        first_pointer += 1
        second_pointer += 1
  
        curr_sum_of_subarry = curr_sum_of_subarry - arr[first_pointer-1] + arr[second_pointer]
        
        if (curr_sum_of_subarry/k) > max_mean:
            max_mean = curr_sum_of_subarry/k
        
    return max_mean


def main():

    #Test-Cases
    l1 = [4,5,-3,2,6,1]
    k1 = 2
    print(MaxMeanSubArray(l1,k1))

    l2 = [4,5,-3,2,6,1]
    k2 = 3
    print(MaxMeanSubArray(l2,k2))

    l3 = [1,1,1,1,-1,-1,2,-1,-1]
    k3 = 3
    print(MaxMeanSubArray(l3,k3))

    l4 = [1,1,1,1,-1,-1,2,-1,-1,6]
    k4 = 5
    print(MaxMeanSubArray(l4,k4))

if __name__ == '__main__':    
    main()
        
#Time-spent: 35 minutes

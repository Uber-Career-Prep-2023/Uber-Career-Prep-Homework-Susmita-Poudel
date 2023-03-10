#Question 7: Two strings are considered to be “k-anagrams” if they can be made into anagrams by changing at most k characters in one of the strings. Given two strings and an integer k, determine if they are k-anagrams.
#Hashin Technique(Two arrays/strings increment/decrement hashmap counts)
#Time-complexity: O(n)           #Space-complexity: O(n)

def k_anagrams(str1, str2, k):

    if len(str1) != len(str2):
        return False

    hashmap_with_all_chars_in_str1 = {}

    for char in str1:
        if char in hashmap_with_all_chars_in_str1:
            hashmap_with_all_chars_in_str1[char] += 1

        else:
            hashmap_with_all_chars_in_str1[char] = 1

    #print(hashmap_with_all_chars)
    for char in str2:
        if char in hashmap_with_all_chars_in_str1:
            hashmap_with_all_chars_in_str1[char] -= 1

        

    #print(hashmap_with_all_chars)
    needed = sum(hashmap_with_all_chars_in_str1.values())

    return needed == k

def main():
    #Test-Cases
    s1, s2 =  "apple", "peach"
    k = 1
    print(k_anagrams(s1,s2,k))

    #Output: False

    s1,s2  = "apple", "peach"
    k = 2
    print(k_anagrams(s1,s2,k))
    #Output: True

    s1,s2 = "cat", "dog"
    k = 3
    print(k_anagrams(s1,s2,k))
   #Output: True

    s1,s2 =  "debit curd", "bad credit"
    k= 1
    print(k_anagrams(s1,s2,k))
    #Output: True

    s1, s2 = "baseball", "basketball"
    k: 2
    print(k_anagrams(s1,s2,k))
    Output: False


if __name__ == '__main__':
    main()


#Time-Spent: 25 minutes

        
        

        
    
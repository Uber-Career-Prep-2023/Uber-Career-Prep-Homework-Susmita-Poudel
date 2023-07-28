'''Question5: Given a string and a second string representing required characters, 
return the length of the shortest substring containing all the required characters.'''

#Growing/Shrinking Sliding Window + Hash Elements
#Time Complexity: O(N)       Space Complexity: O(k), k = length of pattern

def shortest_substring(str1, pattern):
   
    dict_with_all_pattern = {}
    for char in pattern:
        dict_with_all_pattern[char] = dict_with_all_pattern.get(char, 0) + 1

   
    first_pointer = 0
    second_pointer = 0
    missing_char_count = 0
    required_count = len(pattern)
    min_len = float('inf')

    print(dict_with_all_pattern)
    while second_pointer < len(str1):
        print(dict_with_all_pattern)
        if str1[second_pointer] in dict_with_all_pattern:
            dict_with_all_pattern[str1[second_pointer]] -= 1
            if dict_with_all_pattern[str1[second_pointer]] >= 0:
                missing_char_count += 1
        second_pointer += 1

        
        while missing_char_count == required_count:
            if second_pointer - first_pointer < min_len:
                min_len = second_pointer - first_pointer
            if str1[first_pointer] in dict_with_all_pattern:
                dict_with_all_pattern[str1[first_pointer]] += 1
                if dict_with_all_pattern[str1[first_pointer]] > 0:
                    missing_char_count -= 1
            first_pointer += 1

    return min_len 


    

def main():
    str1, pat =  "abracadabra", "abc"
    print(shortest_substring(str1,pat))
#Output: 4
#(Shortest Substring: "brac")

    str2, pat =  "zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx"
    #print(shortest_substring(str2,pat))
     #(Fun fact: "Zzyzx" is a town in the Mojave Desert in California!)
#Output: 10
#(Shortest Substring: "zzxwdcbxyz")

    str3, pat = "dog", "god"
    #print(shortest_substring(str3,pat))
#Output: 3
#(Shortest Substring: "dog")




if __name__ == "__main__":
    main()

#Time-Spent: 50 minutes

        


            


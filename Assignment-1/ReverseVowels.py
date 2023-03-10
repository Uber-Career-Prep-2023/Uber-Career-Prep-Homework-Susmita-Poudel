#Question2: Given a string, reverse the order of the vowels in the string.
# Two-pointer technique (Forward/Backward Two pointers)
#Time-complexity: O(n)      Space-complexity:O(n)

def reverseVowels(s):

    vowels = ['a', 'e', 'i', 'o', 'u']

    first_pointer = 0
    second_pointer = len(s) - 1
    array_of_chars_in_s = []
    for char in s:
        array_of_chars_in_s.append(char)

   
    while first_pointer < second_pointer:
    
        if array_of_chars_in_s[first_pointer].lower() not in vowels:
            first_pointer += 1

        if array_of_chars_in_s[second_pointer].lower() not in vowels:
            second_pointer -= 1

        if array_of_chars_in_s[first_pointer].lower() in vowels and array_of_chars_in_s[second_pointer].lower() in vowels:
            temp = array_of_chars_in_s[first_pointer]
            array_of_chars_in_s[first_pointer] = array_of_chars_in_s[second_pointer]
            array_of_chars_in_s[second_pointer] = temp
            first_pointer += 1
            second_pointer -=1

   
    modified_str = ''
    for char in array_of_chars_in_s:
        modified_str += char

    return modified_str
             
   
    

def main():
    #test-cases
    test1 = "Uber Career Prep"
    print(reverseVowels(test1))
    #Modified String: "eber Ceraer PrUp"

    test2 = "xyz"
    print(reverseVowels(test2))
    #Modified String: "xyz"

    test3 =  "flamingo"
    print(reverseVowels(test3))
    #Modified String: "flominga"

if __name__ =='__main__':
    main()

#Time spent: 30 minutes



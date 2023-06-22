#Question 7: ReverseWords
#Given a string, return the string with the order of the space-separated words reversed
#Stack
#Time-complexity: 0(n), Space complexity: O(n): n = number of characters
import collections
def ReverseWords(s_words):
    #if empty string is passed
    if len(s_words) == 0:
        return 

    #if there are no spaces
    if ' ' not in s_words:
        return s_words

    stack = []
    words = s_words.split()
  
    for word in words:
        stack.append(word)

    out = []
    while stack:
        out.append(stack.pop())

    reversed_string = ' '.join(out)
    has_trailing_whitespace = s_words.endswith(" ")
    #if there is a whitespace at end
    if has_trailing_whitespace:
        return " " + reversed_string
    return reversed_string

def main():
    x = "Uber Career Prep"
    #print(ReverseWords(x))
    #Output: "Prep Career Uber"

    y =  "Emma lives in Brooklyn, New York."
    #print(ReverseWords(y))

    #whitespace at the end
    z = "Hakuna. Matata "
    #print(ReverseWords(z))

    a = 'abcdef'
    print(ReverseWords(a))


if __name__ == "__main__":
    main()


#Time-spent: 27 minutes    
 

  
        

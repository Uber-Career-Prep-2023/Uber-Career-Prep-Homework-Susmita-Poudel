#Question 6: WordBreak
#Given a string of characters without spaces and a dictionary of valid words, determine if 
#it can be broken into a list of valid words by adding spaces. 

#Time-complexity: 0(n^2)   Space-complexity: 0(n) n = length of input string 's'

def wordBreak(s, wordDict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string is a valid word
    s = s.lower()
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    
    return dp[n]


def main():
    wordDict = {"elf", "go", "golf", "man", "manatee", "not", "note", "pig", "quip", "tee", "teen"}

    input1 = "mangolf"
    print(wordBreak(input1, wordDict))  # Output: True

    input2 = "manateenotelf"
    print(wordBreak(input2, wordDict))  # Output: True

    input3 = "quipig"
    print(wordBreak(input3, wordDict))  # Output: False



if __name__ == '__main__':
        main()

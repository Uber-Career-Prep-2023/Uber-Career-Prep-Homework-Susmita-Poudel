#Question 6: WordBreak
#Given a string of characters without spaces and a dictionary of valid words, determine if 
#it can be broken into a list of valid words by adding spaces. 



#I couldnt figure out how to solve this problem :)



# Example usage:
def main():
    wordDict = {"Elf", "Go", "Golf", "Man", "Manatee", "Not", "Note", "Pig", "Quip", "Tee", "Teen"}

    input1 = "mangolf"
    print(wordBreak(input1, wordDict))  # Output: True

    input2 = "manateenotelf"
    print(wordBreak(input2, wordDict))  # Output: True

    input3 = "quipig"
    print(wordBreak(input3, wordDict))  # Output: False



if __name__ == '__main__':
        main()

#Question4: Given two strings representing series of keystrokes, determine whether the resulting text is the same. Backspaces are represented by the '#' character so "x#" results in the empty string ("").
#Simultaneous Iteration Two Pointer
#Time Complexity: O(n)      Space Complexity: 0(n)

def backspaceStringCompare(s1, s2):

    first_pointer = 0
    second_pointer = 0

    while first_pointer < len(s1) or second_pointer < len(s2):
    
        
        if first_pointer < len(s1) and s1[first_pointer] == '#':
            if s1[first_pointer -1] == 'x':
                part1 = s1[0:first_pointer - 1] 
                part2 = s1[first_pointer + 1: len(s1)]
                s1 = part1 + " " + part2
                first_pointer -= 1

            else:
                part1 = s1[0:first_pointer - 1] 
                part2 = s1[first_pointer + 1: len(s1)]
                s1 = part1 + part2
                first_pointer -= 2
        else:
            first_pointer += 1
        
                
        if second_pointer < len(s2) and s2[second_pointer] == '#':
            
            if s2[first_pointer -1] == 'x':
                part1 = s2[0:second_pointer - 1] 
                part2 = s2[second_pointer + 1: len(s2)]
                s2 = part1 + " " + part2
                second_pointer -=2

            else:
                part1 = s2[0:second_pointer - 1] 
                part2 = s2[second_pointer + 1: len(s2)]
                s2 = part1  + part2
                second_pointer -= 3

        else:
            second_pointer+= 1
       

        return s1 == s2

def main():
    #Test-Cases
    s1= "Uber Career Prep"
    s2 = "u#Uber Careee#r Prep"
    print(backspaceStringCompare(s1,s2))

    s0, s1 =  "abcde", "abcde"
    print(backspaceStringCompare(s0,s1))

    a,b = "abcdef###xyz", "abcw#xyz"
    print(backspaceStringCompare(a,b))

    c,d = "abcdef###xyz", "abcdefxyz###"
    print(backspaceStringCompare(c,d))
    

if __name__ == '__main__':
    main()

#Time-spent: 30 minutes          
                
            

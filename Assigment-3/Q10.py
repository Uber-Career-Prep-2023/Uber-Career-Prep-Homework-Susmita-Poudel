#Question 10: PrerequisiteCourses
#Given a list of courses that a student needs to take to complete their major and a map of courses to their prerequisites, return a valid order for them to take their courses assuming they only take one course for their major at once.
#Graph- DFS Traversal
#Time-complexity: O(V+E), Space-complexity: O(V)

import collections 
def PrerequisiteCourses(l,d):
  
    visited = set()
    classes = []

    def dfs(c):

        visited.add(c)
        if c in d:
            for neighbor in d[c]:
                if neighbor not in visited:
                    x = dfs(neighbor)

        classes.append(c)

       

    for course in l:
        if course not in visited:
            dfs(course)  

    return classes




def main():
    l = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
    d = { "Data Structures": ["Intro to Programming"],
"Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }
    print(PrerequisiteCourses(l,d))

    a= ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"]
    b = { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"],
          "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"] }
    
    print(PrerequisiteCourses(a,b))

if __name__ == '__main__':
    main()

#Time-spent: 45 minutes
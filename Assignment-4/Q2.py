'''Boggle is a word game in which players compete to find the most words on a square grid of random letters. 
Valid words must be at least three characters and formed from non-overlapping (i.e., a position on the board can only 
be used once in a word) adjacent (including diagonal) letters. Given a Boggle board and a dictionary of valid words, 
return all valid words on the board'''

#Time-complexity: O(r*c)  space-complexity: O(w*l), w = words in dictionary, l = longest word in dictionary
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class BoggleSolverWithTrie:
    def __init__(self, board, dictionary):
        self.board = board
        self.dictionary = dictionary
        self.valid_words = set()
        self.root = TrieNode()

        # Insert all words from the dictionary into the Trie
        for word in self.dictionary:
            self.insert_word(word)

    def insert_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def is_valid(self, i, j):
        return 0 <= i < len(self.board) and 0 <= j < len(self.board[0])

    def dfs(self, i, j, node, word):
        char = self.board[i][j]
        if char not in node.children:
            return

        node = node.children[char]
        word += char

        if node.is_end_of_word:
            self.valid_words.add(word)

        temp = self.board[i][j]
        self.board[i][j] = '#'  # Mark cell as visited

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # Explore neighboring cells
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if self.is_valid(ni, nj) and self.board[ni][nj] != '#':
                self.dfs(ni, nj, node, word)

        self.board[i][j] = temp  # Backtrack

    def solve(self):
        # Traverse the entire board to initiate DFS from each cell
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.dfs(i, j, self.root, "")

        return list(self.valid_words)



#Time-spent = Over 3 hours; needed to take help from internet and still cannot understand entirely the time and space compleixty


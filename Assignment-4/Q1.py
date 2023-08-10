#Implement a trie class, including the insert, search, and delete methods
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def _char_to_index(self, char):
        '''Helper function that converts character(lowercase a to z) into index'''
        return ord(char) - ord('a')
    
    #Insert Function
    def insert(self, word):
        node = self.root
        for char in word:
            index = self._char_to_index(char)
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.validWord = True

    #Search function
    def _search_node(self, node, word):
        for char in word:
            index = self._char_to_index(char)
            if not node.children[index]:
                return None
            node = node.children[index]
        return node
    
    def isValidWord(self, word):
        node = self._search_node(self.root, word)
        return node is not None and node.validWord
    
    def _has_children(self, node):
        return any(child is not None for child in node.children)

    def _remove_helper(self, node, word, depth):
        if depth == len(word):
            if node.validWord:
                node.validWord = False
            return not self._has_children(node)
        
        char = word[depth]
        index = self._char_to_index(char)
        
        if not node.children[index]:
            return False
        
        should_delete = self._remove_helper(node.children[index], word, depth + 1)
        
        if should_delete:
            node.children[index] = None
            return not node.validWord and not self._has_children(node)
        
        return False
    #Remove function
    def remove(self, word):
        if self.isValidWord(word):
            self._remove_helper(self.root, word, 0)







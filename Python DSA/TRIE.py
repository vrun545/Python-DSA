class TrieNode:
    def __init___(self):
        self.children[26] = [None]*26
        self.isTerminal = False

class Trie:
    def __init__(self):
        self.root = self.getNode() 

    def getNode(self):
        return TrieNode()

    def searchWord(self, word):
        pass

    def insertWord(self, word):
        pass

    def removeWord(self, word):
        pass

trie1 = Trie()

#code
class TrieNode:
    
    def __init__(self):
        self.children= [None]*26
        self.we = 0
def insert(root, word):
    #we will insert word into the Trie root character by character
    for i in word:
        idx = ord(i) - ord('a') #gives us the relative index
        if root.children[idx]== None:
            #first time insertion
            root.children[idx] = TrieNode()
        root = root.children[idx]
    #word has been inserted so we can increase the word ending by 1
    root.we+=1

def search(root, word):
    for i in word:
        idx = ord(i) - ord('a')
        if root.children[idx]== None:
            return False
        root = root.children[idx]
    if root.we > 0:
        return True
    else:
        return False
        
t = int(input())
for i in range(t):
    n = int(input())
    words = list(map(str, input().split()))
    target = input()
    
    #now instantiate a root TrieNode and insert words into it
    root = TrieNode()
    for i in words:
        cpy = root
        insert(cpy, i)
    
    #now to search for word
    cpy=  root
    a = search(cpy, target)
    print(int(a))
    
    

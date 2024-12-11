

class Node:
    def __init__(self, d):
        self.data = data
        self.neighbors = []

def make_clone(root, clones):
    if not root:
        return None 
    
    clone = Node(root.data)
    clones[root] = clone

    for c in root.neighbors:
        x = clones.get(c)

        if not x:
            clone.neighbors += [make_clone(c, clones)]
        else:
            clone.neighbors += [x]
    
    return clone

def clone(root):
    clones = {}
    return make_clone(root, clones)
  

if __name__ == "__main__":
    inpt = [[2,3],[1,3],[1,2]]
    result = clone(inpt)
    print(result)
class BinarySearchTree:
    class __Node:
        def __init__(self,val,left = None,right= None):
            self.val = val
            self.left = left
            self.right = right
        def getVal(self):
            return self.val
        def setVal(self,newval):
            self.val = newval
        def getLeft(self):
            return self.left
        def getRight(self):
            return self.right
        def setLeft(self,newleft):
            self.left = newLeft
        def setRight(self,newright):
            self.right = newright
        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem
                yield self.val
                if self.right != None:
                    for elem in self.right:
                        yield elem
    def __init__(self):
        self.root = None
    def insert(self,val):
        def __insert(root,val):
            if root == None:
                return BinarySearchTree.__Node(val)
            if val < root.getVal():
                root.setLeft(__insert(root.getLeft(),val))
            else:
                root.setRight(__insert(root.getRight(),val))
            return root
        self.root = __insert(self.root,val)
    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()
def dfs(current, goal):
    if current == goal:
        return [current]
    for next in adjacent(current):
        result = dfs(next)
        if result != None:
            return [current] + result
    return None
def main():
    s = input("e")
    lst = s.split()
    tree = BinarySearchTree()
    for x in lst:
        tree.insert(float(x))
    for x in tree:
        print(x)
if __name__ == "__main__":
    main()

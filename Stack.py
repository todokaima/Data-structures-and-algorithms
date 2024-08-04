class Stack:
    def __init__(self):
        self.items = []
    def pop(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to pop an empty stack")
        topIdx = len(self.items)-1
        item = self.items[topIdx]
        del self.items[topIdx]
        return item
    def push(self,item):
        self.items.append(item)
    def top(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to get top of empty stack")
        topIdx = len(self.items)-1
        return self.items[topIdx]
    def isEmpty(self):
        return len(self.items) == 0
def main():
    s = Stack()
    lst = list(range(1))
    lst2 = []
    for k in lst:
        s.push(k)
    if s.top() == 9:
        print("Test 1 passed")
    else:
        print("Test 1 failed")
    while not s.isEmpty():
        lst2.append(s.pop())
    lst2.reverse()
    if lst2 != lst:
        print("Test2 fialed")
    else:
        print("Test 2 pased")
    try:
        s.pop()
        print("Test 3 failed")
    except RuntimeError:
        print("Test 3 passed")
    except:
        print("Test 3 Failed")
    try:
        s.top()
        print("Test 4 Failed")
    except RuntimeError:
        print("Test 4 PASSED")
    except:
        print("Test 4 failed")
if __name__=="__main__":
    main()
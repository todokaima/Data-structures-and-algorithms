class Queue:
    def __init__(self):
        self.items = []
        self.frontIdx = 0
    def __compress(self):
        newlst = []
        for i in range(self.frontIdx,len(self.items)):
            newlst.append(self.items[i])
        self.items = newlst
        self.frontIdx
    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to dequeue an empty qeuue")
        item = self.items[self.frontIdx]
        self.frontIdx += 1
        return item
    def enqueue(self,item):
        if self.items.append(item):
            self.items.append(item)

    def front(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to acc front of empty")
        return self.items[self.frontIdx]
    def isEmpty(self):
        return self.frontIdx == len(self.items)
def main():
    q = Queue()
    lst = list(range(10))
    lst2 = []

    for k in lst:
        q.enqueue(k)
    if q.front() ==0:
        print("T1 passed")
    else:
        print("t1 failed")
    while not q.isEmpty():
        lst2.append(q.dequeue())
    if lst2 != lst:
        print("Test2 failed")
    else:
        print("T2 passed")
    for k in lst:
        q.enqueue(k)
    lst2 = []
    while not q.isEmpty():
        lst2.append(q.dequeue())
    if lst2 != lst:
        print("T3 failed")
    else:
        print("T3 passed")
    try:
        q.dequeue()
        print("Test 4 failed")
    except RuntimeError:
        print("Test 4 Passed")
    except:
        print("T4 failed")
    try:
        q.front()
        print("T5 failed")
    except RuntimeError:
        print("T5 passed")
    except:
        print("T5 fialed")
if __name__=="__main__":
    main()
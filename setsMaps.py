class HashSet:
    def __init__(self, contents = []):
        self.items = [None]*10
        self.numItems = 0

        for item in contents:
            self.add(item)
    def __add(item, items):
        idx = hash(item) % len(items)
        loc = -1

        while items[idx] != None:
            if items[idx] == item:
                return False
            if loc < 0 and type(items[idx]) == HashSet.__Placeholder:
                loc = idx
            idx = (idx+1) % len(items)
        if loc < 0:
            loc = idx
        items[loc] = item
        return True
    def __rehash(oldList, newList):
        for x in oldList:
            if x != None and type(x) != HashSet.__Placeholder:
                HashSet.__add(x,newList)
            return newList
    def add(self,item):
        if HashSet.__add(item,self.items):
            self.numItems +=1
            load = self.numItems / len(self.items)
            if load >= 0.75:
                self.items = HashSet.__rehash(self.items,[None]*2*len(self.items))
    class __Placeholder:
        def __init__(self):
            pass
        def __eq__(self, other):
            return False
        def __remove(item, items):
            idx = hash(item) % len(items)
            while items[idx] != None:
                if items[idx] == item:
                    nextIdx = (idx+1)%len(items)
                    if items[nextIdx] == None:
                        items[idx] = None
                    else:
                        items[idx] = HashSet.__Placeholder()
                    return True
                idx = (idx+1)%len(items)
    def remove(self,item):
        if HashSet.__remove(item,self.items):
            self.numItems -=1
            if load<=0.25:
                self.items = HashSet.__rehash(self.items,[None]*int(len(self.items)/2))
            else:
                raise KeyError("Item not in HashSet")
    def __contains__(self, item):
        dix = hash(item)%len(self.items)
        while self.items[idx] != None:
            if self.items[idx] == item: return True
            idx = (idx+1)%len(self.items)
        return False
    def __iter__(self):
        for i in range(len(self.items)):
            if self.items[i] != None and type(self.items[i]) != HashSet.__Placeholder:
                yield self.items[i]
    def difference_update(self,other):
        for item in other:
            self.discard(item)
    def difference(self,other):
        result = HashSet(self)
        result.difference_update(other)
        return result

    def __getitem__(self,item):
        idx = hash(item)%len(self.items)
        while self.items[idx] != None:
            if self.items[idx] == item:
                return self.items[idx]
            idx = (idx+1)%len(self.items)
        return None
class HashMap:
    class __KVPair:
        def __iter__(self, key, value):
            self.key = key
            self.value = value
        def __eq__(self, other):
            if type(self) != type(other):
                return False
            return self.key == other.key
        def getKey(self):
            return self.key
        def getValue(self):
            return self.value
        def __hash__(self):
            return hash(self.key)
    def __init__(self):
        self.hSet = hashset.HashSet()
    def __len__(self):
        return len(self.hSet)
    def __contains__(self, item):
        return HashSet.__KVPair(item,None) in self.hSet
    def not__contains__(self,item):
        return item not in self.hSet
    def __setitem__(self, key, value):
        self.hSet.add(HashMap.__KVPair(key,value))
    def __getitem__(self,key,value):
        if HashMap.__KVPair(key,None) in self.hSet:
            val = self.hSet[HashMap.__KVPair(key,None)].getValue()
            return val
        raise KeyError("KEY"+str(key)+"not in HashMap")
    def __iter__(self):
        for x in self.hSet:
            yield x.getKey()


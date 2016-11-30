class Node:
    def __init__(self, item, nxt):
        self.item = item
        self.nxt = nxt
        
class LinkedList:
    def __init__(self):
        self.mFirst = None
        self.mSize = 0

    def Insert(self, item):
        if self.Exists(item):
            return False
        n = Node(item, self.mFirst)
        self.mFirst = n
        self.mSize += 1
        return True

    def Exists(self, dummyItem):
        current = self.mFirst
        while current:
            if current.item == dummyItem:
                return True
            current = current.nxt
        return False
    
    def Retrieve(self, dummyItem):
        current = self.mFirst
        while current:
            if current.item == dummyItem:
                return current.item
            current = current.nxt
        return None
    
##    def Size(self):
##        count = 0
##        current = self.mFirst
##        while current:
##            count += 1
##            current = current.nxt
##        return count
    
    def Size(self):
        return self.mSize

    
    def Traverse(self, callbackFunction):
        current = self.mFirst
        while current:
            callbackFunction(current.item)
            current = current.nxt

    def Delete(self, dummyItem):
        if not self.Exists(dummyItem):
            return False
        self.mSize -= 1

        # Handle case where first node needs deleting:
        if self.mFirst.item == dummyItem:
            self.mFirst = self.mFirst.nxt
            return True
        
        current = self.mFirst
        while current.nxt.item != dummyItem:
            current = current.nxt
        # Now current points to the node before the node that needs deleting.

        current.nxt = current.nxt.nxt
        return True

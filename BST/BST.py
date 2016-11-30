class Node:
    def __init__(self, item, right, left):
        self.item = item
        self.right = right
        self.left = left
        
class BST:
    def __init__(self):
        self.mRoot = None
        self.mSize = 0


    def Insert(self, item):
        if self.Exists(item):
            return False
        else:
            self.mRoot = self.InsertR(item, self.mRoot)
            self.mSize += 1
            return True

    def InsertR(self, item, current):
        if current is None:
            current = Node(item,None, None)
        elif item < current.item:
            current.left = self.InsertR(item, current.left)
        else:
            current.right = self.InsertR(item, current.right)
        return current

    def Exists(self, dummyItem):
        return self.ExistsR(dummyItem, self.mRoot)

    def ExistsR(self, dummyItem, current):
        if current is None:
            return False
        try:
            if current.item == dummyItem:
                return True
        except AttributeError:
            print current
        if dummyItem < current.item:
            return self.ExistsR(dummyItem, current.left)
        else:
            return self.ExistsR(dummyItem, current.right)
    
    def Retrieve(self, dummyItem):
        return self.RetrieveR(dummyItem, self.mRoot)

    def RetrieveR(self, dummyItem, current):
        #print self.mRoot.item.SS
        if current is None:
            return None
        if current.item == dummyItem:
            return current.item
        if dummyItem < current.item:
            return self.RetrieveR(dummyItem, current.left)
        else:
            return self.RetrieveR(dummyItem, current.right)

    ####Size will be counted during Insert and Delete####
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
        age = 0.0
        age += self.TraverseR(callbackFunction, self.mRoot)
        return age

    def TraverseR(self, function, current):
        age = 0
        if current is not None:
            age = function(current.item)
        if current.left is not None:
            age += self.TraverseR(function, current.left)
        if current.right is not None:
            age += self.TraverseR(function, current.right)
        return age

    def Delete(self, dummyItem):
        if not self.Exists(dummyItem):
            return False
        self.mSize -= 1
        self.mRoot = self.DeleteR(dummyItem, self.mRoot)
        return True

    def DeleteR(self, item, current):
        if item < current.item:
            current.left = self.DeleteR(item, current.left)
        elif item > current.item:
            current.right = self.DeleteR(item, current.right)
        else:
            if not current.left and not current.right:
                current = None
            elif not current.right:
                current = current.left
            elif not current.left:
                current = current.right
            else:
                successor = current.right
                while successor.left:
                    successor = successor.left
                current.item = successor.item
                current.right = self.DeleteR(successor.item, current.right)
        return current

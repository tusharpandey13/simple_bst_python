class Node:
    def __init__(self, val):
        self.val = val
        self.r = None
        self.l = None


class tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root == None:
            self.root = Node(val=val)
        else:
            self._add(val=val, node=self.root)

    def _add(self, val, node):
        if(val < node.val):
            if(node.l != None):
                self._add(val=val, node=node.l)
            else:
                node.l = Node(val)
        else:  # >=
            if(node.r != None):
                self._add(val=val, node=node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root != None:
            return(self._find(val=val, node=self.root))
        else:
            return None

    def _find(self, val, node):
        if (node == None) or (node.val == val):
            return node
        # else:
        if (val < node.val):  # and (node.l != None):
            return self._find(val, node.l)
        # elif (val > node.val) : # and (node.r != None):
        return self._find(val, node.r)
        # else:
        #     printinorder('fe')
        #     return None

    def printinorderold(self):
        self._printinorderold(self.root)

    def _printinorderold(self, node):
        if node != None:
            printinorder(node.val)
            self._printinorderold(node.l)
            self._printinorderold(node.r)
        else:
            printinorder('None')

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        ctr = 0
        if node != None:
            ctr += 1
            if node.l != None:
                ctr += self._size(node.l)
            if node.r != None:
                ctr += self._size(node.r)
        return ctr

    def maxdepth(self):
        return self._maxdepth(node=self.root)

    def _maxdepth(self, node):
        if node == None:
            return 0
        return 1 + max(self._maxdepth(node=node.l), self._maxdepth(node=node.r))

    def _isleaf(self, node):
        if node.l == None and node.r == None:
            return True
        else:
            return False

    def printinorder(self):
        self._printinorder(self.root)

    def _printinorder(self, node):
        if node != None:
            if node.l != None:
                self._printinorder(node.l)
            print(node.val)
            if node.r != None:
                self._printinorder(node.r)

    def printpostorder(self):
        self._printpostorder(self.root)

    def _printpostorder(self, node):
        if node != None:
            if node.l != None:
                self._printpostorder(node.l)
            if node.r != None:
                self._printpostorder(node.r)
            print(node.val)

    def haspathsum(self, n):
        return self._haspathsum(n, self.root)

    def _haspathsum(self, n, node):
        if node == None:
            return n == 0
        n -= node.val
        return self._haspathsum(n, node.l) or self._haspathsum(n, node.r)

    def printpaths(self):
        print(self._getpaths(self.root))

    def _getpaths(self, node):
        if node == None:
            print('[[]]')
            return [[]]  # [[], []]
        else:
            # return [node.l, node.r]
            tmpl = [[]]
            if not self._isleaf(node):
                tmpl = [[node.val] + x for x in (self._getpaths(node.l) + self._getpaths(node.r))]
            else:
                tmpl = [[node.val]]
            print(tmpl)
            return tmpl


t1 = tree()
t1.add(4)
t1.add(2)
t1.add(5)
t1.add(1)
t1.add(3)
# printinorder(t1.find(5))
# t1.printinorderold()
# t1.printinorder()
# print(t1.size())
# t1.printpostorder()
# print(t1.maxdepth())
print(t1.printpaths())

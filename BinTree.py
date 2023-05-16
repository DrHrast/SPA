class BinaryTree:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def preorder(self):
        pre_order = str(self.value)
        if self.left != None:
            pre_order += self.left.preorder()
        if self.right != None:
            pre_order += self.right.preorder()
        return pre_order

    def inorder(self):
        in_order = ''
        if self.left != None:
            in_order += self.left.inorder()
        in_order += str(self.value)
        if self.right != None:
            in_order += self.right.inorder()
        return in_order

    def postorder(self):
        post_order = ''
        if self.left != None:
            post_order += self.left.postorder()
        if self.right != None:
            post_order += self.right.postorder()
        post_order += str(self.value)
        return post_order

    def pre_in_post(self):
        print(self.preorder())
        print(self.inorder())
        print(self.postorder())

    def add_left(self, value):
        if self.left != None:
            tmp = self
            while tmp.left != None:
                if tmp.left != None and tmp.right == None:
                    tmp.right = BinaryTree(value)
                    break
                else:
                    tmp = tmp.left 
            if tmp.left == None:
                tmp.left = BinaryTree(value)
        else:
            self.left = BinaryTree(value)

    def add_right(self, value):
        if self.right != None:
            tmp = self
            while tmp.right != None:
                if tmp.right != None and tmp.left == None:
                    tmp.left = BinaryTree(value)
                    break
                else:
                    tmp = tmp.right
            if tmp.right == None:
                tmp.right = BinaryTree(value)
        else:
            self.right = BinaryTree(value)

class Heap:
    def __init__(self):
        self.data = list()
        self.size = 0

    def left(self, i):
        return 2 * i + 1
    
    def right(self, i):
        return 2 * i + 2
    
    def parent(self, i):
        return (i - 1) // 2
    
    def insert(self, v):
        self.data.append(v)
        self.size += 1
        i = self.size - 1
        while i > 0 and self.data[self.parent(i)] > self.data[i]:
            self.data[self.parent(i)], self.data[i] = self.data[i], self.data[self.parent(i)]
            i = self.parent(i)

    def minHeapify(self, i):
        gotovo = False
        while not gotovo:
            lijevo = self.left(i)
            desno = self.right(i)
            mini = i
            if lijevo < self.size:
                if self.data[lijevo] < self.data[mini]:
                    mini = lijevo
            if desno < self.size and self.data[desno] < self.data[mini]:
                mini = desno
            if mini != i:
                self.data[mini], self.data[i] = self.data[i], self.data[mini]
                i = mini
            else:
                gotovo = True

    def buildMinHeap(self, a):
        self.data = a
        self.size = len(a)
        p = self.size // 2
        for i in range(p, -1, -1):
            self.minHeapify(i)

    def remove(self):
        if self.size > 1:
            v = self.data[0]
            self.data[0] = self.data.pop()
            self.size -= 1
            self.minHeapify(0)    
            return v   
        elif self.size == 1:
            self.size -= 1
            return self.data.pop() 
        
def HeapSort(a):
    h = Heap()
    h.buildMinHeap(a)
    b = list()
    while h.size > 0:
        b.append(h.remove())
    return b


tree1 = BinaryTree(2)
tree1.add_left(5)
tree1.add_left(6)
tree1.add_left(1)
tree1.add_left(3)
tree1.add_left(7)
tree1.add_right('P')
tree1.pre_in_post()
a = [5, 7, 2, 3, 4]


h = Heap()
for e in a:
    h.insert(e)
print(h.data)

a = [10, 3, 11, 9, 5, 8, 19, 6, 1]
g = Heap()
g.buildMinHeap(a)
print(g.data)
print(g.remove())
print(g.data)
b = HeapSort(a)
print(b)
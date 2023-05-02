class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LL:

    #########################
    #   UGRAĐENE            #
    #########################

    def __init__(self):
        self.head = None

    def __str__(self):
        curr = self.head
        clan = ''
        while curr != None:
            clan += str(curr.value) + ' '
            curr = curr.next
        return clan
    
    #########################
    #   STATIČKE            #
    #########################
    
    def is_prime(v):
        br = 0
        for i in range(2, v):
            if v % i == 0:
                br += 1
        if br > 0:
            return False
        return True
    
    #########################
    #   OSTALE              #
    #########################

    def nElementa(self, n):
        br = 1
        curr = self.head
        if self.head == None:
            return 
        else:
            if n == 1:
                return self.head.value
            else:
                while curr != None:
                    if br == n:
                        return curr.value
                    br += 1
                    curr = curr.next
                return IndexError('Out of bound')
               
            
    def nIndexa(self, n):
        ind = 0
        curr = self.head
        if self.head == None:
            return
        else:
            if n == 0:
                return self.head.value
            else:
                while curr != None:
                    if ind == n:
                        return curr.value
                    ind += 1
                    curr = curr.next
                return IndexError('Out of bound')
            
    def add_left(self, v):
        tmp = Node(v)
        tmp.next = self.head
        self.head = tmp

    def add_right(self, v):
        if self.head == None:
            self.head = Node(v)
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = Node(v)

    def pop_right(self):
        if self.head == None:
            return
        elif self.head.next == None:
            v = self.head.value
            self.head = None
            return v
        else:
            curr = self.head
            while curr.next.next != None:
                curr = curr.next
            v = curr.next.value
            curr.next = None
            return v   
    
    def remove_primes(self):
        if self.head == None:
            return 
        curr = self.head
        while self.head.next != None:
            v = self.head.value
            if LL.is_prime(v) == True:
                self.head = self.head.next
            elif LL.is_prime(v) == True and self.head.next == None:
                self.head = None
            else: break
        while curr.next != None:
            v = curr.next.value
            if LL.is_prime(v) == True:
                curr.next = curr.next.next
            else:
                curr = curr.next
    
    def contains(self,v):
        if self.head == None:
            return False
        else:
            tmp = self.head
            while tmp != None:
                if tmp.value == v:
                    return True
                tmp = tmp.next
            return False
        
    def remove_odd(self):
        if self.head == None:
            return
        elif self.head.next == None and self.head % 2 != 0:
            self.head == None
        while self.head != None:
            if self.head.value % 2 != 0:
                self.head = self.head.next
            break
        tmp = self.head
        while tmp.next != None:
            if tmp.next.value % 2 != 0:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next

    def min(self):
        if self.head == None:
            return
        elif self.head.next == None:
            return self.head.value
        tmp = self.head
        mini = self.head.value
        while tmp != None:
            if tmp.value < mini:
                mini = tmp.value
            tmp = tmp.next
        return mini
    
    def remove(self, v):
        if self.head == None:
            return
        if self.head.next == None and self.head.value == v:
            self.head = None
            return
        else:
            while self.head.value == v:
                self.head = self.head.next
            tmp = self.head
            while tmp.next != None:
                if tmp.next.value == v:
                    tmp.next = tmp.next.next
                else:
                    tmp = tmp.next

    def f(self):
        if self.head == None or self.head.next == None:
            return
        else:
            tmp = self.head
            while tmp.next != None:
                if tmp.value > tmp.next.value:
                    tmp.value, tmp.next.value = tmp.next.value, tmp.value
                tmp = tmp.next

    def sort(self):
        if self.head == None or self.head.next == None:
            return
        else:
            tmp = self.head
            while tmp.next != None:
                tmp2 = tmp.next
                while tmp2 != None:
                    if tmp.value > tmp2.value:
                        tmp.value, tmp2.value = tmp2.value, tmp.value
                    tmp2 = tmp2.next
                tmp = tmp.next

    def reverse(self):
        if self.head == None or self.head.next == None:
            return
        else:
            br = 0
            tmp = self.head
            while tmp.next != None:
                br += 1
                tmp = tmp.next
            tmp = self.head
            n = 0
            while n < br // 2:
                tmp2 = tmp.next
                n2 = n + 1
                while n2 < br - n:
                    n2 += 1
                    tmp2 = tmp2.next
                tmp.value, tmp2.value = tmp2.value, tmp.value
                tmp = tmp.next
                n += 1
                


class LL2(LL):
    def __init__(self):
        super().__init__()
        self.tail = None
    
    def addRight(self, v):
        if self.head == None:
            self.head = self.tail = Node(v)
        else:
            tmp = Node(v)
            self.tail.next = tmp
            self.tail = self.tail.next

class Queue(LL):
    def __init__(self):
        super().__init__()
        self.tail = None

    def enqueue(self, v):
        if self.head == None:
            self.head = self.tail = Node(v)
        else:
            tmp = Node(v)
            self.tail.next = tmp
            self.tail = self.tail.next
    
    def dequeue(self):
        if self.head == None:
            return
        else:
            v = self.head.value
            self.head = self.head.next
            return v
    
    def isEmpty(self):
        return self.head == None
    
    def decode(izraz):
        red = Queue()
        for e in izraz:
            if e == '+':
                red.enqueue(red.dequeue())
                print(red)
            elif e == '-':
                red.dequeue()
                print(red)
            elif e == ' ':
                continue
            else:
                red.enqueue(int(e))
                print(red)
        return red
    
class Stack(LL):
    def __init__(self):
        super().__init__()

    def push(self, v):
        if self.head == None:
            self.head = Node(v)
        else:
            tmp = Node(v)
            tmp.next = self.head
            self.head = tmp

    def pop(self):
        if self.head != None:
            v = self.head.value
            self.head = self.head.next
            return v
        return
    
    def decode(izraz):
        s = Stack()
        izraz = izraz.split()
        if izraz[0] in '+-*/':
            izraz.reverse()
        for el in izraz:
            if el in '+-*/':
                a = s.pop()
                b = s.pop()
                if el == '+':
                    s.push(a + b)
                elif el == '-':
                    s.push(a - b)
                elif el == '*':
                    s.push(a * b)
                elif el == '/':
                    s.push(a / b)
            else:
                s.push(int(el))
        return s.pop()


a = LL()
a.head = Node(2)
a.head.next =  Node(3)
a.head.next.next = Node(5)
a.head.next.next.next = Node(8)
a.head.next.next.next.next = Node(1)

print(a)
print(a.nElementa(5))
print(a.nIndexa(4))
a.add_left(13)
print(a)
a.add_right(2)
a.add_right(20)
print(a)
v = a.pop_right()
print(v)
print(a)
a.add_left(v)
a.add_right(v)
a.add_left(11)
a.add_left(21)
a.add_left(11)
a.add_left(7)
a.add_right(7)
a.add_right(5)
print(a)
a.remove_primes()
print('not primes: ', a)
a.add_right(5)
a.add_right(7)
print(a)
a.remove_odd()
print('not odds', a)
a.add_right(2)
print('mini je', a.min())
print(a)
a.add_left(2)
a.add_left(2)
a.add_left(2)
a.add_right(2)
a.add_right(2)
a.add_right(2)
print('L:', a)
a.remove(2)
print('remove dupl:', a)
a.add_right(5)
a.add_right(12)
a.add_right(3)
a.add_right(8)
print(a)
a.f()
print('semi sort:', a)
a.sort()
print('full sort:', a)
a.reverse()
print('reverse:', a)
a.add_right(5)
a.add_right(12)
a.add_right(3)
a.add_right(8)
a.add_right(1)
print(a)
a.reverse()
print(a)


print('\n\n')
print('#' * 15)
b = LL2()
b.addRight(3)
b.addRight(5)
b.addRight(11)
b.addRight(1)
b.addRight(2)
print(b)
print('tail value', b.tail.value)
print('head value', b.head.value)

print('\n\n')
print('#' * 15)
izraz = '1 + 3 6 - - 9 8 + + 7 -'
print(Queue.decode(izraz))

print('\n\n')
print('#' * 15)
izraz = '1 2 + 3 4 + * 5 +'
reza = Stack.decode(izraz)
print(izraz)
print(reza)
izraz2 = '3 5 + 2 3 + * 7 -'
reza2 = Stack.decode(izraz2)
print(izraz2)
print(reza2)
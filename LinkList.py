#########################
#   IMPORTS             #
#########################

import random

#########################
#   KLASE               #
#########################

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class DNode:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

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
    
    def __len__(self):
        lenght = 1
        if self.head == None:
            return 0
        else:
            tmp = self.head
            while tmp.next != None:
                tmp = tmp.next
                lenght += 1
            return lenght
    
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
    
    def is_odd(v):
        if v % 2 == 1:
            return True
        return False
    
    def is_even(v):
        if v % 2 == 0:
            return True
        return False
    
    def randomN(a, b):
        return random.randint(a, (b + 1))
    
    #########################
    #   OSTALE              #
    #########################

    def isEmpty(self):
        return self.head == None


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
            
    def insert_per_index(self, n = 0, v = 0):
        ind = 1
        if n == 0:
            self.add_left(v)
        elif n > self.__len__() - 1:
            self.add_right(v)
        else:
            tmp2 = self.head.next
            tmp = self.head
            while ind < n:
                tmp2 = tmp2.next
                tmp = tmp.next
                ind += 1
            tmp.next = Node(v)
            tmp.next.next = tmp2

    def insert_per_position(self, n = 0, v = 0):
        pos = 2
        if n == 1:
            self.add_left(v)
        elif n > self.__len__():
            self.add_right(v)
        else:
            tmp2 = self.head.next
            tmp = self.head
            while pos < n:
                tmp2 = tmp2.next
                tmp = tmp.next
                pos += 1
            tmp.next = Node(v)
            tmp.next.next = tmp2
 
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

    def remove_odds(self):
        if self.head == None:
            return 
        curr = self.head
        while self.head.next != None:
            v = self.head.value
            if LL.is_odd(v) == True:
                self.head = self.head.next
            elif LL.is_odd(v) == True and self.head.next == None:
                self.head = None
            else: break
        while curr.next != None:
            v = curr.next.value
            if LL.is_odd(v) == True:
                curr.next = curr.next.next
            else:
                curr = curr.next

    def remove_evens(self):
        if self.head == None:
            return 
        curr = self.head
        while self.head.next != None:
            v = self.head.value
            if LL.is_even(v) == True:
                self.head = self.head.next
            elif LL.is_even(v) == True and self.head.next == None:
                self.head = None
            else: break
        while curr.next != None:
            v = curr.next.value
            if LL.is_even(v) == True:
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

    def ins_N_rand(self, nBrojeva = 1, min = 1, max = 9):
        for i in range(nBrojeva):
            n = LL.randomN(min, max)
            self.add_right(n)
                

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

    def addLeft(self, v):
        if self.head == None:
            self.head = self.tail = Node(v)
        else:
            tmp = Node(v)
            tmp.next = self.head
            self.head = tmp
    
class DLL:
    #########################
    #   UGRAĐENE            #
    #########################

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self) -> str:
        curr = self.head
        clan = ''
        while curr != None:
            clan += str(curr.value) + ' '
            curr = curr.next
        return clan
    
    def __sizeof__(self) -> int:
        if self.head == None:
            return 0
        else:
            lenght = 1
            tmp = self.head
            while tmp != self.tail:
                lenght += 1
                tmp = tmp.next
            return lenght
        
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
    
    def is_odd(v):
        if v % 2 == 1:
            return True
        return False
    
    def is_even(v):
        if v % 2 == 0:
            return True
        return False

    def randomN(a, b):
        return random.randint(a, (b + 1))

    #########################
    #   OSTALE              #
    #########################

    def append(self, v):
        v = DNode(v)
        if self.head == None:
            self.head = self.tail = v
        else:
            self.tail.next = v
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
    
    def ins_first(self, v):
        v = DNode(v)
        if self.head == None:
            self.head = self.tail = v
        else:
            self.head.prev = v
            self.head.prev.next = self.head
            self.head = self.head.prev

    def reverse(self):
        if self.head == None:
            return
        else:
            tmp = self.tail
            while tmp != None:
                print(f'{tmp.value}', end = ' ')
                tmp = tmp.prev
            print()
    
    def insert_per_index(self, n = 0, v = 0):
        ind = 1
        if n == 0:
            self.ins_first(v)
        elif n > self.__sizeof__() - 1:
            self.append(v)
        else:
            tmp2 = self.head.next
            tmp = self.head
            while ind < n:
                tmp2 = tmp2.next
                tmp = tmp.next
                ind += 1
            tmp.next = DNode(v)
            tmp.next.next = tmp2
            tmp.next.prev = tmp            
            tmp2.prev = tmp.next

    def insert_per_position(self, n = 0, v = 0):
        ind = 2
        if n == 0:
            self.ins_first(v)
        elif n > self.__sizeof__():
            self.append(v)
        else:
            tmp2 = self.head.next
            tmp = self.head
            while ind < n:
                tmp2 = tmp2.next
                tmp = tmp.next
                ind += 1
            tmp.next = DNode(v)
            tmp.next.next = tmp2
            tmp.next.prev = tmp            
            tmp2.prev = tmp.next

    def ins_N_rand(self, nBrojeva = 1, min = 1, max = 9):
        for i in range(nBrojeva):
            n = DLL.randomN(min, max)
            self.append(n)


class Queue(LL):
    def __init__(self):
        super().__init__()
        self.tail = None

    def isEmpty(self):
        return self.head == None
    
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
        
    def copy(self):
        copyQ = Queue()
        ph = []
        while not self.isEmpty():
            ph.append(self.dequeue())
        for el in ph:
            copyQ.enqueue(el)
            self.enqueue(el)
        return copyQ
    
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

    def isEmpty(self):
        return self.head == None

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
    
    def copy(self):
        copyS = Stack()
        ph = []
        while self.isEmpty() == False:
            ph.append(self.pop())
        ph.reverse()
        for el in ph:
            copyS.push(el)
            self.push(el)
        return copyS
    
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

print('#' * 15)
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
a.insert_per_index(2, 6)
a.insert_per_index(0, 4)
a.insert_per_index(11, 2)
a.insert_per_index(14, 1)
print('Sa index insertom:', a)
ab = LL()
ab.ins_N_rand(5)
print('random brojevi:', ab)

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
b.addLeft(7)
b.addLeft(4)
print(b)

print('\n\n')
print('Queue')
print('#' * 15)
izraz = '1 + 3 6 - - 9 8 + + 7 -'
q1 = Queue()
q1 = Queue.decode(izraz)
print('Og:', q1)
print('Kopija:', q1.copy())

print('\n\n')
print('Stack')
print('#' * 15)
izraz = '1 2 + 3 4 + * 5 +'
reza = Stack.decode(izraz)
print(izraz)
print(reza)
izraz2 = '3 5 + 2 3 + * 7 -'
reza2 = Stack.decode(izraz2)
print(izraz2)
print(reza2)
s = Stack()
s.push(2)
s.push(5)
s.push(7)
print('Og:', s)
print('Kopija:', s.copy())

print('\n\n')
print('#' * 15)
dll = DLL()
dll.append(5)
dll.append(8)
dll.ins_first(2)
dll.ins_first(2)
print(dll)
dll.reverse()
dll.insert_per_index(2, 3)
print('nešto:', dll)
dll.insert_per_index(4, 7)
dll.insert_per_index(10, 1)
print('nešto:', dll)
dll.reverse()
print(dll)
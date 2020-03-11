import time
import hashlib
import bcrypt

​
def myFakeHash(word):
    hash = len(word)
    return hash
​
myFakeHash('Timothy') # --> 7
myFakeHash('sevenns') # --> 7
​
​
# scramble the key and come up with very different values
def djb2(key):
    # start from a large prime number
    hash_value = 5381
​
    # randomly scramble it by using bit-shifting
    for char in key:
        hash_value = hash_value + (hash_value << 5) + char
​
    return hash_value
​
​
key = b"mypassword"
​
n = 10000
​
start_time = time.time()
for i in range(n):
    djb2(key)
end_time = time.time()
​
print("djb2 run time: ", end_time - start_time)
​
​
start_time = time.time()
for i in range(n):
    hashlib.sha256(key)
end_time = time.time()
​
print("sha256 run time: ", end_time - start_time)
​
start_time = time.time()
salt = bcrypt.gensalt()
for i in range(n):
    bcrypt.hashpw(key, salt)
end_time = time.time()
​
print("hashpw run time: ", end_time - start_time) ## omg this takes so long!!


import time
​
class DynamicArray:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * capacity
​
​
    def insert(self, index, value):
​
        if self.count == self.capacity:
            self.double_size()
​
        for idx in range(self.count, index, -1):
            self.storage[idx] = self.storage[idx - 1]
​
        self.storage[index] = value
        self.count += 1
​
    def append(self, value):
        if self.count == self.capacity:
            self.double_size()
​
        self.storage[self.count] = value
​
        self.count += 1
​
    def double_size(self):
        # double the capacity
        self.capacity = self.capacity * 2
        # make a new array twice the size of the old one
        new_arr = [None] * self.capacity
​
        # copy everything over
        for i in range(self.count):
            new_arr[i] = self.storage[i]
​
        self.storage = new_arr
​
# O(n^2)
def add_to_front(n):
    x = []
    for i in range(n):
        x.insert(i, n-1)
    return x
​
# O(n)
def add_to_back(n):
    x = []
    for i in range(n):
        x.append(i)    # between friends we say this is O(1) even though sometimes we have to resize
    return x
​
## Let's NEVER resize! bwahahaha
def preallocate(n):
    x = [None] * n
​
    for i in range(n):
        x[i] = i
​
    return x
​
n = 10000000
start_time = time.time()
add_to_front(n) # O(n^2)
end_time = time.time()
​
print("Time to add to front", end_time - start_time)
​
start_time = time.time()
add_to_back(n) # O(n)
end_time = time.time()
​
print("Time to add to back", end_time - start_time)
​
start_time = time.time()
preallocate(n) # O(n)
end_time = time.time()
​
print("Time to add to back, if we preallocate space", end_time - start_time)
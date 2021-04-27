fruits = ['kumquat', 'Cherimoya', 'Loquat', 'longan', 'jujube']
print(sorted(fruits, key=str.casefold))

from itertools import takewhile, dropwhile
colors = ['red', "oleogusres",'green', 'orange', 'purple', 'pink', 'blue']
def short_length(word): return len(word) < 6
print(list(dropwhile(short_length, colors)))
print(1,2,3,4,5,6,7,8, sep="\n")

from functools import reduce
from itertools import accumulate
num = [2,2,3,4,46,3,6,42,7,265]
def product(x,y):
    return x * y
print(reduce(product,num))
print(list(accumulate(num,product)))

def is_odd(n):
    return n % 2 == 1
vars()
obj = filter(is_odd,num)
print(list(obj))

iss_odd = lambda n : n % 2 == 1
print(iss_odd(266))

greet = lambda name="world" : print(f"hello {name}")
greet("anurag")
greet()

# even numbers
print(list(filter(lambda n: n % 2 == 0, num)))


def shout(text): 
    return text.upper() 
    
def whisper(text): 
    return text.lower() 
    
def greet(func): 
    # storing the function in a variable 
    greeting = func("Hi, I am created by a function \
    passed as an argument.") 
    print(greeting)

greet(shout)
greet(whisper)

def dec_funct(a):
    def wraper_function():
        print("hello")
        a()
    return wraper_function

@dec_funct
def func():
    print("how are you ?")
func()
# or
# dec_func = dec_funct(func)
# dec_func()
def decorator(func):
    def wrapper():
        print("this is before function execution")
        func()
        print("this is after function execution")
    return wrapper

#@decorator
def test_func():
    print("this is inside the function")
#test_func()
# or
var = decorator(test_func)
var()


#
def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner

def decor(func): 
    def inner1(): 
        x = func() 
        return 2 * x 
    return inner1 

@decor1
@decor
def num(): 
    return 10
print(num()) 



# If you need to loop over multiple lists at the same time, use zip
# If you only need to loop over a single list just use a for-in loop
# If you need to loop over a list and you need item indexes, use enumerate

presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for i in range(len(presidents)):
    print("President {}: {}".format(i + 1, presidents[i]))



president = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for num, name in enumerate(president,start=1):
    print("President {}:{} ".format(num, name))

# loop over two lists at once
colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for i, color in enumerate(colors):
    print(i)
    ratio = ratios[i]
    print("{}% {}".format(ratio, color))

# loop over two lists at once
colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
pres = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for color, ratio, pre in zip(colors, ratios, pres):
    print("{}% {} {}".format(ratio * 100, color, pre))


words = ["Welcome", "to", "Python"]
print(words)
print(*words, sep="\n")
print(*words, end="!\n")

# breakpoint()

# This makes an empty set
numb = {*()}
print(numb)

for n in range(0, 50, 2):
    print(n)

one_iterable = [2, 1, 3, 4, 6, 5]
another_iterable = ['A', 'N', 'U', 'R', 'A', 'G']
for n, letter in zip(one_iterable,another_iterable):
    print(n,letter)

# we can do with this iterator is loop over it (but only once)
num = [2,3,1,3,4,5,4]
reversed_num = reversed(num)
# print(list(reversed_num))
# print(list(reversed_num))
for n in reversed_num:
    print(n)


#  other ways to reverse Python lists besides the reversed function:
# Slicing syntax
for n in num[::-1]:
    print(n)

# In-place reverse method
num.reverse()
for n in num:
    print(n)

class Circle:

    def __init__(self, radius=1):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

circle = Circle()
circle.radius = 10
print(circle.diameter)

class Thing():
    pass
thing = Thing()
thing.x = 4
print(getattr(thing,'x'))
setattr(thing,'x',12)
print(thing.x)

numbers = [2,3,1,3,4,5,4]
doubled_odds = []
for n in numbers:
    if n % 2 == 1:
        doubled_odds.append(n*2)
print(doubled_odds)

doubled_odd = [n * 1 for n in numbers if n % 2 == 1]
print(doubled_odd)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {}?  It is {}.'.format(q, a))


fizzbuzz = [
    f'fizzbuzz {n}' if n % 3 == 0 and n % 5 == 0
    else f'fizz {n}' if n % 3 == 0
    else f'buzz {n}' if n % 5 == 0
    else n
    for n in range(0,100,10)
]
print(fizzbuzz)

[print(n) for n in range(1, 11,2)]

    
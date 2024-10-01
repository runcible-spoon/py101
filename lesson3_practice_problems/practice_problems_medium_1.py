import os

os.system('clear')

question = 0

def question_number_banner():
    global question
    question += 1
    print(f"\n\n=============== QUESTION {question} ===============")


question_number_banner()
'''
Question 1

Let's do some "ASCII Art": a stone-age form of nerd artwork from back in 
the days before computers had video screens.

For this practice problem, write a program that outputs The Flintstones 
Rock! 10 times, with each line prefixed by one more hyphen than the line 
above it. The output should start out like this:

-The Flintstones Rock!
--The Flintstones Rock!
---The Flintstones Rock!
    ...
'''

def flintstones_rock():
    dashes = '-'
    for _ in range(10):
        print(f"{dashes}The Flintstones Rock!")
        dashes = dashes + '-'

flintstones_rock()


# ls

for padding in range(1, 11):
    print(f'{"-" * padding}The Flintstones Rock!')


'''
Question 2
'''
question_number_banner()
'''
Alan wrote the following function, which was intended to return all 
of the factors of number:

Alyssa noticed that this code would fail when the input is a negative 
number, and asked Alan to change the loop. 

How can he make this work? 

Note that we're not looking to find the factors for negative numbers, 
but we want to handle it gracefully instead of going into an infinite loop.
'''

def factors(number):
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return print(result)

def factors_rewritten():
    number = int(input("Enter a number to see its factors: "))
    while number <= 0:
        print("enter a positive integer")
        number = int(input())
    
    result = []
    divisor = number

    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return print(result)

# factors_rewritten()

'''
Bonus Question: What is the purpose of number % divisor == 0 in that code?

A: Finds the divisors that do not have remainders when 
they are divided by number, i.e. its factors
'''



'''
Question 3
'''
question_number_banner()
'''
Alyssa was asked to write an implementation of a rolling buffer. 
You can add and remove elements from a rolling buffer. 
However, once the buffer becomes full, any new elements will displace 
the oldest elements in the buffer.

She wrote two implementations of the code for adding elements to the buffer:
'''
def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer
'''
What is the key difference between these implementations?
'''

# They use different methods to add to the object buffer. 
# Append would require buffer to always be a list
# the second implementation allows for different collection types 
# for the buffer argument.

# WRONG: second method doesn't work for dicts either..

# LS: 1 mutates the argument (no-no)


buffer_test_dict = {
    'test1': 'test2'
}

# add_to_rolling_buffer2(buffer_test_dict, 3, {'test3:' 'test4'})
# print(buffer_test_dict)


'''
Question 4
'''
question_number_banner()
'''
What will the following two lines of code output?
'''
print(0.3 + 0.6)
print(0.3 + 0.6 == 0.9)
'''
Don't look at the solution before you answer.
'''

# 0.9
# False

import math

print(0.3 + 0.6)
print(math.isclose(0.3 + 0.6, 0.9))


'''
Question 5
'''

question_number_banner()

'''
What do you think the following code will output?
'''
nan_value = float("nan")

print(nan_value == float("nan"))

# False

'''
Bonus Question

How can you reliably test if a value is nan?
'''

# from docs.python.org: . To check whether a number is a NaN, 
# use the isnan() function to test for NaNs instead of is or ==.

print(math.isnan(nan_value))


'''
Question 6
'''
question_number_banner()
'''
What is the output of the following code?
'''
answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)

# 34

'''
Question 7
'''
question_number_banner()
'''
One day, Spot was playing with the Munster family's home computer, 
and he wrote a small program to mess with their demographic data:
'''
import copy

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}
print(munsters)

def mess_with_demographics(demo_dict):
    new_munsters = copy.deepcopy(demo_dict)
    for key, value in new_munsters.items():
        value["age"] += 42
        value["gender"] = "other"
    return new_munsters
'''
After writing this function, he typed the following code:
'''
print(mess_with_demographics(munsters))
'''
Before Grandpa could stop him, Spot hit the Enter key with his tail. 
Did the family's data get ransacked? Why or why not?
'''
print(munsters)

'''
Question 8
'''
question_number_banner()
'''
Function and method calls can take expressions as arguments. 
Suppose we define a function named rps as follows, which follows 
the classic rules of the rock-paper-scissors game, 
but with a slight twist: in the event of a tie, 
it just returns the choice made by both players.
'''

def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"
'''
What does the following code output?
'''
print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))

# prints 'paper'


'''
Question 9
'''
question_number_banner()
'''
Consider these two simple functions:
'''
def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")
'''
What will the following function invocation return?
'''

print("foo() or 'no'): ", (foo() and 'no'))

print('foo: ',foo())

print('bar: ', bar())

print('bar(foo()): ', bar(foo()))


'''
Question 10
'''
question_number_banner()
'''
In Python, every object has a unique identifier that can be accessed 
using the id() function. This function returns the identity of an object,
which is guaranteed to be unique for the object's lifetime. 

For certain basic immutable data types like short strings or integers, 
Python might reuse the memory address for objects with the same value. 

This is known as "interning".

Given the following code, predict the output:
'''
a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))

# true 

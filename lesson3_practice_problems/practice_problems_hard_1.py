import os

question = 0

def question_number_banner():
    global question
    question += 1
    print(f"\n\n=============== QUESTION {question} ===============")

'''
Question 1
'''
question_number_banner()
'''
Will the following functions return the same results?
'''
def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())
'''
Try to answer without running the code or looking at the solution
'''

# no. second() is formatted incorrectly. 

'''
Question 2
'''
question_number_banner()
'''
What does the last line in the following code output?
'''
dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list) # [1]
print(dictionary) # error: dict_type has no method append # WRONG it worked fine
'''
Try to answer without running the code or looking at the solution.
'''


'''
To modify num_list but not the original dictionary, we could:

initialize num_list with a reference to a copy of the original list:
'''
dictionary = {'first':[1]}
num_list = dictionary['first'].copy()
num_list.append(2)

print(num_list)
print(dictionary)

'''
or use list slicing, which returns a new list:
'''
dictionary = {'first':[1]}
num_list = dictionary['first'].copy()
num_list.append(2)


print(num_list)
print(dictionary)


'''
Question 3
'''
question_number_banner()
'''
Given the following similar sets of code, what will each code snippet print?
'''
# A)
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print('\nA')

print(f"one is: {one}") # one is: ["one"]
print(f"two is: {two}") # two is: ["two"]
print(f"three is: {three}") # three is ["three"]

# B)
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print('\nB')

print(f"one is: {one}") # one is: ["one"]
print(f"two is: {two}") # two is: ["two"]
print(f"three is: {three}") # three is: ["three"]

# C)
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print('\nC')

print(f"one is: {one}") # one is: ['two']
print(f"two is: {two}") # two is: ['three']
print(f"three is: {three}") # three is: ['one']

'''
In this case, the mess_with_vars function modifies the 
content of the lists directly. Since lists in Python 
are mutable and passed by reference, the changes are reflected 
outside the function.
'''


'''
Question 4
'''
question_number_banner()
'''
Ben was tasked to write a simple Python function to determine whether 
an input string is an IP address using 4 dot-separated numbers, 
e.g., 10.4.5.11.

Alyssa supplied Ben with a function named is_an_ip_number. 
It determines whether a string is a numeric string between 
0 and 255 as required for IP numbers and asked Ben to use it. 
'''
def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False
'''
Here's the code that Ben wrote:
'''
def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            break

    return True

'''
Alyssa reviewed Ben's code and said, "It's a good start, but you 
missed a few things. You're not returning a false condition, 
and you're not handling the case when the input string has 
more or less than 4 components, e.g., 4.5.5 or 1.2.3.4.5: 
both those values should be invalid."

Help Ben fix his code.
'''
def is_dot_separated_ip_address():
    input_string = input("Enter an IP address: ")
    dot_separated_words = input_string.split(".")

    while (
        (len(dot_separated_words) <= 3) 
        or 
        (len(dot_separated_words)) >= 5
        ):
        print("Not valid IP address.")
        input_string = input()

    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            print("Not a valid IP address.")
            return False

    print("Valid IP address.")           
    return True

is_dot_separated_ip_address()


# ls 

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False

    while dot_separated_words:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

'''
Question 5
'''
question_number_banner()
'''
What do you expect to happen when the greeting 
variable is referenced in the last line of the code below?
'''
if False:
    greeting = "hello world"

print(greeting)

# NameError: greeting has not been defined

# OR:

# "hello world!" 

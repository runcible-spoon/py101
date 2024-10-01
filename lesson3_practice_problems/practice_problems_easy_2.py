question = 0

def question_number_banner():
    global question
    question += 1
    print(f"=============== QUESTION {question} ===============")

'''
Question 1

Write two distinct ways of reversing the list without mutating the original list.
'''

question_number_banner()

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

numbers_reversed = list(reversed(numbers))
print(numbers_reversed)
print(numbers)

numbers_reversed = numbers[::-1]
print(numbers_reversed)
print(numbers)

'''Question 2

Given a number and a list, determine whether the number is included in the list.
'''

question_number_banner()

numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

print(number1 in numbers)
print(number2 in numbers)

'''
Question 3

Programmatically determine whether 42 lies between 10 and 100, 
inclusive. Do the same for the values 100 and 101.
'''

question_number_banner()

print(42 in range(10, 101))
print(100 in range(10, 101))
print(101 in range(10, 101))

'''
Question 4

Given a list of numbers [1, 2, 3, 4, 5], mutate the list by removing 
the number at index 2, so that the list becomes [1, 2, 4, 5].
'''

question_number_banner()

nums = [1, 2, 3, 4, 5]
print(nums)

nums.remove(2)
print(nums)

# ls
del numbers[2]

'''
Question 5

How would you verify whether the data structures assigned to the variables numbers and table are of type list?
'''

question_number_banner()

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

print(type(numbers), type(table))

# ls

print(type(numbers) is list)
print(type(table) is list)


'''
Question 6

Back in the stone age (before CSS), we used spaces to align things on the screen. 
If we have a 40-character wide table of Flintstone family members, 
how can we center the following title above the table with spaces?
'''

question_number_banner()

title = "Flintstone Family Members"

length = (len(title))
print(length)

spaces = ' '

spaces = spaces * int((length / 2))
print(spaces, title, spaces)


# ls 

centered_title = title.center(40)
print(centered_title)


'''
Question 7

Write a one-liner to count the number of lower-case t characters in
 each of the following strings:
'''

question_number_banner()

statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."


number_of_lowercase_ts = print(statement1.count('t'), statement2.count('t'))


'''
Question 8

Determine whether the following dictionary of people and their age 
contains an entry for 'Spot':
'''

question_number_banner()

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

print('Spot' in ages)


'''Question 9

We have most of the Munster family in our ages dictionary:
'''

question_number_banner()

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}

'''
Add entries for Marilyn and Spot to the dictionary:
'''

additional_ages = {'Marilyn': 22, 'Spot': 237}

ages.update(additional_ages)
print(ages)

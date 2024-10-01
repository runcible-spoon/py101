question = 0

def question_number_banner():
    global question
    question += 1
    print(f"=============== QUESTION {question} ===============")



'''
Question 1

Write two different ways to remove all of the elements from the following list:

'''

question_number_banner()

numbers = [1, 2, 3, 4]

numbers.clear()
print(numbers)


numbers = [1, 2, 3, 4]
numbers = []
print(numbers)

'''
Question 2

What will the following code output?
Try to answer without running the code.
'''
question_number_banner()

print([1, 2, 3] + [4, 5])

# [1, 2, 3, 4, 5]


'''
Question 3

What will the following code output?

Try to answer without running the code.
'''
question_number_banner()
str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)

# hello there


'''
Question 4

What will the following code output?

Try to answer without running the code.
'''
question_number_banner()

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)

#  {"first": "value1"}, {"second": "value2"}, 3, 4, 5

# WRONG: the dictionary values are treated in the same way as nested list objects. 

# So: [{'first': 42}, {'second': 'value2'}, 3, 4, 5] 

'''
Question 5

The following function unnecessarily uses two return statements to 
return boolean values. Can you rewrite this function so it only has 
one return statement and does not explicitly use either True or False?

Try to come up with two different solutions.
'''
question_number_banner()

def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False


def is_color_valid(color):
    return color == 'blue' or 'green'

def is_color_valid(color):
    return color in ['blue', 'green']

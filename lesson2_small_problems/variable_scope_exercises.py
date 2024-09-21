print('Exercises')
print('no. 1')
# What will the following code print and why? Don't run it until you have tried to answer.

num = 5

def my_func():
    print(num)

my_func() # 5

print('no. 2')

# What will the following code print and why? Don't run it until you have tried to answer.

num = 5

def my_func():
    num = 10

my_func() 
print(num) # 5

print('no. 3')
# What will the following code print and why? Don't run it until you have tried to answer.

num = 5

def my_func():
    global num
    num = 10

my_func()
print(num) # 10

print('no. 4')
# What will the following code print and why? Don't run it until you have tried to answer.

def outer():
    outer_var = 'hello'

    def inner():
        inner_var = 'world'
        print(outer_var, inner_var)

    inner()

outer() # hello world



print('no. 5')
# What will the following code do? Don't run it until you have tried to answer.

def my_func():
    num = 10

my_func()
print(num) # NameError

print('no. 6')
# What will the following code print and why? Don't run it until you have tried to answer.

def my_func6():
    x = 15

    def inner_func1():
        x = 25
        print('inner 1: ', x)

    def inner_func2():
        print('inner 2: ', x)

    inner_func1()
    inner_func2()

my_func6() # 25, 15

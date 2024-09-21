a = 1

def foo():
    b = 2

    def bar():
        c = 3
        
        print(a)
        print(b)
        print(c)

    bar()

    print(a)
    print(b)
    print(c)

foo()

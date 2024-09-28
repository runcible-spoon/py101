x = 1
y = 'outer scope'

if x > 1:
    y = 'foo'
    print(y)
if x < 1:
    y = 'bar'
    print(y)
if x == 1:
    y = 'qux'
    print(y)

print(y)

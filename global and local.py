a=10
def f():
    print("inside of f():" ,a)
f()
print("global:",a)
def g():
    a=9
    print("inside of g():",a)

g()
print("global:",a)
def h():
    a=8
    print("inside of h():",a)
h()
print("global:",a)
#define a staic variable and access and change through a class
class static:
    staticVariable=10
print(static.staticVariable)
static.staticVariable=5
print(static.staticVariable)
#access through instance and change instance
instance =static()
print(instance.staticVariable)
instance.staticVariable=20
print(instance.staticVariable)
print(static.staticVariable)
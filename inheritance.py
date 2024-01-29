class A():
    def display(dp):
        print("Display inside class A")
    def show(self):
        print("Show Inside class A")
class B(A):
    def print(pt):
        print(("print Inside class B"))
    def show(self):
        print("show inside class B")
class C(B):
    def show(self):
        print("show inside class C")
s=A()
s.display()
s.show()
k=B()
k.print()
k.show()
g=C()
g.show()

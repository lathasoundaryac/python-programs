class A:
    def __init__(self):
        self.name="latha"
    def print_A(self):
        print(self.name)
obj=A()
obj.print_A()

class B(A):
    def __init__(self):
        self.name="soundarya"
    def print_B(self):
        print(self.name)
obj=B()
obj.print_B()
class C:
    name=None
    _roll=None
    _branch=None
    def __init__(self,name,roll,branch):
        self.name=name
        self._roll=roll
        self._branch=branch
    def dispalyName(self):
        print("Name :",self.name)
    def _dispalyRoll(self):
        print("Roll :", self._roll)
    def _displayBranch(self):
        print("Branch :",self._branch)
    def access_displayBranch(self):
        self._displayBranch()

class D(C):

    def __init__(self,name,roll,branch):
        super().__init__(name,roll,branch)




obj=D("Sony",40,"CSE")
obj.dispalyName()
obj.access_displayBranch()


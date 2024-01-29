class super:
    var1=None
    _var2=None
    _var3=None
    def __init__(self,var1,var2,var3):
        self.var1=var1
        self._var2=var2
        self._var3=var3
    def displaypublicmember(self):
        print("public member :",self.var1)
    def _displayproctedmember(self):
        print("procted member :",self._var2)
    def _displayprivatemember(self):
        print("private member :",self._var3)
    def accessprivatemember(self):
        self._displayprivatemember()
class sub(super):
    def __init__(self,var1,var2,var3):
              super.__init__(self,var1,var2,var3)
    def accessproctedmember(self):
        self._displayproctedmember()
obj=sub("KG",5,"KG !")
obj.displaypublicmember()
obj.accessproctedmember()
obj.accessprivatemember()

print("object is accessing protected member :",obj._var2)
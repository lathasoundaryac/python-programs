from abc import ABC,abstractmethod
class polgon(ABC):
    @abstractmethod
    def noofsides(self):
        pass
class triangel(polgon):
    def noofsides(self):
        print(("triangle:I have 3 sides"))
class square(triangel):
    def noofsides(self):
        print("square:I have 4 sides")

T=triangel()
T.noofsides()
R=square()
R.noofsides()

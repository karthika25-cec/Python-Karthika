class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def __lt__(self,other):
        return self.area()<other.area()
l1=int(input("Enter the length of first rectangle:"))
w1=int(input("Enter the width of first rectangle:"))
l2=int(input("Enter the length of second rectangle:"))
w2=int(input("Enter the width of second rectangle:"))
r1=Rectangle(l1,w1)
r2=Rectangle(l2,w2)
if r1<r2:
    print("R1 has smallest area.")
else:
    print("R2 has smallest area.")
    

# put your python code here
class1 = int(input())
class2 = int(input())
class3 = int(input())

odd1 = class1 % 2
odd2 = class2 % 2
odd3 = class3 % 2

desks1 = (class1+odd1)/2
desks2 = (class2+odd2)/2
desks3= (class3+odd3)/2

print(int(desks1+desks2+desks3))
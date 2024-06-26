####    Classes and object exploration


class A:
   def __init__(self, c):                       ## constructor
       print("---------Inside class A----------")
       self.c = c  #### initiation
   print("Print inside A.")

   def alpha(self):
       c = self.c + 1
       return c

print(dir(A))
print("Instantiating A..")
a = A(1)
print(a.alpha())

class B:
   def __init__(self, a):
       print("---------Inside class B----------")
       self.a = a

   print(a.alpha())     ###  Calling method alpha() over object of class A 
   d = 5
   print(d)
   print(a)

print("Instantiating B..")
b = B(a)
print(a)                ###   Instantiating object a over class B *
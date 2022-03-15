#class Rectangle:
    # define constructor with attributes: length and width 
 #   def __init__(self, length , width):
  #      self.length = length
   #     self.width = width
        
    # Create Perimeter method
    #def Perimeter(self):
     #   return 2*(self.length + self.width)
    
    # Create area method
    #def Area(self):
     #   return self.length*self.width   
    
    # create display method
    #def display(self):
     #   print("The length of rectangle is: ", self.length)
      #  print("The width of rectangle is: ", self.width)
       # print("The perimeter of rectangle is: ", self.Perimeter())
        #print("The area of rectangle is: ", self.Area())
#class Parallelepipede(Rectangle):
 #   def __init__(self, length, width , height):
  #      Rectangle.__init__(self, length, width)
   #     self.height = height
        
    # define Volume method
    #def volume(self):
     #   return self.length*self.width*self.height
        
#myRectangle = Rectangle(7 , 5)
#myRectangle.display()
#print("----------------------------------")
#myParallelepipede = Parallelepipede(7 , 5 , 2)
#print("the volume of myParallelepipede is: " , myParallelepipede.volume())

#class Person:
    # define constructor with name and age as parameters
 #   def __init__(self, name, age):
  #      self.name = name
   #     self.age = age
    # create display method fro Person class
    #def display(self):
        #print("Person name : ", self.name)
        #print("Person age = ", self.age)
    
# create child class Student of Person class
#class Student(Person):
    # define constructor of Student class with section additional parameters 
 #   def __init__(self, name , age , section):
  #      Person.__init__(self,name, age)
   #     self.section = section
    
    # Create display method for Student class
    #def displayStudent(self):
     #   print("Student name : ", self.name)
      #  print("Student age = ", self.age)
       # print("Student section = ", self.section)
    
# Testing Person class
#P = Person("Thomas Ogega", 37)
#P.display()
#print("-------------------------------")
#S = Student("Jahmiel", 23 , "Mathematics")
#S.displayStudent()

#class BankAccount:
    # create the constuctor with parameters: accountNumber, name and balance 
 #   def __init__(self,accountNumber, name, balance):
  #      self.accountNumber = accountNumber
   #     self.name = name
    #    self.balance = balance
        
    # create Deposit() method
    #def Deposit(self , d ):
     #   self.balance = self.balance + d
    
    # create Withdrawal method
    #def Withdrawal(self , w):
     #   if(self.balance < w):
      #      print("impossible operation! Insufficient balance !")
       # else:
        #    self.balance = self.balance - w
    # create bankFees() method
    #def bankFees(self):
     #   self.balance = (95/100)*self.balance
        
    # create display() method
    #def display(self):
     #   print("Account Number : " , self.accountNumber)
      #  print("Account Name : " , self.name)
       # print("Account Balance : " , self.balance , " $")
        
# Testing the code :
#newAccount = BankAccount(2178514584, "Albert" , 2700)
# Creating Withdrawal Test
#newAccount.Withdrawal(300)
# Create deposit test
#newAccount.Deposit(200)
# Display account informations
#newAccount.display()

#from math import pi
#class Circle:
 #   def __init__(self, a, b, r):
  #      self.a = a
   #     self.b = b
    #    self.r = r

#    def perimeter (self):
 #       return  2 * pi * self.r


  #  def area (self):
   #     return  pi * self.r**2
    

    # form of the cercle equation 
   # def formEquation (self, x, y):
    #    return (x-self.a)**2 + (y-self.b)**2 - self.r**2
    
    # method to test if given point blong to the circle or not 
    #def test_belong (self, x, y):
     #   if (self.formEquation (x, y) == 0):
      #      print ("the point: (", x, y, ") belongs to the circle C")
       # else:
        #    print ("the point: (", x, y, ") does not belong to the circle C")


# Creating of an instance object
#C = Circle (1,2,1)

#print ("the perimeter of the circle C is:", C.perimeter() )
#print ("the area of circle C is:", C.area())
# we test if the point(1,1) belong to the circle or not
#C.test_belong(1,1) 
# The output is:
#the perimeter of the circle C is: 6.283185307179586
#the area of circle C is: 3.141592653589793
#the point: ( 1 1 ) belongs to the circle C

#class Computation:
  #  def __init__ (self):
 #       pass
# --- Factorial ------------
   # def factorial(self, n):
    #    j = 1
     #   for i in range (1, n + 1):
      #      j = j * i
       # return j
    
# --- Sum of the first n numbers ----
    #def sum (self, n):
     #   j = 1
      #  for i in range (1, n + 1):
       #     j = j + i
        #return j
    
# --- Primality test of a number ------------
    #def testPrim (self, n):
     #   j = 0
      #  for i in range (1, n + 1):
       #     if (n% i == 0):
        #        j = j + 1
        #if (j == 2):
         #   return True
        #else:
         #   return False

# --- Primality test of two integers ------------
    #def testprims (self, n, m):
        
        # initialize the number of commons divisors
     #   commonDiv = 0
      #  for i in range (1, n + 1):
       #     if (n% i == 0 and m% i == 0):
        #        commonDiv = commonDiv + 1
        #if commonDiv == 1:
        #    print ("The numbers", n, "and", m, "are co-primes")
        #else:
         #   print ("The numbers", n, "and", m, "are not co-primes")

#---Multiplication table-------------
    #def tableMult (self, k):
     #   for i in range (1,10):
      #      print (i, "x", k, "=", i * k)

# --- All multiplication tables of the numbers 1, 2, .., 9
    #def allTables (self):
     #   for k in range (1,10):
      #      print ("\nthe multiplication table of:", k, "is:")
       #     for i in range (1,10):
        #        print (i, "x", k, "=", i * k)

# ----- list of divisors of an integer
#    def listDiv (self, n):
        # initialization of the list of divisors
 #       lDiv = []
  #      for i in range (1, n + 1):
   #         if (n% i == 0):
    #            lDiv.append (i)
     #   return lDiv

# ------ list of prime divisors of an integer ----------------
    #def listDivPrim (self, n):
        # initialization of the list of divisors
     #   lDiv = []
      #  for i in range (1, n + 1):
       #     if (n% i == 0 and self.testPrim (i)):
        #        lDiv.append (i)
        #return lDiv

# Instantiation example
#Comput= Computation ()
#Comput.testprims (13, 7)
#print ("List of divisors of 18:", Comput.listDiv (18))
#print ("List of prime divisors of 18:", Comput.listDivPrim (18))
#Comput.allTables ()



# Question 1
#class Book:
     # Question 2
 #    def __init__(self , Title , Author , Price):
  #        self.Title    =  Title
   #       self.Author   =  Author
    #      self.Price    =  Price
          
     # Question 3
     #def view(self ):
      #    return ("Book Title: " , self.Title ,  "Book Author: " , self.Author, "Book Price: " , self.Price)
          
# Question 4
#MyBook = Book("Python Crash Course" , "Thomas" , "23 $")          
#print( MyBook.view())
# The output: ('Book Title: ', 'Python Crash Course', 'Book Author: ', 'Eric Matthes', 'Book Price: ', '23 $'


#import math
#p1 = [4, 0]
#p2 = [6, 6]
#distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

#print(distance)



#from tkinter import*
# Question 1
#class TK_extended(Tk):

 #   def __init__(self, master , title):
  #      self.master = master
   #     self.title = title
    #------------    
    # Question 2 
    #------------
    #def create(self):
     #   self.master = Tk()
      #  self.master.title(self.title)        
    
    #------------    
    # Question 3 
    #------------        
    #def resize(self, width , height):
     #   self.master.geometry("{}x{}".format(width , height))
       
    #------------    
    # Question 4 
    #------------     
    #def generate(self):
     #   self.master.mainloop() 
        
        
#------------    
# Execution 
#------------        
#root = TK_extended("win" , "My Window")
#root.create()
#root.resize(500 , 300)
#root.generate()

# Python 3 Program to convert str1 to
# str2 in exactly k operations
 
# Returns true if it is possible to convert
# str1 to str2 using k operations.
#def isConvertible(str1, str2, k):
     
    # Case A (i)
 #   if ((len(str1) + len(str2)) < k):
  #      return True
 
    # finding common length of both string
   # commonLength = 0
    #for i in range(0, min(len(str1),
       #                   len(str2)), 1):
     #   if (str1[i] == str2[i]):
      #      commonLength += 1
       # else:
        #    break
 
    # Case A (ii)-
    #if ((k - len(str1) - len(str2) + 2 *
      #          commonLength) % 2 == 0):
     #   return True
 
    # Case B-
    #return False
 
# Driver Code
#if __name__ == '__main__':
 #   str1 = "geek"
  #  str2 = "geek"
   # k = 7
   # if (isConvertible(str1, str2, k)):
    #    print("Yes")
    #else:
     #   print("No")
 
    #str1 = "geeks"
    #str2 = "geek"
    #k = 5
    #if (isConvertible(str1, str2, k)):
    #    print("Yes")
    #else:
     #   print("No")
 

import math

class Computation:
    def __init__(self):pass

#factorial of a number
def factorial(self, integer):
  if integer == 0:return 1
    else:return integer * self.factorial(integer - 1)

#sum of first n number
def Sum(self, integer):
return sum(range(1, integer + 1))

#test if integer is a prime number
def testPrim(self, integer):
if integer >= 1:
for i in range(2, integer // 2):
if (integer % i) == 0:
print(f"{integer} is not a prime number")
break
else:
print(f'{integer} is a prime number')


#test if the number between the given integers are prime number
def testPrims(self, integer, another_integer):
if integer < another_integer:
for i in range(integer, another_integer + 1):
for j in range(2, i):
if (i % j) == 0:
print(f"{i} is not a prime number")
break
else:
print(f"{i} is a prime number")


#multiplication table of a given integer
def tableMult(self, integer):
print(f"Multiplication Table of {integer}")
for i in range(1,11):
print(f"{integer} x {i} = {integer * i} ")

#multiplication tables 1-9
def allTableMult(self):
for i in range(1,11):
print(f"Multiplication table of {i}")
for j in range(1, 11):
print(f'{j} x {i} = {j * i}')

#list divisor of a number
def listDiV(self, n):
LDiv = []
for i in range(1, int(math.sqrt(n)) + 1):
if n % i == 0:
yield i
if i * i != n:
LDiv.append(n//i)
for divisor in reversed(LDiv):
yield divisor

#prime divisor of a list
def listDivPrim(self, integer):
lst = []
for i in range(1, int(math.sqrt(integer) + 1)):
if integer % i == 0:
lst.append(i)
if i * i != integer:
lst.append(integer // i)
#lst.sort()
#print(lst)
for k in lst:
if k >= 1:
for h in range(2, k):
if k % h == 0:
#print(f"{k} is not a prime number")
break
else:
print(f"Prime Divisor of {integer}: {k}")


fact = Computation()
print(f"Factorial: {fact.factorial(4)}")
print(f'Sum of a given integer: {fact.Sum(5)}')
print("Test if a number is prime or not:")
fact.testPrim(5)
fact.testPrim(6)
print('\n')
print("Test if two numbers are prime number between them: ")
fact.testPrims(13,15)
print('\n')
print("Display the multiplication table of a given integer")
fact.tableMult(4)
print('\n')
print("Display the multiplication table 1-10")
fact.allTableMult()
print('\n')
print("Display the divisor of a given integer")
print(list(fact.listDiV(100)))
print('\n')
print("Show the prime divisor of a given integer")
fact.listDivPrim(100)
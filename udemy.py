#exercise
'''st = 'Print only the words that start with s in this sentence'
words = st.split()
lst = [word for word in words if word[0]=='s']#returns all words that begins with s
print(lst)


lst = [number for number in range(1, 50) if number%3 == 0]
print(lst)'''
#even and odd numbers length of words
'''st = 'Print every word in this sentence that has an even number of letters'
words = st.split()
#print(len(words))
for word in words:
    if len(word)%2 ==0:
        print("this word: ", word.upper(), " is an even word")
    else:
        print("this word: ", word.upper(), " is an odd word")'''
#multiples of three, five and three&five
'''for number in range(1, 100):
    if number%3== 0 and number%5== 0:
        print('FizzBuzz')
        continue
    elif number%3== 0:
        print('Fizz')
        continue    

    elif number%5 ==0:
        print('Buzz')
        continue
    print(number)'''

'''st = "Create a list of the first letters of every word in this string"
words= st.split()
lst = [word[0] for word in words]
print(lst)'''

#prime numbers
'''def is_prime(num):
    for n in range(2,num):
        if num % n == 0:
            return "Not Prime"
    else:
        return "The number is a prime number!"

print(is_prime(9))

'or'
'''
'''import math
def is_prime(num):
    if num %2 == 0 and num> 2:
        return False
    for i in range(3,int(math.sqrt(num)) +1, 2):
        if num % i ==0:
            return False
    return True

print(is_prime(71))'''

#lamda expression:one line condensed version of an expression
#normal
'''def square(num):
    return num**2 
#lambda
square = lambda num:num**2
print(square(3))

#lambda for even
even = lambda num: num%2 == 0
def even(num):
    return num%2 ==0

#lambda for first letter of string
first = lambda s: s[0]
print(first('hello'))'''

'''def adder(x, y):
    return x+y
'''

'''adder = lambda x, y: x + y
print(adder(1,2))'''

#exercise2
'''
def vol(rad):
    return (4.0/3)*3.142*rad**3

print(vol(2))'''

'''def ran_check(num, low, high):
    if num in range(low, high):
        return True
    else: 
        return False

print(ran_check(99, 2, 77))'''
'''
sample_string = 'Hello Mr.Rogers, how are you this fine Tuesday?'
import string
def up_low(s):
    up_count = 0
    low_count = 0
    for word in s:
        if word== word.upper():
            if word in string.ascii_letters:
                up_count += 1
                print(word)
        elif word== word.lower():
            low_count+= 1
    print("No. of Upper case characters: ", up_count)
    print("No. of Lower case characters: ", low_count)

up_low('Hello Mr.Rogers, how are you this fineTuesday?')
'''

'''def unique_list(l):
    print(list(set(l)))

unique_list([1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,5])'''

'''def multiply(numbers):
    first = 1
    for number in numbers:
        first*= number
    print(first)

multiply([1,2,3,-4])'''

'''import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset<= set(str1.lower())


print(ispangram("The quick, brown fox jumps over the lazy dog"))

print(ispangram('abcdefghijklmnopqrstuvwxyz'))
alphabet = string.ascii_lowercase'''


#OOP
'''class Dog(object):

    species = 'mammal'
    legged = 4
    location = 'land'

    def __init__(self,breed,name, fur_color,fur= True):
        self.breed = breed
        self.name = name 
        self.fur = fur 
        self.fur_color = fur_color


sam= Dog(breed ="husky", name= "Samwell Tally", fur_color = "brown")
print(sam.name)'''

#circle class
'''class Circle(object):
    #class object attribute
    pi = 3.14
    #all methods within a class must take self as an argument
    def __init__(self, perimeter=True, radius=1):
        self.radius = radius
        #self.perimeter = self.radius, Circle.pi
        #this attribute is the same as the method perimeter

    def area(self):
        #radius**2 *pi
        return (self.radius**2) * Circle.pi

    def set_radius(self, new_radius):
        ''''''''This methods takes in a radius, and resets the current radius''''''''
        self.radius = new_radius

    def get_radius(self):
        return self.radius

    def perimeter(self):
        return self.radius, Circle.pi

c= Circle(radius = 100)
c.set_radius(new_radius=45)
print(c.radius)#this is an attribute, so no ()
print(c.get_radius())#this is a method, so ()
print(c.perimeter)'''
 

#inheritance of OOP
'''class Animal:

    def __init__(self):
        print('Animal Created')

    def whoAmI(self):
        print('Animal')
    
    def eat(self):
        print('Eating')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    def whoAmI(self):
        print('Dog')

    def bark(self):
        print('woof!')


d =Dog()
d.eat'''

#exercise3
'''class Line(object):
    def __init__(self, coor1, coor2):
        self.coor1= coor1
        self.coor2= coor2
        self.coordinate = coor1, coor2



    def distance(self):
        x1,y1 =self.coor1
        x2,y2 = self.coor2
        return ( (x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        x1,y1 =self.coor1
        x2,y2 = self.coor2
        return float(y2-y1)/(x2-x1)

coordinate1 = Line(coor1= 3, coor2= 2).coordinate
coordinate2 = Line(coor1= 8, coor2= 10).coordinate
li = Line(coordinate1, coordinate2)
print(coordinate1)
print(coordinate2)
print(li.distance())'''

'''coordinate1= (3, 2)
coordinate2 (8, 10)
li = Line(coordinate1, coordinate2)
li.distance() =9.433981132056603
li.slope() = 1.6'''

'''class Cylinder(object):
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.radius= radius
        self.height= height

    def volume(self):
        return Cylinder.pi *(self.radius**2) *self.height

    def surface_area(self):
        return Cylinder.pi *(self.radius)* self.height

c = Cylinder(2, 3)
print(c.surface_area())'''




'''x = 0
def string_length(my_string):
        return len(my_string)'''

#other methods in OOP
class Book:
    book_number = 0
    def __init__(self, book, author, pages):
        self.book = book
        self.author = author
        self.pages = pages
        self.book_number +=1

    def __str__(self):
        return "Book: %s, Author:%s, Pages: %s" %(self.book, self.author, self.pages)

    def __len__(self):
        return self.pages
print(Book.book_number)
b = Book("Python", "Jose", 100)
c = Book("acotar", "Sarah J Maas", 372)
print(c)
print(b)
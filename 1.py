# i = 5
# while True:
#   print(i)
#   i = i - 1
#   if i <= 2:
#     break

# nums=list(range(5))
# print(nums[4])

# a=2005
# b=2011
# print(list(range(a, b)))

# list = [1, 1, 2, 3, 5, 8, 13]
# list[2] = "qwe"
# list.insert(3, "qqq")
# print(list)

# for i in range(10):
#   if not i % 2 == 0:
#     print(i+1)

# import json
# initialize different data
# str_data = 'normal string'
# int_data = 1
# float_data = 1.50
# list_data = [str_data, int_data, float_data]
# nested_list = [int_data, float_data, list_data]
# dictionary = {
#     'int': int_data,
#     'str': str_data,
#     'float': float_data,
#     'list': list_data,
#     'nested list': nested_list
# }

# convert them to JSON data and then print it
# print('String :', json.dumps(str_data))
# print('Integer :', json.dumps(int_data))
# print('Float :', json.dumps(float_data))
# print('List :', json.dumps(list_data))
# print('Nested List :', json.dumps(nested_list, indent=4))
# print('Dictionary :', json.dumps(dictionary, indent=4))  # the json data will be indented

# sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# print(sqs[7:5:-1])

# nums = [5, 42, 7, 1, 0]
# res = nums[::-1]
# print(res)

# str_inp = "hello"
# last_char = str_inp[-1::]
# resu = str_inp[1:-1]
# resul = str_inp[0:3]
# print(resul)

# x = [6, 4, 2, 9]
# x = x[::-1]
# print(x[0]+x[2])

# N = 100
# #your code goes here
# sum = 0
# for i in range(1, N+1):
#     sum += i
# print(sum)

# list = [8, 4, 2, 6]
# list.remove(2)
# print(len(list)+list.count(6))

# nums = [2,4,8,9,5]
# nums.insert(1, 3)
# print(nums)
# nums.remove(9)
# print(nums)
# nums.insert(0, nums.count(8))
# print(nums)
# print(nums[3])

# res = 0
# for i in range(3):
#     res+=i
# print(res)

# try:
#     print(1 / 0)
# except ZeroDivisionError:
#     raise ValueError

# print(0)
# assert "h" != "w"
# print (1)
# assert False
# print(2)
# assert True
# print(3)

# file = open("filename.txt", "r")
# print(file.readlines())
# for i in range(21):
#     print(file.read(4))
# file.close()

# names = ["John", "Oscar", "Jacob"]

# file = open("names.txt", "w+")
# file.write('\n'.join(names))
#write down the names into the file
# for name in names:
#     file.write('%s\n'% name)
    # file.write("\n")
# file.close()

# file= open("names.txt", "r")
#output the content of file in console
# print(file.read())
# file.close()

# try:
#     f = open("filename.txt")
#     print(f.read())
#     print(1 / 0)
# finally:
#     f.close()
#     print("FFF")

# try:
#     print(1)
#     assert 2 + 2 == 5
# except AssertionError:
#     print(3)
# except:
#     print(4)

# file = open("books.txt", "r")
# rows=file.readlines()
# count=int(len(rows))
# print(count)
# print(range(count))
# for row in rows:
    # print(row[0]+str(len(row.rstrip('\n'))))
    # print(row[0]+str(len(row.replace('\n',''))))

    # if row not in '\n':
    # str=file.readlines()[i]
        # print(row)
    # elif row in '\n':
        # continue
    # row+=1
    # while file.readlines()[i] not in "\n":
    # readf=file.readlines()[i]
    # print(readf)
# items= read.join(' ')
# for item in read:
# if  '\n' not in read:
    #   tit=item[0]
    #   chars=[]
    #   for i in item:
# items=''.join(read)
# print(items[0])
# print(len(items))
# for item in items:
    # print(item)
    # tit=item[0]
    # count=len(item)
# print(str(tit)+str(count))
        #   chars.append(item[i])
# else:
    # continue 
    # print(tit+str(len(chars)))

# file.close()

# file = open("books.txt", "r")
# list = file.readlines()
# for row in list:
#      row = row.replace('\n', '')
#      title = row[0] 
#      print(title + str(len(row)))
# file.close()

# fib = {1: 1, 2: 1, 3: 2, }
# print(fib.get(4, "N") + str(fib.get(7, 5)))

# import math

# p1 = (23, -88)
# p2 = (6, 42)
# x = int((p2[0]-p1[0])*(p2[0]-p1[0]))
# y = int((p2[1]-p1[1])*(p2[1]-p1[1]))
# d=math.sqrt(x+y)
# print(d)
# str="42 vbgt dfrt"
# str="vbgtd atril"
# elements=str.split()
# if len(elements)==1:
# numbers=[5, 4, 3, 2, 1]
# print(numbers[::-1])
# print(elements[-1::])
# nums=(55,44,33,22)
# print(abs(-42))
# print(nums[:2])
# print(min(nums[:2]))
# print(max(min(nums[:2]), abs(-42)))

# else:
# print(elements[-1][-1])

# evens=[i**2 for i in range(10) if i**2 % 2 == 0]
# print(evens)

# x=75
# list=[i for i in range(x) if i%5 == 0 and i%3==0 ]
# print(list)

# txt="asd vngyru xcvftryd nnn"
# txt=txt.split()
# print(txt)
# wordl=''
# for word in txt:
#     if len(word) > len(wordl):
#         wordl= word
# print(wordl)
    
# def test(func, arg):
#     return func(func(arg))

# def mult(x):
#     return x * x

# print(test(mult, 2))

# names = ["David", "John", "Annabelle", "Johnathan", "Veronica"]
# print(list(filter(lambda x: len(x) > 5, names)))
#your code goes here
# def long(x):
#     out = []
#     for word in x:

#         if len(word)>5:
#             out.append(word)
    # print(out)
    # return out
# print(long(names))
# word=list(filter(long, names))
# print(word)

# def make_word():
#     word = ""
#     for ch in "spam":
#         word +=ch
#         yield word

# print(list(make_word()))

# def sum_to(x):
#     if x==1:
#         return 1
#     return x + sum_to(x-1)
# print (sum_to(5))

# def is_even(x):
#   if x == 0:
#     return True
#   else:
#     return is_odd(x-1)

# def is_odd(x):
#   return not is_even(x)
# print(is_odd(17))

# set1 = {2, 4, 5, 6}  
# set2 = {4, 6, 7, 8, 11, 42, 2}  
# print(set1-set2)

# nums = {1, 2, 3, 4, 5, 6}
# nums = {0, 1, 2, 3} & nums
# nums = filter(lambda x: x > 1, nums)
# print(len(list(nums)))

# def power(x, y):
#     if y == 0:
#         return 1
#     else:
#         return x * power(x, y-1)

# print(power(2, 3))

# a=(lambda x: x* (x+1)) 
# (6)
# print(a)

# class Student:
#     def __init__(self, name):
#         self.name = name
  
#     def sayHi(self):
#         print("Hi from "+self.name)
  
# s1 = Student("Amy")
# s1.sayHi()

# class Vehicle: 
#   def horn(self):
#     print("Beep!")

# class Car(Vehicle):
#   def __init__(self, name, color):
#     self.name = name
#     self.color = color

# obj = Car("BMW", "red")
# print(obj.horn())

# class SpecialString:
#     def __init__(self, cont):
#         self.cont = cont

#     def __truediv__(self, other):
#         line = "=" * len(other.cont)
#         print(line)
#         return "\n".join([other.cont, line, self.cont])

# spam = SpecialString("spam")
# hello = SpecialString("Hello world!")
# print(spam / hello)
# print(hello / spam)

# import random
# class VagueList:
#     def __init__(self, cont):
#         self.cont = cont

#     def __getitem__(self, index):
#         return self.cont[index + random.randint(-1, 1)]

#     def __len__(self):
#         return random.randint(0, len(self.cont)*2)

# vague_list = VagueList(["A", "B", "C", "D", "E"])
# print(len(vague_list))
# print(len(vague_list))
# print(vague_list[2])
# print(vague_list[0])

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def __add__(self, other):
#         return BankAccount(self.balance + other.balance)
        

# a = BankAccount(1024)
# b = BankAccount(42)

# result = a + b
# print(result.balance)

# a = 42  # Create object <42>
# b = a  # Increase ref. count  of <42> 
# c = [a]  # Increase ref. count  of <42> 

# del a  # Decrease ref. count  of <42>
# b = 100  # Decrease ref. count  of <42> 
# c[0] = -1  # Decrease ref. count  of <42>

# class BankAccount:
#     def __init__(self, balance):
#         self._balance = balance

#     def __repr__(self):
#          return "Account Balance: {}".format(self._balance)
    
#     def deposit(self, amount):
#         #your code goes here
#         self._balance += amount
#         return self._balance

# acc = BankAccount(0)
# acc.deposit(int(input()))
# print(acc)

# 
# spaces = 0

# Display message if spaces are available
# if spaces >0:
#   print("Available spaces")

# Display a different message if spaces are not available
# else:
    # print("Sorry, the parking lot is full")

# players = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

#Create 3 lists with 2 players each
#Use slicing to create a list for Group 1
# g1 = players[0:2]

#Use slicing to create a list for Group 2
# g2 = players[2:4]

#Use slicing to create a list for Group 3
# g3 = players[4:6]

# print("Group 1:",g1)
#display the 1st group

# print("Group 2:",g2)
#display the 2nd group


# print("Group 3:",g3)
#display the 3rd group

#taking the weight as input
# weight =12

#complete the function
# def shipping_cost(mas):
#     calc=mas*5
#     return mas*5
     

#function call
# shipping_cost(weight)
# print(shipping_cost(weight))

# contacts = [
#     ('James', 42),
#     ('Amy', 24),
#     ('John', 31),
#     ('Amanda', 63),
#     ('Bob', 18)
# ]
# name = 'Amy'
# for contact in contacts:
#   if name == contact[0]:
#     print(name, 'is', contact[1])
#     exit()
# print('Not found')

# a, b, c, d, *e, f, g = range(20)
# print(len(e))

# letters = {"a", "b", "c", "d"}
# if "e" not in letters:
#   print(1)
# else:
#   print(2)

# skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
# job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}
# intersect = skills&job_skills
# print(intersect)

# a = 7
# b = 42
# a,b = b,a
# print(b, a)

# price = 23
# perc = 7 
# res = (lambda x,y:x*(y/100))(price, perc) 
# print(res)

# nums = [11, 22, 33, 44, 55]
# result = list(map(lambda x: x+5, nums))
# print(result)

# def isPrime(x):
#     if x < 2:
#         return False
#     elif x == 2:
#         return True  
#     for n in range(2, x):
#         if x % n ==0:
#             return False
#     return True

# def primeGenerator(a, b):
#     #your code goes here
#     for y in range(a, b):
#       if isPrime(y):
#         yield y

    
# f = 3
# t = 61

# print(list(primeGenerator(f, t)))

# def convert(num):
#   if num == 0:
#     return 0
# #   elif num == 1:
#     # return 1
#   else: 
#    return (num % 2 + 10 * convert(num // 2))
# x = 1
# print(convert(x)) 

# class Player: 
#     def __init__(self, name, level): 
#         self.name = name 
#         self.level = level 
#     def intro(self): 
#         print(self.name + " (Level " + str(self.level) + ")") 
#         #your code goes here 
# n="Ann" 
# i=3 
# player=Player(n,i) 
# player.intro()

# class Student:
#   def __init__(self, name):
#     self.name = name
# test = Student("Bob")
# print(test)

# class Student:
#   def __init__(self, name):
#     self.name = name
  
#   def sayHi(self):
#     print("Hi from "+ self.name)
  
# s1 = Student("Amy")
# s1.sayHi()

# class Shape: 
#     def __init__(self, w, h): 
#         self.width = w 
#         self.height = h 
#     def area(self): 
#         return self.width*self.height 
#     def __gt__(self, other): 
#         return (self.area() > other.area()) 
#     def __add__(self, other): 
#         return Shape(self.width + other.width, self.height + other.height) 
# w1 = 5 #int(input()) 
# h1 = 7 #int(input()) 
# w2 = 3# int(input()) 
# h2 = 8#int(input()) 
# s1 = Shape(w1, h1) 
# s2 = Shape(w2, h2) 
# result = s1 + s2 
# print(result.area()) 
# print(s1 > s2)

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def calculate_area(self):
#         return self.width * self.height

#     @classmethod
#     def new_square(cls, side_length, side_width):
#         return cls(side_length, side_width)

# square = Rectangle.new_square(5, 8)
# print(square.calculate_area())


# class Pizza:
#   def __init__(self, toppings):
#     self.toppings = toppings
#   @staticmethod
#   def validate_topping(topping):
#     if topping == "pineapple":
#       raise ValueError("No pineapples!")
#     else:
#       return True

# ingredients = ["cheese", "onions", "spam"]
# if all(Pizza.validate_topping(i) for i in ingredients):
#   pizza = Pizza(ingredients)

# class Person:
#   def __init__(self, name):
#     self._name = name
#   @property
#   def name(self):
#     return self._name
  
#   @name.setter
#   def name(self, value):
#     self.value = value


# tweet = "zaqwsxcderfvtgbnhyu"

# file = open("books.txt", "r")
# for i in range(21):
#   print(file.read(4))
# for line in file.readlines():
#     print(line)
# N = int(input())
# N = 4
# chars = file.read(N)
# print(chars)

# file.close()

# list = []
# with open("books.txt") as f:
   #your code goes here
  # while not "EOF":
  # lines = f.readlines()
  # for i in range (len(lines)):
  #   print("Line "+ str(i+1)+ ": "+str(len(lines[i].split()))+" words")
  # print(list)
    
# class Number:
#   def __init__(self, num):
#     self.value = num 
#       #your code goes here
#   @property 
#   def isEven(self): 
#     if self.value % 2 == 0: 
#       return True 
#     else:
#       return False 
# x = Number(int(input()))
# print(x.isEven)


# def get_input():
#   command = input(": ").split()
#   verb_word = command[0]
#   if verb_word in verb_dict:
#     verb = verb_dict[verb_word]
#   else:
#     print("Unknown verb {}". format(verb_word))
#     return

#   if len(command) >= 2:
#     noun_word = command[1]
#     print (verb(noun_word))
#   else:
#     print(verb("nothing"))

# def say(noun):
#   return 'You said "{}"'.format(noun)

# verb_dict = {
#   "say": say,
# }

# while True:
#   get_input()

# class GameObject:
#   class_name = ""
#   desc = ""
#   objects = {}

#   def __init__(self, name):
#     self.name = name
#     GameObject.objects[self.class_name] = self

#   def get_desc(self):
#     return self.class_name + "\n" + self.desc

# class Goblin(GameObject):
#   class_name = "goblin"
#   desc = "A foul creature"

# goblin = Goblin("Gobbly")

# def examine(noun):
#   if noun in GameObject.objects:
#     return GameObject.objects[noun].get_desc()
#   else:
#     return "There is no {} here.".format(noun)
# verb_dict = {
#   "say": say,
#   "examine": examine,
# }

# class GameObject:
#     class_name = ""
#     desc = ""
#     objects = {}
 
#     def __init__(self, name):
#         self.name = name
#         GameObject.objects[self.class_name] = self
 
#     def get_desc(self):
#         return self.class_name + "\n" + self.desc
 
 
# class Goblin(GameObject):
#     def __init__(self, name):
#         self.class_name = "goblin"
#         self.health = 3
#         self._desc = "A foul creature"
#         super().__init__(name)
 
#     @property
#     def desc(self):
#         if self.health >= 3:
#             return self._desc
#         elif self.health == 2:
#             health_line = "It has a wound on its knee."
#         elif self.health == 1:
#             health_line = "Its left arm has been cut off!"
#         elif self.health <= 0:
#             health_line = "It is dead."
#         return self._desc + "\n" + health_line
 
#     @desc.setter
#     def desc(self, value):
#         self._desc = value
 
 
# goblin = Goblin("Gobbly")
 
 
# def hit(noun):
#     if noun in GameObject.objects:
#         thing = GameObject.objects[noun]
#         if type(thing) == Goblin:
#             thing.health -= 1
#             if thing.health <= 0:
#                 msg = "You killed the goblin!"
#             else:
#                 msg = "You hit the {}".format(thing.class_name)
#     else:
#         msg = "There is no {} here.".format(noun)
#     return msg
 
 
# def examine(noun):
#     if noun in GameObject.objects:
#         return GameObject.objects[noun].get_desc()
#     else:
#         return "There is no {} here.".format(noun)
 
 
# def get_input():
#     command = input(": ").split()
#     verb_word = command[0]
#     if verb_word in verb_dict:
#         verb = verb_dict[verb_word]
#     else:
#         print("Unknown verb {}".format(verb_word))
#         return
 
#     if len(command) >= 2:
#         noun_word = command[1]
#         print(verb(noun_word))
#     else:
#         print(verb("nothing"))
 
 
# def say(noun):
#     return 'You said "{}"'.format(noun)
 
 
# verb_dict = {
#     "say": say,
#     "examine": examine,
#     "hit": hit
# }
 
# while True:
#     get_input()

# class Test:
#     __egg = 7
# t = Test()
# print(t._Test__egg)

# class Juice:
#     def __init__(self, name, capacity):
#         self.name = name
#         self.capacity = capacity

#     def __str__(self):
#         return (self.name + ' ('+str(self.capacity)+'L)')

#     def __add__(self, other):
#         new_name = self.name + "&" + other.name
#         new_capacity = self.capacity + other.capacity
#         return(Juice(new_name, new_capacity))


# a = Juice('Orange', 1.5)
# b = Juice('Apple', 2.0)

# result = a + b
# print(result)

# import re

#your code goes here
# str=str(input())
# str="0015367001100"
# pattern=r"00"
# if re.match(pattern, str):
#     new_str= re.sub(pattern, r"+", str, 1)
#     print(new_str)
# else:
#     print(str)
# print(new_str)
    
# import re

# word = "mine"
#your code goes here
# pat=r"^m..e$"
# if re.match(pat, word):
#     print("Match")
# else:
#     print("No match")


# import re
# Id = "428888424242"
# ip = '199.206.231.11'
# tel = "93457634"
# pattern = r"\A(1|8|9)\d{7}$"

# regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
# pat = r"([0-9]{1,3}\.){3}[0-9]{1,3}"
#your code goes here
# pattern=r"(42)+"

# if re.match(regex, ip):
#     print(ip)
# else:
#     print("Wrong format")


# import re
# password = "WRTBNaeiouDFGTM"
#your code goes here
# pattern=r"(?=.*[A-Z])(?=.*\d).+"
# pattern=r"1(23)(4(56)78)9(0)?"

# match=re.match(pattern, "1234567891011") 
# if match:
#    print(match.group())
#    print(match.group(0))
#    print(match.group(1))
#    print(match.group(2))
#    print(match.group(3))
#    print(match.group(4))
#    print(match.groups())

#    print('\n'.join(re.findall(r"#\w+", text)))
# num = [1,4,12, -3, 2, 111]
# print(max(num))
# print(sorted(num))

# import re

# pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\+{4}])"
# pattern = r"(4{5,6})\1"
# str = "456 44444 444444 44444444444 444444444444 "

# match = re.findall(pattern, str)
# if match:
#     print(match)

# a, b, c, d, *e, f, g = range(20)
# print(len(e))

# a = 7
# b = 1 if a >= 15 else 42
# print(b)

# balance = 2000
# to_cash = 500
# balance = int(input())
# to_cash = int(input())

#change the code
# money_left = balance-to_cash if (to_cash<=balance and to_cash > 500)else "Error"

# print(money_left)

# ages = []
# i = 0
# while i<3:
#    age = int(input())
#    if age >= 16:
#       ages.append(age)
#       i+=1
#    else:
#       print("Too young!")
#       break
# else:
#    print("Get ready!")

# for i in range(10):
#   if i > 5:
#     print(i)
#     break
#   else:
#     print("7")

# try:
#   print(1)
#   print(1 + "1" == 2)
#   print(2)
# except TypeError:
#   print(3)
# else:
#   print(4)

def function():
   print("This is a module function")

if __name__=="__main__":
   print("This is a script")   
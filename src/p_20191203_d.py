# str_1 = str(123)
# chr_1 = chr(13)
# ord_1 = ord(chr_1)
# # print(str_1, chr_1, ord_1)
# print(chr_1)

# for s in str_1:
#     print(s)

# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a,b,a+b))
# print('%d - %d = %d' % (a, b, a - b))

# a = 10
# a *= a + 2
# print(a)

# f = float(input('input F:'))
# c = (f-32)/1.8
# # print('output C:', c)
# print('%.1fF = %.1fC' % (f, c))

# print('%d is aaaa ooo %.2f and bla %d' %(10,10,10))

# import math

# r = float(input('radius:'))
# area = math.pi*r**2
# perimeter = math.pi*2*r

# print('area: %.2f, perimeter: %.2f' % (area,perimeter))

# print('hello','world', sep=',', end='!')

# str1 = 'hello, world!'
# str2 = '-\u9a86\u660a'
# str3 = str1.title() + ' ' + str2.lower()
# print(str3)

# sum = 0
# for i in range(1,100,2):
#     sum += i
# print('sum: %d' % (sum))

# import random

# num = int(random.randrange(1,100))
# guess = int(input('please enter an integer:'))
# while guess != num:
#     if guess > num:
#         print('too big!')
#     elif guess < num:
#         print('too small!')
#     guess = int(input('please enter an integer:'))

# print('bingo!')

# answer = random.randint(1,100)
# counter = 0
# while True:
#     counter +=1
#     number = int(input('please enter an integer:'))
#     if number > answer:
#         print('too big!')
#     elif number < answer:
#         print('too small!')
#     elif number == answer:
#         print('bingo!')
#         break

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()

# num = int(input('please enter an integer: '))
# flag = True
# for i in range(2,(num-1)):
#     if num % i == 0:
#         flag = False
#         print('it is not a prime number' )
#         break
# if flag:
#     print('it is a prime number' )

# str1 = '*'
# str2 = ' '
# for i in range(1,6):
#     k = 6-i
#     str_n = str1*i + str2*k
#     print(str_n)

# class A(object):
#     def __method(self):
#         print('I am a method in A')
#     def method(self):
#         self.__method()

# a = A()
# # a.method()

# class B(A):
#     def __method(self):
#         print('B')

# b = B()
# b.method()

# name ='igor'
# print(name.__len__())

# for _ in range(5):
#     print ('_ is just a temporary varable name')

# class Test22():
#     def __init__(self):
#         self.__test__ = 22

# print(Test22().__test__)

# class Test(object):
#     def __init__(self):
#         self.foo = 11
#         self._bar = 23
#         self.__baz = 23
#         self.testPrint = 'test'

# t = Test()
# # print(dir(t))
# print(t.__baz)
# class ExtendedTest(Test):
#     # pass
#     def __init__(self):
#         super().__init__()
#         self.foo = 'overridden'
#         self._bar = 'overridden'
#         self.__baz = 'overridden'

# t2 = ExtendedTest()
# print(t2.testPrint)

# class A:
#     def add(self,x):
#         print(x+1)

# class B(A):
#     def add(self,x):
#         super().add(x)

# b = B()
# print(b.add(2))

# class FooParent(object):
#     def __init__(self):
#         self.parent = 'I am the parent'
#         print('parent')
    
#     def bar(self, message, a):
#         print('%s %s from Parent' % (message,a))

# class FooChild(FooParent):
#     def __init__(self):
#         # super().__init__()
#         print('Child')
#         # self.parent = 'overridden'

#     def bar(self, message, a):
#         # super().bar(message, a)
#         print('Child bar function')
#         print(self.parent)

# # f = FooParent()
# # f.bar('HelloWorld','Hi')
# f = FooChild()
# # f.bar('HelloWorld', 'Hi')
# print(f.parent)
# f.bar('add')

# class Bird:
#     def __init__(self):
#           self.hungry = True
#     # def eat(self):
#     #       if self.hungry:
#     #            print('Ahahahah')
#     #       else:
#     #            print('No thanks!')

# class SongBird(Bird):
#      def __init__(self):
#         super().__init__() 
#         self.sound = 'Squawk'
#      def sing(self):
#         print(self.sound)

# sb = SongBird()
# sb.sing() 
# print(sb.hungry)   

# class A():
#     def __init__(self):
#         print('enter A')
#         print('leave A')

# class B(A):
#     def __init__(self): 
#         print('enter B')
#         super().__init__()
#         print('leave B')

# class C(A):
#     def __init__(self):
#         print('enter C')
#         super().__init__()
#         print('leave C')

# class D(B,C):
#     def __init__(self):
#         print('enter D')
#         super().__init__()
#         print('leave D')

# d = D()

# row = 5
# for i in range(row):
#     for _ in range(i+1):
#         print('*', end='')
#     print()

# row = 5
# for i in range(row):
#     for _ in range(5-i):
#         print(' ', end='')
#     print('*'*(i+1))

# for num in range(500):
#     str_num = str(num)
#     sum = 0
#     for n in str_num:
#         sum += int(n)**3
#     if sum == num: 
#         print(sum)
 
# num = 123
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
#     print(num)
# # print(reversed_num)


# def Sum(a,b,c):
#     return a*5+b*3+c/3
# nums = []
# for a in range(1,int(100/5)):
#     for b in range(1,int((100-a*5)/3)):
#         c = 100-a-b
#         if Sum(a,b,c) ==  100:
#             nums.append([a,b,c])
#             break
# for num in nums:        
#     print('the numbers are %d, %d, %d' %(num[0],num[1],num[2]))

# nums = [1]
# num = 1
# for i in range(20):
#     nums.append(num)
#     num += nums[i]
# print(nums)

# a = 0
# b = 1
# for _ in range(20):
#     a,b = b, a+b
#     print (a)

# num = int(input('please enter a integer: '))
# temp = num
# num2 = 0
# while temp > 0:
#     num2 *= 10
#     num2 += temp%10
#     temp //=10
# print(num,num2)

# def test_args(first, *args):
#    print ('Required argument: ', first)
#    for v in args:
#       print ('Optional argument: ', v)

# test_args(1,2,3,4)
# def test_kwargs(first, *args, **kwargs):
#     print ('Required argument: ', first)
#     for v in args:
#         print ('Optional argument (*args): ', v)
# #    for k, v in kwargs.items():
# #       print ('Optional argument %s (*kwargs): %s' % (k, v))
#     print (kwargs.items())

# test_kwargs(1, 2, 3, 4, k1=5, k2=6)

# def test_args(first, second, third, fourth, fifth):
#     print ('First argument: ', first)
#     print ('Second argument: ', second)
#     print ('Third argument: ', third)
#     print ('Fourth argument: ', fourth)
#     print ('Fifth argument: ', fifth)

# # args = [1, 2, 3, 4, 5]
# # print(*args)
# # test_args(*args)

# kwargs = {
#     'first': 1,
#     'second': 2,
#     'third': 3,
#     'fourth': 4,
#     'fifth': 5
# }

# test_args(**kwargs)
# print(kwargs.items())
# print(**kwargs)

# def foo():
#     b = 'hello'

#     # Python中可以在函数内部再定义函数
#     def bar():
#         c = True
#         print(a)
#         print(b)
#         print(c)

#     bar()
#     # print(c)  # NameError: name 'c' is not defined


# if __name__ == '__main__':
#     a = 100
#     # print(b)  # NameError: name 'b' is not defined
#     foo()

# def foo():
#     a = 200
#     print(a)  # 200


# if __name__ == '__main__':
#     a = 100
#     foo()
#     print(a)  # 100

# def foo():
#     global a
#     a = 200
#     print(a)  # 200


# if __name__ == '__main__':
#     a = 100
#     foo()
#     print(a)  # 200

# s1 = 'hello, world!'
# s2 = "hello, world!"
# # 以三个双引号或单引号开头的字符串可以折行
# s3 = """
# hello, 
# world!
# """
# print(s1, s2, s3, end='')

# s1 = '\'hello, world!\''
# s2 = '\n\\hello, world!\\\n'
# print(s1, s2, end='')

# s1 = '\141\142\143\x61\x62\x63'
# s2 = '\u9a86\u660a'
# print(s1, s2)

# s1 = r'\'hello, world!\''
# s2 = r'\n\\hello, world!\\\n'
# print(s1, s2, end='')

# s1 = 'abcde'
# # print('ac' in s1)
# # print(s1[::-1])
# print(s1.center(50, '*'))

# a, b = 5, 10
# print('{0} * {1} = {2}'.format(a, b, a * b))

# a, b = 5, 10
# print(f'{a} * {b} = {a * b}')

# stock ='tsmc'
# close = 201
# print(f'{stock} price: {close}')

# f = [x+y for x in 'abcd' for y in '123456']
# print(f)
# import sys

# f = [x ** 2 for x in range(1, 1000)]
# print(sys.getsizeof(f))  # 查看对象占用内存的字节数
# print(f)

# f = (x ** 2 for x in range(1, 1000))
# print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
# print(f)
# for val in f:
#     print(val)

# f = {x ** 2 for x in range(1, 1000)}
# print(sys.getsizeof(f))
# print(f)

# def fib(n):
#     a, b = 0,1
#     for _ in range(n):
#         a,b = b, a+b
#         yield a

# # def main():
# #     for val in fib(20):
# #         print(val)

# # if __name__ == "__main__":
# #     main()

# print(list(fib(10)))

# list1 = [1,2,3,4,5]
# tuple1 = tuple(list1) 
# print(tuple1)
# list2 = list(tuple1)
# print(list2)

# set1 = set([1,2,3])
# print(set1)

# items1 = dict(one=1, two=2, three=3, four=4)
# # 通过zip函数将两个序列压成字典
# items2 = dict(zip(['a', 'b', 'c'], '123'))
# # 创建字典的推导式语法
# items3 = {num: num ** 2 for num in range(1, 10)}
# print(items1, items2, items3)
# # # print(zip(['a', 'b', 'c'], '123'))

# items4 = dict([('a',1),('b',2),('c',3)])
# # print(items4)
# items4.update(a=20)
# # for key in items4:
# #     print(f'{key}: {items4[key]}')

# # print(items4.popitem())

# import os
# import time

# def main():
#     content = 'constant output'
#     while True:
#         os.system('cls')
#         print(content)
#         time.sleep(0.2)
#         content = content[1:] + content[0]

# if __name__ =='__main__':
#     main()

# import random
# def generate_code(code_len=4):
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0,(len(all_chars)-1))
#         char = all_chars[index]
#         code += char
#     # code = code[1:] dode[::2]
#     return code, len(code)
# print(generate_code(4))

# filename = 'abcd.obj'
# pos = filename.rfind('.')
# print(filename[pos:])

# def is_leap_year(year):

#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

# def which_day(year, month, day):
#     days_in_month = [31,29,31,40,31,30,31,31,30,31,30,31]
#     if is_leap_year(year):
#         days_in_month[1]=28
#     days = 0
#     for i in range(month):
#         days += days_in_month[i]
#     days += day
#     return days
# print(which_day(2000,6,5))

# class Test:

#     def __init__(self, foo):
#         self.__foo = foo

#     def __bar(self):
#         print(self.__foo)
#         print('__bar')


# def main():
#     test = Test('hello')
#     test._Test__bar()
#     print(test._Test__foo)


# if __name__ == "__main__":
#     main()

# from time import sleep, time, localtime
# import os

# class Clock(object):
#     """数字时钟"""

#     def __init__(self, hour=0, minute=0, second=0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second

#     @classmethod
#     def now(cls):
#         ctime = localtime(time())
#         return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

#     def run(self):
#         """走字"""
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0

#     def show(self):
#         """显示时间"""
#         return '%02d:%02d:%02d' % \
#                (self._hour, self._minute, self._second)

# def main():
#     clock = Clock.now()
#     while True:
#         # os.system('cls')
#         clock.run()
#         sleep(1)
#         print(clock.show())

# if __name__ == '__main__':
#     main()


# class Student(object):
#     def __init__(self,test):
#         self._score = test

#     @property
#     def score(self):
#         return self._score
    
#     @score.setter
#     def score(self,value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value


# s = Student(10)
# s.score = 60
# print(s.score)

# class Person(object):
#     def __init__(self,name,age):
#         self._name = name
#         self._age = age
    
#     @property
#     def name(self):
#         return self._name
    
#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self,age):
#         self._age = age
    
#     def play(self):
#         if self._age <= 16:
#             print('%s<=16' % self._name)
#         else:
#             print('%s>16' % self._name)
    
# def main():
#     person = Person('A',14)
#     person.play()
#     person.age = 22
#     person.play()

# if __name__ =='__main__':
#     main()


# class Person(object):

#     # 限定Person对象只能绑定_name, _age和_gender属性
#     __slots__ = ('_name', '_age', '_gender', '_is_gay')

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, age):
#         self._age = age

#     def play(self):
#         if self._age <= 16:
#             print('%s正在玩飞行棋.' % self._name)
#               print ( "he is {}".format())
#               print (f'{asdoi}= ,  {sdf}')
#         else:
#             print('%s正在玩斗地主.' % self._name)


# def main():
#     person = Person('王大锤', 22)
#     person.play()
#     person._gender = '男'
#     print(person._gender)
#     person._is_gay = 'yes'
#     print(person._is_gay)

# if __name__ == '__main__':
#     main()

# @staticmethod
# @classmethod

# class Person(object):
#     __slots__ = ('_name','_age','_gender','_is_gay' )

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     @property
#     def name(self):
#         return self._name
    
#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self,value):
#         self._age = value

#     def play(self):
#         if self._age <=16:
#             print('%s is watching TV' % self._name)
#         else:
#             print('%s is reading' % self._name)

# class Student(Person):
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self._grade = grade
    
#     @property
#     def grade(self):
#         return self._grade

#     @grade.setter
#     def grade(self, value):
#         self._grade = value

#     def study(self,course):
#         print('%s from %s is studying %s'% (self._name, self._grade, course))

# class Teacher(Person):
#     def __init__(self, name, age, title):
#         super().__init__(name, age)
#         self._title = title
    
#     @property
#     def title(self):
#         return self._title

#     @title.setter
#     def title(self, value):
#         self._title = value

#     def teach(self, course):
#         print('%s %s is teaching %s' % (self._title, self._name, course))



# def main():
#     person = Person('Ab', 15)
#     person._is_gay = True
#     print(person._is_gay)
#     # person.play()
#     # person.age = 30
#     # person.play()
#     student = Student('xiaoming',15,'9th year')
#     student.age = 20
#     student.play() 
#     student.grade = '8th year'
#     student.study('math')
#     teacher = Teacher('laozhang',30, 'Dean')
#     teacher.title = 'Master'
#     teacher.teach('art')

# if __name__ == '__main__':
#     main()

# from abc import ABCMeta, abstractclassmethod

# class Pet(object, metaclass = ABCMeta):
#     def __init__(self, nickname):
#         self._nickname = nickname

#     @abstractclassmethod
#     def make_voice(self):
#         pass

# class Dog(Pet):
#     def make_voice(self):
#         print('%s: wangwangwang' % self._nickname)

# class Cat(Pet):
#     def make_voice(self):
#         print('%s: miaomiao' % self._nickname)

# def main():
#     pets = [Dog('Boy'), Cat('Kat')]
#     for pet in pets:
#         pet.make_voice()

# if __name__ =='__main__':
#     main()

# class Person(object):
#     def __init__(self, name, gender):
#         self._name = name
#         self._gender = gender
    
#     def __str__(self):
#         return '(Person: %s, %s)' % (self._name, self._gender)
    
#     __repr__ = __str__

# p = Person('Ab','female')
# print(p)
# print(type(p))

# class Test(object):
#     __slots__ = ('a')
#     def test(self):
#         self.a = 10
#         print(self.a)

# t = Test()
# t.test()

from abc import ABCMeta, abstractmethod

class Employee(object, metaclass = ABCMeta):
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self,salary):
        pass

class Manager(Employee):
    def get_salary(self):
        return 15000

class Programmer(Employee):
    def __init__(self, name, hours=0):
        super().__init__(name)
        self._hours = hours

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, hours):
        self._hours = hours if hours > 0 else 0

    def get_salary(self):
        return self._hours*150

emps = [Manager('Mike'), Programmer('yuta'), Programmer('wen')]
for emp in emps:
    if isinstance(emp, Programmer):
        emp.hours = int(input('please input %s working hours ' % emp._name))
    print('%s salary is %s' % (emp._name, emp.get_salary()))
    


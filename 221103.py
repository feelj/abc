# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
    
# areum = Human('아무개', 40, '남자')


#클래스 안에서 출력이나 어떤 동작을 하려면 메서드(인스턴스가 필요함.)


# class Human:
#     def abc(self, name, age, sex):
#         self.name = name
#         self.name = age
#         self.name = sex

#     def aaa(self):
#         print("이름: {}, 나이: {}, 성별: {}",format(self.name))


# class Student:
#     def start(self):
#         print('안녕하세요')
#     def printname(self,name):
#         print('이름은 {0} 입니다'.format(name))

# stu = Student()
# Student.start(stu)
# stu.printname('홍길동')


# class Student:
#     schoolname = 'Korea'
#     schoolname = '한국'

# stu1 = Student()
# stu2 = Student()

# print('stu1의 주소 : {0}'.format(id(stu1)))
# print('stu2의 주소 : {0}'.format(id(stu2)))

# Student.schoolname='Seoul'
# print("\nStudnet의 학교:", Student.schoolname)
# print("\nstu1의 학교:", stu1.schoolname)
# print("\nstu2의 학교:", stu2.schoolname)

# print(areum.age)
 
# print(self)


# class gugu:
#     def abc(a):
#         a = int(input())
#         for b in range(1,10):
#             print(f'{a} * {b} = {a * b}')
# K = gugu
# gugu.abc(K)
# print(K)


class K:
    def a(x):
        if x%2 == 1:
            print("홀수")
        else:
            print("짝수")
    def b(a, b, c):
                
        print(f'{a} + {b} + {c} / 3 = {(a+b+c)/3}')

    def c():
        i = 5
        for i in range(i):
            print("*" * i)

K.a(int(input()))
a,b,c=map(int,input().split())
K.b(a, b, c)
K.c()

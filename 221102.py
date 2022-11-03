# def add():
#     a = int(input("입력하세요: "))
#     for a in range():
#         print(f'{a} * {a-1} = {a * (a-1)}')


#     if (a==1):
#         return 1
#     else:
#         return a*(a-1)

# add()


# def fibo(x,y):
#     if(x<99):
#         print(x, y, end = ' ')
#         x = x+y
#         y = y+x
#         return fibo(x,y)
#     else:
#         return 1
# fibo(int(input()),int(input()))

n = int(input())

def hanoi(n,rod1,rod3,rod2):
    if n == 1:
        print(rod1,rod3)

    else:
        hanoi(n-1,rod1,rod2,rod3)
        print(rod1,rod3)
        hanoi(n-1,rod2,rod3,rod1)

print(n**2 -2)
hanoi(n,1,3,2)
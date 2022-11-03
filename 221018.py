# a = 8
# for i in range(a):
#     print(" " * (a-i+1), end="")
#     print('*' * (i+1))


# a = 8
# for i in range(a):
#     print(" " * (a), end="")
#     print('*' * (a))


# a = 8
# for i in range(a):
#     print('*' * (i))
#     print(" " * (a+1), end="")


# a=11

# for i in range(a//2):	
    # print(' ' * (a//2-i), end='')
    # print('*' * (2*i+1))
    
# for i in range(a//2-1):
#     print(' ' * (i+2), end='')
#     print('*' * ((a//2*2)-3-2*i))


# for i in range(a-1):
#     print(' ' * (a-i+2), end='')
#     print('*' * ((a)-i))


# a = [[10,20],[30,40],[50,60]]
# for i in a:
#     for j in i:
#         print(j, end='')
#         print()

#int(input('입력하세요'))
for sum in range(1,10):
    for k in range(2,10):
      print(f'{k} * {sum} = {k * sum : 2d} ')
    print()


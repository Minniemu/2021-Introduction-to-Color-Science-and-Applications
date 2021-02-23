import math
def factorial_me(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

def comb_1(n,m):
    return math.factorial(n)//(math.factorial(n-m)*math.factorial(m))

def comb_2(n,m):
    return factorial_me(n)//(factorial_me(n-m)*factorial_me(m))

n = input("Please input n = ")
print(f'n = {n}') 
k = input("Please input k = ")
print(f'k = {k}')
m = input("Please input m = ")
print(f'm = {m}')
print(type(n))
combine = comb_1(n,k)


print(comb_1(n,k))
print(type(comb_1(6,5)))
print(type(1))





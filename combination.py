
def factorial_me(n):
    result = 1
    for i in range(2, n + 1):
        result = result*i
    return result
def comb(n,m):
    return factorial_me(n)//(factorial_me(n-m)*factorial_me(m))
bool = True
while bool:
    n = input("Please input n = ")
    n = int(n)
    print(f'n = {n}')

    k = input("Please input k = ")
    k = int(k)
    print(f'k = {k}')
    #防呆
    if k > n :
        bool= True
        print("INPUT ERROR! n should be greater or equal to k! ")
        continue


    m = input("Please input m = ")
    m = int(m)
    print(f'm = {m}')
    combine = comb(n,k)
    #防呆
    if m > combine-1:
        bool = True
        print("INPUT ERROR! m should be smaller or equal to combination of n and k! ")
    else :
        bool = False

print("Out of loop")







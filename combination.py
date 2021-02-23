
def factorial_me(n):
    result = 1
    for i in range(2, n + 1):
        result = result*i
    return result
def comb_2(n,m):
    return factorial_me(n)//(factorial_me(n-m)*factorial_me(m))
bool = True
while bool:
    n = input("Please input n = ")
    n = int(n)
    print(f'n = {n}')

    k = input("Please input k = ")
    k = int(k)
    print(f'k = {k}')

    m = input("Please input m = ")
    m = int(m)
    print(f'm = {m}')


    combine = comb_2(n,k)
    print(combine)
    if k > n or m > combine-1:
        bool = True
    else :
        bool = False

print("Out of loop")







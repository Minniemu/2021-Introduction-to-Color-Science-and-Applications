def factorial_me(n):
    result = 1
    for i in range(2, n + 1):
        result = result*i
    return result
def comb(n,m):
    if n<m:
        return 0
    else :
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
    if k > n or n>81:
        bool= True
        print("INPUT ERROR! 1<=n<=81 and 1<=k<=n ! ")
        continue


    m = input("Please input m = ")
    m = int(m)
    print(f'm = {m}')
    combine = comb(n,k)
    #防呆
    if m > combine-1:
        bool = True
        print("INPUT ERROR! 0<=m<=C(n, k)-1 ! ")
    else :
        bool = False

print('(n,k,m) = (%d,%d,%d)'%(n,k,m)) 
R = m
cobidic = []
temp = []
indexs = []

s = n
for i in range(1,k+1):
   ''' print("R = ",R)'''
    for j in range(s-1,k-i-1,-1):
        value = comb(j,k-i+1)
        #print("value = ",value) 
        if value <= R:
            '''print("value = ",value) 
                                                print("j = ",j)'''
            cobidic.append(j)
            R = R-value
            s = j
            break


print("cobidic = ",cobidic)
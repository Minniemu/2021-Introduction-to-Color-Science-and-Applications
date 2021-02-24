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
for i in range(n-1,k,-1): 
    value = comb(i,k)
    if value <= R:
        temp.append(value)
        indexs.append(i)
max_value = max(temp)
max_index = temp.index(max_value)
cobidic.append(indexs[max_index])
R = R - max_value
r = 2
sk = indexs[max_index]
print("R = ",R)
for i in range(0,k):
    s = n-1
    for j in range(s-1,k-r-1,-1):
        temp.cl






'''while R != 0  and r <= k:
    temp.clear()
    indexs.clear()
    for i in range(sk-1,k-r-1,-1):
        value = comb(i,r)
        if value <= R:
            temp.append(value)
            indexs.append(i)
    #print(temp)
    #print(indexs)
    max_value = max(temp)
    max_index = temp.index(max(temp))
    cobidic.append(indexs[max_index])
    sk = indexs[max_index]
    R = R - max_value
    r = r+1
    print(cobidic)
if r <= k:
    cobidic.append(0)'''
print(cobidic)
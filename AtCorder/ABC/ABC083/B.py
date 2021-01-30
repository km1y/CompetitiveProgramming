N, A, B = map(int, input().split())

res = 0
debugL = []

for i in range(1, N+1):
    L = list()
    for j in str(i):
        L.append(int(j))
    if A <= sum(L) <=B:
        res += i

print(res)

N = int(input())
L = list(map(int, input().split()))

Asum = 0
Bsum = 0

L.sort(reverse=True)

for i in range(len(L)):
    if i%2 == 0:
        Asum += L[i]
    else:
        Bsum += L[i]

print(Asum - Bsum)

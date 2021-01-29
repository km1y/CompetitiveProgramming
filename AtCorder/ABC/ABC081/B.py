N = int(input())
L = list(map(int, input().split()))

cnt = 0

while all(num % 2 == 0 for num in L):
    L = list(num/2 for num in L)
    cnt += 1

print(cnt)

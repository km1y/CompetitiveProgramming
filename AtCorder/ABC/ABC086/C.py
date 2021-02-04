N = int(input())

t, x,y = 0, 0, 0

res = "Yes"

for i in range(N):
    T, X, Y = map(int, input().split())
    if abs(X-x) + abs(Y-y) > T-t or (abs(X-x)+abs(Y-y)+T-t)%2==1:
        res ="No"
    t, x, y = T, X, Y

print(res)

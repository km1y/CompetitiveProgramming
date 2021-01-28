num = list(map(int, input().split()))
re = num[0] * num[1] % 2

if re == 0:
    print("Even")
else:
    print("Odd")
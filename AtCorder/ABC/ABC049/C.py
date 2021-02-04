S = input()

L = ["eraser", "erase" , "dreamer", "dream"]

for l in L:
    S = S.replace(l, "")

if S == "":
    print("YES")
else:
    print("NO")

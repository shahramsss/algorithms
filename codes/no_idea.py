N = input().split()
M = input().split()
A = input().split()
B = input().split()


happiness = 0

for i in M:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1

print(happiness)

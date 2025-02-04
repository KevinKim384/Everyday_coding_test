import sys

a = int(sys.stdin.readline().rstrip())
for _ in range(a):
    b, c = map(int, sys.stdin.readline().rsplit())
    print(b + c)

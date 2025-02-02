a,b,c = map(int, input().split())
list = [a,b,c]
if a == b == c:
    print(a*1000 + 10000)
elif a == b or a == c or c == b:
    if a == b:
        print(a*100 + 1000)
    elif b == c:
        print(b*100 + 1000)
    else:
        print(a*100 + 1000)
else:
    print(max(list)*100)
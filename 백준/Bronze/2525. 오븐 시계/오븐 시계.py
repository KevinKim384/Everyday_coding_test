h, m = map(int, input().split())
cm = int(input())
total = h * 60 + m + cm 
total %= 1440  
print(total // 60, total % 60) 
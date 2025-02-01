#a, b = map(str, input().split())
#a = int(a) 
#digits = [int(digit) for digit in b] 

#for x in digits[::-1]:
#    print(a * x)
#print(a * int(b))
#코렙에는 정상적으로 나오는데 여긴 왜 ValueError라고 뜨는거여? 어이가 없네 ㅋㅋㅋㅋ
#a, b = map(int, input().split()) 이것도 안되네 ㅋㅋㅋㅋㅋㅋ 여기 뭐요?
a = int(input())
b = int(input())
print(a * (b%10))
print(a * (b%100 // 10))
print(a* (b//100))
print(a * b)
total_money = int(input())
total_cost = 0
total_count = int(input())

for _ in range(total_count):
    cost, num = map(int, input().split())
    total_cost += (cost*num)
print("Yes" if total_money == total_cost else "No")
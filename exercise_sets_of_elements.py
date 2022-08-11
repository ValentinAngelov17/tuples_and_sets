length = input().split(" ")
m, n = int(length[0]), int(length[1])
set_number_1 = set()
set_number_2 = set()

for a in range(m):
    number = int(input())
    set_number_1.add(number)

for b in range(n):
    numbers = int(input())
    set_number_2.add(numbers)

answer = set_number_1 & set_number_2
for j in answer:
    print(j)
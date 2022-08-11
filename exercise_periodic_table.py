lines = int(input())
chemical_set = set()

for _ in range(lines):
    chemical = input().split(' ')
    for n in range(len(chemical)):
        chemical_set.add(chemical[n])

for j in chemical_set:
    print(j)
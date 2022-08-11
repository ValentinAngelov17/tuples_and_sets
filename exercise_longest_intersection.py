lines = int(input())
first_set = set()
second_set = set()
intersect = ''
temp = int()
temp2 = set()

for i in range(lines):
    command = input().split(",")
    first_number_start = int(command[0])
    mid_range = command[1].split('-')
    first_number_end = int(mid_range[0])
    for k in range(first_number_start, first_number_end +1):
        first_set.add(k)

    second_number_start = int(mid_range[1])
    second_number_end = int(command[2])
    for j in range(second_number_start, second_number_end +1):
        second_set.add(j)
    intersect = first_set & second_set
    if len(intersect) > len(temp2):
        temp2 = intersect
    if len(intersect) > temp:
        temp = len(intersect)

    first_set = set()
    second_set = set()
temp3 = []
for t in temp2:
    temp3.append(t)
print(f"Longest intersection is {temp3} with length {temp}")
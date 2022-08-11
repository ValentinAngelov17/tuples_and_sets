number_tuple = (input().split(' '))
number_dict = {}
for number in number_tuple:
    a = number_tuple.count(number)
    number_dict[number] = a
for numbers, count in number_dict.items():
    print(f'{float(numbers):.1f} - {count} times')

n = int(input())
car_parking = set()
for i in range(n):
    direction, car_number = input().split(', ')
    if direction == "IN":
        car_parking.add(car_number)
    else:
        car_parking.remove(car_number)
if car_parking:
    for car in car_parking:
        print(car)
else:
    print('Parking Lot is Empty')
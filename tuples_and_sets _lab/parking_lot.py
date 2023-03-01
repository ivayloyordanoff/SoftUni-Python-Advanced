car_number_records = [input() for _ in range(int(input()))]
parking_lot = set()
COMMAND_IN = "IN"
COMMAND_OUT = "OUT"

for record in car_number_records:
    command, car_number = record.split(", ")

    if command == COMMAND_IN:
        parking_lot.add(car_number)

    elif command == COMMAND_OUT:
        parking_lot.remove(car_number)

if parking_lot:
    for car_number in parking_lot:
        print(car_number)
else:
    print("Parking Lot is Empty")

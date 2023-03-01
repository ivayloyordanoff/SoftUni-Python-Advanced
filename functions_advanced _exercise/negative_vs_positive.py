def negative():
    sum_of_negative = sum([num for num in numbers if num < 0])

    return sum_of_negative


def positive():
    sum_of_positive = sum([num for num in numbers if num > 0])

    return sum_of_positive


def print_func():
    print(negative())
    print(positive())

    if abs(negative()) > positive():
        print("The negatives are stronger than the positives")
    elif positive() > abs(negative()):
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]

print_func()

def rectangle(length, width):
    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    if type(length) != int or type(width) != int:
        return "Enter valid values!"

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"

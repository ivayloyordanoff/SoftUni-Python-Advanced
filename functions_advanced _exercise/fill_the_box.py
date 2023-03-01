def fill_the_box(height, length, width, *args):
    size = height * length * width
    cubes = 0

    for arg in args:
        if arg == "Finish":
            break
        cubes += arg

    if size > cubes:
        return f"There is free space in the box. You could put {size - cubes} more cubes."
    else:
        return f"No more free space! You have {abs(cubes - size)} more cubes."

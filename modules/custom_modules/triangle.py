def print_triangle(size):
    for row in range(1, size + 2):
        print(*[col for col in range(1, row)])

    for row in range(size, 0, - 1):
        print(*[col for col in range(1, row)])


# # 2 version
# def print_triangle(size):
#     triangle = ""
#
#     for n in range(1, size + 1):
#         for i in range(1, n + 1):
#             triangle += f"{i} "
#         triangle += "\n"
#
#     for n in range(size, 0, - 1):
#         for i in range(1, n):
#             triangle += f"{i} "
#         triangle += "\n"
#
#     print(triangle)

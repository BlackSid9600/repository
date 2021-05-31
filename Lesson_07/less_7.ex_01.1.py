class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''


    def __str__(self):
        return '\n'.join(map(str, self.my_list))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.my_list]))




m = Matrix([[11, 5, 3, 6, -2], [-11, 8, 1, -4, 5], [-8, 2, -3, 0, 5], [1, 8, -1, 2, -5]])
new_m = Matrix([[-5, 0, 6, 0, 7], [8, 0, 2, 8, 5], [-8, 2, -2, 5, 4], [2, 5, -7, 1, 20]])
print(m)
# print(m.__str__(new_m))
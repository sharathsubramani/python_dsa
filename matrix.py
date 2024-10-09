# class TwodArray():
#     def __init__(self) -> None:
#         pass

#     def initialize_array():


def insert_elements(name):
    name = name
    size = len(name)
    matrix = [['0' for i in range(size)]for j in range(size)]
    for i in range(size):
        matrix[0][i] = name[i]
        print(name[i])
    for i in range(size):
        matrix[i][0] = name[i]
    for i in range(size):
        matrix[i][i] = name[i]
    for row in matrix:
        print(row)


insert_elements('sharath')


# sample output
# ['s', 'h', 'a', 'r', 'a', 't', 'h]
# ['h', 'h', '0', '0', '0', '0', '0']
# ['a', '0', 'a', '0', '0', '0', '0']
# ['r', '0', '0', 'r', '0', '0', '0']
# ['a', '0', '0', '0', 'a', '0', '0']
# ['t', '0', '0', '0', '0', 't', '0']
# ['h', '0', '0', '0', '0', '0', 'h']

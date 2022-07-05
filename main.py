import random
import sys

from MyQueue import MyQueue
from Stack import Stack

# region Question1
MAX_SIZE = 20
MIN_MAX_VALUE = 1000
DATA_STRUCTURE_TYPES = ["Queue", "Stack"]

"""
the param data_structure_type need to be Queue OR Stack 
"""


def exampleQ1(data_structure_type):
    if data_structure_type.upper() == 'QUEUE':
        data_structure = MyQueue()
    elif data_structure_type.upper() == 'STACK':
        data_structure = Stack()
    else:
        print("the data structure need to be Stack OR Queue")
        sys.exit(1)

    print(f"the data structure that chosen is {data_structure_type}.")
    size = random.randint(1, MAX_SIZE)
    print(f"the size of {data_structure_type} is: ", size)

    for i in range(size):
        current_item = random.randint(-MIN_MAX_VALUE, MIN_MAX_VALUE)
        print(f"push the value: {current_item}")
        data_structure.push(current_item)
    for i in range(size):
        val = data_structure.pop()
        print(f"pop: {val}")


# endregion


# region Question2
def check_dim(dim):
    try:
        dim_int = int(dim)
        if dim_int <= 0:
            raise Exception("dim paramter need to grater than 0")

    except ValueError:
        print("dim paramter need to bee integer")
        sys.exit(1)
    except Exception as error:
        print(error)
        sys.exit(1)


def print_matrix_by_dict(dim: int):
    check_dim(dim)
    range_len = dim ** 2
    matrix_dict = {}
    index = 1
    # init matrix
    for i in range(1, range_len, dim):
        matrix_dict[index] = list(range(i, i + dim))
        index = index + 1
    # printing matrix
    for key, value in matrix_dict.items():
        cur_val = ''.join(str(v) for v in value)
        print(f"{key}. {cur_val}")


def print_matrix_by_list(dim: int):
    check_dim(dim)
    range_len = dim ** 2
    matrix_list = []

    # init matrix
    for i in range(1, range_len, dim):
        matrix_list.append(list(range(i, i + dim)))
    # printing matrix
    for index, values in enumerate(matrix_list):
        cur_val = ''.join(str(v) for v in values)
        print(f"{index + 1}. {cur_val}")


def print_matrix_by_variables(dim: int):
    check_dim(dim)
    range_len = dim ** 2
    # printing matrix
    for index, val in enumerate(range(1, range_len, dim)):
        current = ''.join(str(v) for v in range(val, val + dim))
        print(f"{index + 1}. {current}")


def exampleQ2():
    print("print matrix by dict")
    print_matrix_by_dict(3)
    print("print matrix by list")
    print_matrix_by_list(5)
    print("print matrix by variables")
    print_matrix_by_list(4)


# endregion


if __name__ == '__main__':
    # exampleQ1(DATA_STRUCTURE_TYPES[1])
    # exampleQ1(DATA_STRUCTURE_TYPES[0])
    exampleQ1(random.choice(DATA_STRUCTURE_TYPES))
    exampleQ2()

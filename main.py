import random

from Stack import Stack

MAX_STACK_SIZE = 20
MIN_MAX_VALUE_IN_STACK = 1000


def exampleStack():
    stack_size = random.randint(1, MAX_STACK_SIZE)
    stack = Stack()
    for i in range(stack_size):
        stack.push(random.randint(-MIN_MAX_VALUE_IN_STACK, MIN_MAX_VALUE_IN_STACK))

    print("current size: ", stack.size())
    stack.pop()
    stack.pop()
    print(stack.top())
    print("current size: ", stack.size())


if __name__ == '__main__':
    exampleStack()

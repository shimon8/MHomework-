class Queue(object):
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, val):
        self.input.append(val)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if (self.output == []):
            while (self.input != []):
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []
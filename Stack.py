from queue import Queue


class Stack(object):

	def __init__(self):

		self.q1 = Queue()
		self.q2 = Queue()

		self.curr_size = 0

	def push(self, val):
		self.q1.put(val)
		self.curr_size += 1

	def pop(self):
		if (self.q1.empty()):
			return
		while(self.q1.qsize() != 1):
			self.q2.put(self.q1.get())

		self.curr_size -= 1

		self.q = self.q1
		self.q1 = self.q2
		self.q2 = self.q

	def top(self):
		if (self.q1.empty()):
			return
		while(self.q1.qsize() != 1):
			self.q2.put(self.q1.get())

		top = self.q1.queue[0]
		self.q2.put(self.q1.get())

		self.q = self.q1
		self.q1 = self.q2
		self.q2 = self.q

		return top

	def size(self):
		return self.curr_size


from ting_file_management.abstract_queue import AbstractQueue
from collections import deque
# https://docs.python.org/3/library/collections.html#deque-objects


class Queue(AbstractQueue):
    def __init__(self):
        self._queue = deque()

    def __len__(self):
        return len(self._queue)

    def enqueue(self, value):
        self._queue.append(value)

    def dequeue(self):
        return self._queue.popleft()

    def search(self, index):
        if index not in range(0, self.__len__()):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._queue[index]

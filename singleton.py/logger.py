from queue import Queue


class Logger:
    def __init__(self):
        self.__queue = Queue()
        print("logger instance is created")

    @property
    def queue(self) -> Queue:
        return self.__queue

    def __del__(self):
        print("logger instance is deleted")
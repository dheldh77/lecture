from logger import Logger


def quiz1():
    logger1 = Logger()
    logger2 = Logger()
    logger3 = Logger()
    print(logger1)
    print(logger2)
    print(logger3)

def quiz2():
    logger1 = Logger()
    logger2 = Logger()
    logger1.queue.put(1)

    if logger2.queue.empty() == False:
        print(logger2.queue.get())

if __name__ == "__main__":
    quiz1()
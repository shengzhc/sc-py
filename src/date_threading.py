import threading
import datetime


def print_date(threadName, counter):
    datefields = []
    today = datetime.date.today()
    datefields.append(today)
    print("{}[{}]: {}".format(threadName, counter, datefields[0]))


class MyThread(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadId = counter
        self.name = name
        self.counter = counter

    def run(self):
        print("\nStarting {}[{}]".format(self.name, self.counter))
        print_date(self.name, self.counter)
        print("Exiting {}[{}]\n".format(self.name, self.counter))


thread1 = MyThread("Thread", 1)
thread2 = MyThread("Thread", 2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("\nExiting the Program()!!")

import threading
import datetime

exitFlag = 0
threadLock = threading.Lock()
threads = []


def print_date(threadName, counter):
    today = datetime.date.today()
    print("{}[{}]: {}".format(threadName, counter, today))


class MyThread(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.name = name
        self.threadId = counter
        self.counter = counter

    def run(self):
        threadLock.acquire()
        print("\nStarting {}[{}]\n".format(self.name, self.counter))
        print_date(self.name, self.counter)
        print("Exiting {}[{}]".format(self.name, self.counter))
        threadLock.release()


thread1 = MyThread("Thread", 1)
thread2 = MyThread("Thread", 2)
thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()

print("\nExiting the Program!!!")

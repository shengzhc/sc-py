import _thread as thread
import time

threadId = 1


def factorial(n):
    global threadId
    rc = 0

    if n < 1:
        print("{}: {}\n".format('\nThread', threadId))
        threadId += 1
        rc = 1
    else:
        returnNumber = n * factorial(n-1)
        print("{} != {}".format(str(n), str(returnNumber)))
        rc = returnNumber

    return rc


thread.start_new_thread(factorial, (5, ))
thread.start_new_thread(factorial, (4, ))

print("Waiting for threads to return...")
time.sleep(1)

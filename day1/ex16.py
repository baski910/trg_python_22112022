import threading
import sys

class MyException(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __repr__(self):
        return self.msg


class CustomThread(threading.Thread):
    def f(self):
        name = threading.current_thread().name
        raise MyException("An error in thread "+name)

    def run(self):
        self.exc = None
        try:
            self.f()
        except Exception as e:
            self.exc = e

    def join(self):
        threading.Thread.join(self)
        if self.exc:
            raise self.exc

t = CustomThread()
t.start()
try:
    t.join()
except Exception as e:
    print(e)
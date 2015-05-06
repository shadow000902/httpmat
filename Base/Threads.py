__author__ = 'Administrator'
import threading
import  time
class base_thread(threading.Thread):
    def __init__(self, func):
        threading.Thread.__init__(self)
        self.func = func
        #print(type(self.func))
    def run(self):
        self.func




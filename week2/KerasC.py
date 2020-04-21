import tensorflow as tf
from keras import layers

class printer:
    def __init__(self,s):
        self.string=s

    def __call__(self):
        print(self.string)


s1=printer("hello")
s1()

# class Myclass(object):
#     """A simple example class"""
#     i = 12345
#     def f(self):
#         return 'hello world'
#
# x = Myclass()
#
# def __init__(self):
#     self.data = []

class complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart

x = complex(3.0,-4.5)
print("{};{}".format(x.r,x.i))


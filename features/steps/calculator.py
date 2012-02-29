# -*- coding: UTF-8 -*-

# ----------------------------------------------------------------------------
# Domain Model:
# ----------------------------------------------------------------------------
class Calculator(object):

    def __init__(self, value=0):
        self.result = value

    def reset(self):
        self.result = 0

    def add2(self, x, y):
        self.result += (x + y)
        return self.result

import numpy as np


class LowPassIIR:

    # This class is a first order IIR filter
    # To call the class LowPasssIIR, give a∈[0,1]
    # -----------y[n] = (1-a)*x[n] + a*y[n-1]-----------
    # The smaller the filter coefficient, the smoother the filter result, but the lower the sensitivity
    # The larger the filter coefficient, the higher the sensitivity, but the more unstable the filter result

    def __init__(self, a):
        self.a = self.a[i]
        self.reset()

    def reset(self):
        self.y = 0

    def filter(self,x):
        self.y = (1-self.a) * x + self.a * self.y


        return self.y

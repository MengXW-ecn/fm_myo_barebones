from collections import deque
from threading import Lock, Thread
import numpy as np
import time
import myo
#from IIRFilter import LowPassIIR



class BufferPlus(myo.DeviceListener):
    #An instance of this class constantly collects new EMG data in a queue (buffer)
    def __init__(self, buffer_len):
        self.n = buffer_len
        self.lock = Lock()
        self.mav_data_queue = deque(maxlen=self.n)
        self.y = 0
        self.a = 24/25*np.ones([8,1])

    def filter(self,x):
        self.y = (1-self.a[self.i]) * x + self.a[self.i] * self.y
        return self.y

    def get_mav_data(self,in_data):
        mav_data = []
        #num_splitarray = np.linspace(0,496,64,dtype=int) #(step = 7, num = 64)

        with self.lock:
            # compute the MAV data
            #for j in num_splitarray:
            for self.i in range(0,8):

                col_data = in_data[:,self.i]
                abs_data = np.absolute(col_data)
                
                # filter
                for n in range(0, len(abs_data)):
                    abs_data[n] = self.filter(abs_data[n])
                mav_data.append(list(abs_data))

        return mav_data

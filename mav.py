import myo
import numpy as np
import time
import keyboard
import math

from myo_ecn.listeners                   import ConnectionChecker
from myo_ecn.listeners                   import Buffer
from MultichannelPlot                    import MultichannelPlot
from myo_ecn.listenersPlus               import BufferPlus


def main():
    # ================== setup myo-python (do not change) =====================
    myo.init(sdk_path='../../myo_sdk') # Compile Python binding to Myo's API
    hub = myo.Hub() # Create a Python instance of MYO API
    if not ConnectionChecker().ok: # Check connection before starting acquisition:
        quit()
    # =========================================================================
    # calculate the Mean Absolute Value
    # Setup our custom processor of MYO's events.
    # EmgBuffer will acquire new data in a buffer (queue):
    listener = Buffer(buffer_len = 512) # At sampling rate of 200Hz, 512 samples correspond to ~2.5 seconds of the most recent data.
    computer = BufferPlus(buffer_len = 512)
    # Setup multichannel plotter for visualisation:
    plotter = MultichannelPlot(nchan = 8, xlen = 512) # Number of EMG channels in MYO armband is 8 , window size is 15 for MAV

    # Tell MYO API to satart a parallel thread that will collect the data and
    # command the MYO to start sending EMG data.
    with hub.run_in_background(listener): # This is the way to associate our listener with the MYO API.
        print('Streaming EMG ... Press shift-c to stop.')
        while hub.running:
            time.sleep(0.040)
            # Pull recent EMG data from the buffer
            emg_data = listener.get_emg_data()
            # Transform it to numpy matrix
            emg_data = np.array([x[1] for x in emg_data])

            # avoid len() report erro
            if (emg_data.ndim==2):
                if (emg_data.shape[0]==512):
                    mav_data = computer.get_mav_data(emg_data)
                    mav_data = np.array(mav_data.T)               
                    # update data
                    plotter.update_plot(np.array(mav_data))
                    
           
            
            if keyboard.is_pressed('C'):
                print('Stop.')
                break


if __name__ == '__main__':
    main()


    
    

# ---------------------
class Moving_Average(object):
    def __init__(self, length, return_int = False):
        self.data = []
        self.data_sum = -1
        #self.data_avg = -1
        self.length = length
        self.value = -1
        self.return_int = return_int

        #self.sample_frequency = sample_frequency               #in Hz
        #self.range_ = range_                                   #in seconds
        #self.scope = 1.0 * self.sample_frequency * self.range_       #in number of samples, limits the length of movingAvg    
        #self.sum_movingAvg = 0                                 #tracks the sum of the moving average
        #self.val_movingAvg = -1                                #the latest moving average value
        #self.movingAvg = []                                    #used to store the datapoints for taking a moving average

    def get_movingAvg (self, data):
        self.data.insert(0, data)
        self.data_sum += data

        if len(self.data) > self.length:
            self.data_sum -= self.data.pop()

        if self.return_int == True:
            self.value = int(self.data_sum / self.length) #preserves integer form
        else: 
            self.value = 1.0 * self.data_sum / self.length

        if len(self.data) < (self.length / 2):
            return -1
        else:
            return self.value

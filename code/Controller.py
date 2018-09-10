from CU import CU
from Weight_matrix import Weight_matrix
import numpy as np


NN_layer = 2 
filter_bit = 3
filter_h = 3
filter_w = 3

CU_num = 6
macro = 1
IO_n = 8
xbar_h = 5
xbar_w = 20
OU_h = 3
OU_w = IO_n
pooling_h = 2
pooling_w = 2

class Controller(object):
    def __init__(self):
        self.weight_mat = []
        for i in range(NN_layer):
            self.weight_mat.append(Weight_matrix(NN_layer, filter_bit, filter_h, filter_w))

        self.CU_array = []
        for i in range(CU_num):
            self.CU_array.append(CU(IO_n, self.weight_mat, macro, xbar_h, xbar_w, OU_h, OU_w, pooling_h, pooling_w))

    def run(self):
        while True:
            ###event
            ###appendTask
            break

if __name__ == '__main__':
    controller = Controller()
    controller.run()
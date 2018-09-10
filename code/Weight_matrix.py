import numpy as np

class Weight_matrix(object):
    def __init__(self, NN_layer, filter_bit,  weight_h, weight_w):
        #NN layer = 2
        self.weight_mat = []
        self.weight_mat.append(np.zeros((1*weight_h*weight_w, 2*filter_bit))) # zeros(c*w*h, n*bit)
        self.weight_mat.append(np.zeros((2*weight_h*weight_w, 1*filter_bit))) # zeros(c*w*h, n*bit)

        for i in range(weight_h):
            a = []
            for j in range(weight_w):
                a.append(j)
            self.weight_mat.append(a)
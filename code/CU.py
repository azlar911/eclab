from OnChipBuffer import OnChipBuffer
from PoolingUnit import PoolingUnit
from ActivationUnit import ActivationUnit
from Xbar import Xbar
from BitShiftAndAdd import BitShiftAndAdd
from InputShiftAndAdd import InputShiftAndAdd

class CU(object):
    def __init__(self, IO_n, weight_matrix, macro, xbar_h, xbar_w, OU_h, OU_w, pooling_h, pooling_w):
        self.onChipBuffer = OnChipBuffer()
        self.poolingUnit = PoolingUnit(pooling_h, pooling_w)
        self.activationUnit = ActivationUnit()
        self.Xbar = Xbar(xbar_h, xbar_w, OU_h, OU_w)
        self.bitShiftAndAdd = []
        for i in range(IO_n):
            self.bitShiftAndAdd.append(BitShiftAndAdd())
        self.inputShiftAndAdd = InputShiftAndAdd()

        #hardware_matrix init
        #self.hw_mat = 
        
    def CUtoCU(self):
        pass
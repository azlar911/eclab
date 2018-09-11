from OnChipBuffer import OnChipBuffer
from PoolingUnit import PoolingUnit
from ActivationUnit import ActivationUnit
from Xbar import Xbar
from WordLine import WordLine
from BitShiftAndAdd import BitShiftAndAdd
from InputShiftAndAdd import InputShiftAndAdd

class CU(object):
    def __init__(self, IO_n, weight_matrix, macro, xbar_h, xbar_w, OU_h, OU_w, pooling_h, pooling_w):
        self.onChipBuffer = OnChipBuffer()
        self.poolingUnit = PoolingUnit(pooling_h, pooling_w)
        self.activationUnit = ActivationUnit()
        self.xbar = Xbar(xbar_h, xbar_w, OU_h, OU_w)
        self.wordLine = WordLine(xbar_h)
        self.bitShiftAndAdd = []
        for i in range(IO_n):
            self.bitShiftAndAdd.append(BitShiftAndAdd())
        self.inputShiftAndAdd = InputShiftAndAdd()

        self.weight_mat = weight_matrix

        #hardware_matrix init
        #self.hw_mat = 
        
    def onChipBufferToWL(self):
        pass
        
    def OperationUnit(self):
        pass

    def bSAA(self):
        pass

    def inputSAA(self):
        pass

    def activation(self):
        pass

    def pooling(self):
        pass
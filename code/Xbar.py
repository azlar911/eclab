class Xbar(object):
    def __init__(self, xbar_h, xbar_w, OU_h, OU_w):
        self.xbar_h = xbar_h
        self.xbar_w = xbar_w
        self.OU_h = OU_h
        self.OU_w = OU_w
        self.filter = []
        for i in range(xbar_h):
            r = []
            for j in range(xbar_w):
                r.append(0)
            self.filter.append(r)
        

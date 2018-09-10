
# coding: utf-8

# In[5]:


import numpy as np


# In[12]:


#NN layer = 2 
filter_bit = 3
#layer1_filter = 1*3*3*2
#layer2_filter = 2*3*3*1

weight_mat = []
weight_mat.append(np.zeros((1*3*3, 2*filter_bit))) # zeros(c*w*h, n*bit)
weight_mat.append(np.zeros((2*3*3, 1*filter_bit))) # zeros(c*w*h, n*bit)

#print(weight_mat)


# In[ ]:


CU_num = 6
macro = 1
IO_n = 8
xbar_h = 5
xbar_w = 20
OU_h = 3
OU_w = IO_n


# In[61]:


# 87 init

hw_mat = []
for i in range(6):
    CU = []
    for j in range(5):
        L = []
        for k in range(20):
            L.append({'n_layer':0, 'n_filter':0, 'n_bit':0, 'n_value':0})
        CU.append(L)
    hw_mat.append(CU)
hw_mat = np.array(hw_mat)

CU_idx = 0
CU_idx_max = 0
for f in range(2):
    for w in range(filter_bit):
        CU_idx = 0
        for h in range(1*3*3):
            if h >= (CU_idx+1)*xbar_h:
                CU_idx += 1
                CU_idx_max = max(CU_idx_max, CU_idx)
            htmp = h - 5*(CU_idx)
            hw_mat[CU_idx][htmp][w+f*filter_bit] = {'n_layer':1, 'n_filter':f+1, 'n_bit':w+1, 'n_value':h+1}

            
CU_idx = CU_idx_max+1

for f in range(1):
    for w in range(filter_bit):
        CU_idx = CU_idx_max
        for h in range(2*3*3):
            if h >= (CU_idx-CU_idx_max)*xbar_h:
                CU_idx += 1
            htmp = h - xbar_h*(CU_idx-CU_idx_max)
            hw_mat[CU_idx][htmp][w+f*filter_bit] = {'n_layer':2, 'n_filter':f+1, 'n_bit':w+1, 'n_value':h+1}
            
            
#print(hw_mat[2:6])

#print(CU_idx_max)


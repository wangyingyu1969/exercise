import numpy as np
def jisuan(A,B):
    A=np.array(A)
    B=np.array(B)
    len_array=len(A)-len(B)+1
    C=[]
    for i in range(len_array):
        b=np.sum(A[i:i+len(B-1)]*B)
        C.append(b)
    return C


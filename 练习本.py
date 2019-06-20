import numpy as np
pic=np.random.uniform(-500,500,size=[500,500,3])
pic*=(pic>0)#将像素值低于0的置为0
#pic=pic*(pic<=255)+255*(pic>255) #将大于255的规整为255，其它不变
print(pic)

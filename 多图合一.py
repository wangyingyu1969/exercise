import matplotlib.pyplot as plt
import numpy as np
plt.figure(num='多图合一')
x=np.random.rand(4,3)
y=x**2
plt.subplot(2,1,1)
plt.plot(x,y)

plt.subplot(2,3,4)
plt.plot([0,1],[0,2])

plt.subplot(2,3,5)
plt.plot([0,1],[0,3])

plt.subplot(2,3,6)
plt.plot([0,1],[0,4])
plt.show()

# example 1:
###############################
# plt.figure(figsize=(6, 4))
# # plt.subplot(n_rows, n_cols, plot_num)
# plt.subplot(2, 2, 1)
# plt.plot([0, 1], [0, 1])
#
# plt.subplot(222)
# plt.plot([0, 1], [0, 2])
#
# plt.subplot(223)
# plt.plot([0, 1], [0, 3])
#
# plt.subplot(224)
# plt.plot([0, 1], [0, 4])
#
# plt.tight_layout()
#
# # example 2:
# ###############################
# plt.figure(figsize=(6, 4))
# # plt.subplot(n_rows, n_cols, plot_num)
# plt.subplot(2, 1, 1)
# # figure splits into 2 rows, 1 col, plot to the 1st sub-fig
# plt.plot([0, 1], [0, 1])
#
# plt.subplot(234)
# # figure splits into 2 rows, 3 col, plot to the 4th sub-fig
# plt.plot([0, 1], [0, 2])
#
# plt.subplot(235)
# # figure splits into 2 rows, 3 col, plot to the 5th sub-fig
# plt.plot([0, 1], [0, 3])
#
# plt.subplot(236)
# # figure splits into 2 rows, 3 col, plot to the 6th sub-fig
# plt.plot([0, 1], [0, 4])

import numpy as np
class Func():
    def bsplinelinear(self):
        bsplinelinear = np.array([[1 / 4, 1 / 2, 1 / 4],
                                  [2**(1 / 2) / 4, 0, -2**(1 / 2) / 4],
                                  [-1 / 4, 1 / 2, -1 / 4]])
        return bsplinelinear

    def bsplinecubic(self):
        bsplinecubic = np.array([[1 / 16, 1 / 4, 3 / 8, 1 / 4, 1 / 16],
                                 [1 / 16, -1 / 4, 3 / 8, -1 / 4, 1 / 16],
                                 [-1 / 8, 1 / 4, 0, -1 / 4, 1 / 8],
                                 [6**(1 / 2) / 16, 0, -6**(1 / 2) /
                                  8, 0, 6**(1 / 2) / 16],
                                 [-1 / 8, -1 / 4, 0, 1 / 4, 1 / 8]])
        return bsplinecubic

    def haar(self):
        haar = np.array([[1 / 2, 1 / 2],
                         [1 / 2, -1 / 2]])
        return haar

    def db2(self):
        db2 = np.array([[-0.12940952255092145, 0.22414386804185735,
                         0.836516303737469, 0.48296291314469025],
                        [-0.48296291314469025, 0.836516303737469,
                         -0.22414386804185735, -0.12940952255092145]] / np.sqrt(2))
        return db2

    def db3(self):
        db3 = np.array([[0.035226291882100656, -0.08544127388224149, -0.13501102001039084,
                         0.4598775021193313, 0.8068915093133388, 0.3326705529509569],
                        [-0.3326705529509569, 0.8068915093133388, -0.4598775021193313,
                         -0.13501102001039084, 0.08544127388224149, 0.035226291882100656]] / np.sqrt(2))
        return db3

    def gauss(self):          #平滑处理
        gauss=np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])

        return gauss
    def gauss1(self):
        gasuss1=np.array([[1/16,2/16,1/16],[2/16,4/16,2/16],[1/16,2/16,1/16]])
        return gauss1
    def gauss2(self): #图像锐化
        gauss2=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
        return gauss2
    def gauss3(self):          #水平梯度
        gauss3=np.array([[-1,0,1][-1,0,1],[-1,0,1]])
        return gauss3
    def gauss4(self):       #垂直梯度
        gauss4=np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
        return gauss4

if __name__ == '__main__':Func


#把这个文件定义成FUNC 我输入里面的矩阵名称就可使用，这些矩阵都是过滤器。明天中午给我


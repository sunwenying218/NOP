from skimage import io,transform,color
import numpy as np
import os


def convert_gray(f,**args): #图片处理与格式化的函数
    image=io.imread(f)      #读取图片
    gray=color.rgb2gray(image)  #将彩色图片转换为灰度图片
    
    return gray


if __name__ == "__main__":
    
    path = os.path.abspath('.')
    
    NegPath = path + '/OriginNegPicture'
    NegStrJPG = NegPath + '/*.jpg' 
    NegStrPNG = NegPath + '/*.png'
    NegCollJPG = io.ImageCollection(NegStrJPG, load_func=convert_gray)   #批处理
    NegCollPNG = io.ImageCollection(NegStrPNG, load_func=convert_gray)
    NegTalNum = len(NegCollJPG) + len(NegCollPNG)
    for i in range(len(NegCollJPG)):
        io.imsave(path + '/TrainNegPicture/' + np.str(i) + '.png', NegCollJPG[i])
        print('neg  ' + str(100*i/NegTalNum) + ' %')

    num = i
    for i in range(len(NegCollPNG)):
        io.imsave(path + '/TrainNegPicture/' + np.str(i + num) + '.png', NegCollPNG[i])
        print('neg  ' + str(100*(i + num)/NegTalNum) +' %')



    PosPath = path + '/OriginPosEye'
    PosStrPNG = PosPath + '/*.png'
    PosCollPNG = io.ImageCollection(PosStrPNG, load_func=convert_gray)
    PosTalNum = len(PosCollPNG)
    for i in range(len(PosCollPNG)):
        io.imsave(path + '/TrainPosEye/' + np.str(i) + '.png', PosCollPNG[i])
        print('pos1 ' + str(100*i/PosTalNum) +' %')


        


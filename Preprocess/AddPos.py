import cv2
from skimage import io
import numpy as np


if __name__ == "__main__":

    imgPath = 'D:/PythonFile/CurriculaDesign/Code/Picture/OriginPosEye'
    strJpg = imgPath + '/*.png'
    coll_str = io.ImageCollection(strJpg)
    r_size = (400, 200)

##    # 归一化大小
##    for i in range(len(coll_str)):
##        coll_change = cv2.resize(coll_str[i], r_size)
##        io.imsave(imgPath + '/jpg_' + str(i) + '.png', coll_change)


    # 翻转
    for i in range(len(coll_str)):
        v_flip = cv2.flip(coll_str[i], 1)
        io.imsave(imgPath + '/' + str(i) + 'vflip.png', v_flip)
        print('flip ' + str(i) + ' ok')

    # 调节亮度
    for i in range(len(coll_str)):
        l_clip = np.uint8(np.clip((0.85 * coll_str[i] - 15), 0, 255))  # 对比度，亮度
        h_clip = np.uint8(np.clip((1.5 * coll_str[i] + 10), 0, 255))
        io.imsave(imgPath + '/' + str(i) + 'low.png', l_clip)
        io.imsave(imgPath + '/' + str(i) + 'hight.png', h_clip)
        print('light ' + str(i) + ' ok')



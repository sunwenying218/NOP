import os

neg_txt = 'neg.txt'
pos_txt = 'pos.txt'
neg_file = open(neg_txt, 'w')
pos_file = open(pos_txt, 'w')

path = os.path.abspath('.') # 当前文件绝对路径
n_len = len(os.listdir(path + '/Picture/TrainNegPicture'))
p_len = len(os.listdir(path + '/Picture/TrainPosPicture'))
i = 0

for filename in os.listdir(path + '/Picture/TrainNegPicture'):
    i = i+1
    print('neg ' + str(100*i/n_len) + ' %')
    neg_file.write('Picture/TrainNegPicture/'+filename+'\n')
neg_file.close()

i = 0
for filename in os.listdir(path + '/Picture/TrainPosPicture'):
    i = i+1
    print('pos ' + str(100*i/p_len) + ' %')
    # 文件名，正样本个数，图像位置，尺寸
    pos_file.write('Picture/TrainPosPicture/' + filename + ' 1 0 0 158 158'+'\n')
pos_file.close()




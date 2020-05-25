import os
import argparse

parser = argparse.ArgumentParser(description='generate data list and classnum.')
parser.add_argument('--datapath', type=str)#图像所在的路径
parser.add_argument('--txtpath', type=str,default=None)#生成的txt位置
parser.add_argument('-label', type=int)
parser.add_argument('-txtname', type=str,default='imglist')
args = parser.parse_args()
if args.txtpath==None:
    args.txtpath=args.datapath

def readname():
    filePath = args.datapath #'/home/cy/ML/data/hymenoptera_data/train/bees/'
    name = os.listdir(filePath)
 #   for a in name:
 #       path=filePath+a
    return name
 
 
if __name__ == "__main__":
    name = readname()
    target=args.txtpath+args.txtname+'.txt'
    with open(target,'a') as file_handle:   # .txt可以不自己新建,代码会自动新建
        for a in name:
            data="%s%s %d" % (args.datapath,a,args.label) 
            file_handle.write(data)     # 写入
            file_handle.write('\n') 


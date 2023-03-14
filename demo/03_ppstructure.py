# -*- coding: utf8 -*-

# pp-ocrv2 paddle:latest-dev-cuda11.2-cudnn8.2-gcc82

# https://code.gitlink.org.cn/maxjhandsome/PaddleOCR/src/branch/release/2.2/ppstructure/README_ch.md
# pip3 install -U https://paddleocr.bj.bcebos.com/whl/layoutparser-0.0.0-py3-none-any.whl
import os
import cv2

from paddleocr import PPStructure, draw_structure_result,save_structure_res

dir = os.path.dirname(__file__)
resDir = os.path.join(dir, 'result/03_ppstructure')

table_engine = PPStructure(show_log=True)

save_folder = resDir
img_path = os.path.abspath('../PaddleOCR/doc/imgs/00018069.jpg')
# img_path = os.path.abspath('../PaddleOCR/doc/imgs/00015504.jpg') # 跑这个数据对齐有点不对

imgFileName = os.path.basename(img_path).split('.')[0]

img = cv2.imread(img_path)
result = table_engine(img)
save_structure_res(result, save_folder,imgFileName)

for line in result:
    line.pop('img')
    print(line)

from PIL import Image

font_path = '../PaddleOCR/doc/fonts/simfang.ttf' # PaddleOCR下提供字体包
image = Image.open(img_path).convert('RGB')
im_show = draw_structure_result(image, result,font_path=font_path)
im_show = Image.fromarray(im_show)
im_show.save(os.path.join(resDir,imgFileName, 'result.jpg'))

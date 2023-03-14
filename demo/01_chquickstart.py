# -*- coding: utf8 -*-

# pp-ocrv2 paddle:latest-dev-cuda11.2-cudnn8.2-gcc82

# https://code.gitlink.org.cn/maxjhandsome/PaddleOCR/src/branch/release/2.2/doc/doc_ch/whl.md
# 中文readme -> 中文OCR模型快速使用 -> Paddleocr Package使用说明
from paddleocr import PaddleOCR, draw_ocr

# Paddleocr目前支持中英文、英文、法语、德语、韩语、日语，可以通过修改lang参数进行切换
# 参数依次为`ch`, `en`, `french`, `german`, `korean`, `japan`。
ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
img_path = '../PaddleOCR/doc/imgs/11.jpg'
result = ocr.ocr(img_path, cls=True)
for line in result:
    print(line)

# 显示结果
from PIL import Image

image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result[0]]
txts = [line[1][0] for line in result[0]]
scores = [line[1][1] for line in result[0]]
im_show = draw_ocr(image, boxes, txts, scores, font_path='../PaddleOCR/doc/fonts/simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save('demo/result/01_chquickstart.jpg')
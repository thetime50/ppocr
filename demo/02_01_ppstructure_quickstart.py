import os
import cv2
from paddleocr import PPStructure,draw_structure_result,save_structure_res

dir = os.path.dirname(__file__)
resDir = os.path.join(dir, 'result/02_01_ppstructure_quickstart')

def dirLayoutTableFun():
    table_engine = PPStructure(show_log=True, image_orientation=True)

    save_folder = os.path.join(resDir,'dirLayoutTable')
    # img_path = os.path.abspath('../PaddleOCRv3/doc/imgs/00018069.jpg')
    img_path = os.path.abspath('../PaddleOCRv3/doc/imgs/00015504.jpg') # 跑这个数据分享反了
    imgFileName = os.path.basename(img_path).split('.')[0]

    img = cv2.imread(img_path)
    result = table_engine(img)
    save_structure_res(result, save_folder,imgFileName)

    for line in result:
        line.pop('img')
        print(line)

    from PIL import Image

    # font_path = 'doc/fonts/simfang.ttf' # PaddleOCR下提供字体包
    font_path = '../PaddleOCRv3/doc/fonts/simfang.ttf' # linux    image = Image.open(img_path).convert('RGB')
    im_show = draw_structure_result(image, result,font_path=font_path)
    im_show = Image.fromarray(im_show)
    im_show.save( os.path.join(save_folder,imgFileName,'result.jpg'))

def layoutTableFun():
    table_engine = PPStructure(show_log=True)

    save_folder = os.path.join(resDir,'layoutTable')
    # img_path = os.path.abspath('../PaddleOCRv3/doc/imgs/00018069.jpg')
    img_path = os.path.abspath('../PaddleOCRv3/doc/imgs/00015504.jpg') # 跑这个数据对齐有点不对
    imgFileName = os.path.basename(img_path).split('.')[0]

    img = cv2.imread(img_path)
    result = table_engine(img)
    save_structure_res(result, save_folder,imgFileName)

    for line in result:
        line.pop('img')
        print(line)

    from PIL import Image


    # font_path = 'doc/fonts/simfang.ttf' # PaddleOCR下提供字体包
    font_path = '../PaddleOCRv3/doc/fonts/simfang.ttf' # linux
    image = Image.open(img_path).convert('RGB')
    im_show = draw_structure_result(image, result,font_path=font_path)
    im_show = Image.fromarray(im_show)
    im_show.save(os.path.join(save_folder,imgFileName,'result.jpg'))



# 2.2.3 版面分析
def layoutFun():
    table_engine = PPStructure(table=False, ocr=False, show_log=True)

    save_folder = os.path.join(resDir,'layout')
    # img_path = os.path.abspath('../PaddleOCRv3/doc/imgs/00018069.jpg')
    img_path = os.path.abspath('../PaddleOCRv3/doc/imgs/00015504.jpg') # 跑这个数据对齐有点不对
    imgFileName = os.path.basename(img_path).split('.')[0]
    
    img = cv2.imread(img_path)
    result = table_engine(img)
    save_structure_res(result, save_folder, imgFileName)

    for line in result:
        line.pop('img')
        print(line)

    from PIL import Image
    # font_path = 'doc/fonts/simfang.ttf' # PaddleOCR下提供字体包
    font_path = '../PaddleOCRv3/doc/fonts/simfang.ttf' # linux
    image = Image.open(img_path).convert('RGB')
    im_show = draw_structure_result(image, result,font_path=font_path)
    im_show = Image.fromarray(im_show)
    im_show.save(os.path.join(save_folder,imgFileName,'result.jpg'))


# 2.2.4 表格识别
def tableFun():
    table_engine = PPStructure(layout=False, show_log=True)

    save_folder = os.path.join(resDir,'table')
    # img_path = os.path.abspath('../PaddleOCRv3/doc/imgs/00018069.jpg')
    img_path = os.path.abspath('../PaddleOCRv3/doc/imgs/00015504.jpg') # 跑这个数据对齐有点不对
    imgFileName = os.path.basename(img_path).split('.')[0]

    img = cv2.imread(img_path)
    result = table_engine(img)
    save_structure_res(result, save_folder, imgFileName)

    for line in result:
        line.pop('img')
        print(line)
        
    from PIL import Image
    # font_path = 'doc/fonts/simfang.ttf' # PaddleOCR下提供字体包
    font_path = '../PaddleOCRv3/doc/fonts/simfang.ttf' # linux
    image = Image.open(img_path).convert('RGB')
    im_show = draw_structure_result(image, result,font_path=font_path)
    im_show = Image.fromarray(im_show)
    im_show.save(os.path.join(save_folder,imgFileName,'result.jpg'))


# dirLayoutTable()
# layoutTableFun()
layoutFun()
tableFun()

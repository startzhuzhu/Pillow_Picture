import sys
from PIL import Image,ImageDraw,ImageFont

def watermark_with_text(file_obj,text,color,fontfamily=None):
    image = Image.open(file_obj).convert('RGB')
    draw = ImageDraw.Draw(image)
    width,height = image.size
    margin = 10
    if fontfamily:
        font = ImageFont.truetype(fontfamily,int(height/20))
    else:
        font = None

    textWidth,textHight = draw.textsize(text,font)
    x = (width-textWidth-margin)/2 #计算横轴位置
    y = height-textHight-margin    #计算纵轴位置
    draw.text((x,y),text,color,font)
    return image

if __name__ == '__main__':
    org_file = sys.argv[1]
    with open(org_file,'rb') as f:
        image_with_watermark = watermark_with_text(f,'dongjin.zhu','red')
    with open('new_image_water.png','wb') as f:
        image_with_watermark.save(f)
from PIL import Image
import os

def add_bene(nasPath, outputDir, file_name):
    tempNm = "temp_" + file_name
    finalNm = "proc_" + file_name

    my_image = Image.open(tempNm)  
    my_image.putalpha(255)
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "../image/bene.jpg"
    abs_file_path = os.path.join(script_dir, rel_path)
    watermark = Image.open(abs_file_path)
    watermark.putalpha(255)
    x = my_image.size[0] - watermark.size[0]
    y = my_image.size[1] - watermark.size[1]
    my_image.paste(watermark, (x,y), watermark)
    my_image.save(nasPath + outputDir + "/" + finalNm)
    os.remove(tempNm)
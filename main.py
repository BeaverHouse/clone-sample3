from openpyxl import Workbook
import sys
import json
import glob
import cv2
import os
import arrow

from step1.grayscale import make_gray
from step2.deeper.bene import add_bene

if __name__ == "__main__":
    data = json.loads(sys.argv[1])
    nasPath = data["nasPath"]
    inputDir = data["inputDir"]
    outputDir = data["outputDir"]

    os.makedirs(nasPath + outputDir, exist_ok=True)

    wb = Workbook()
    ws = wb.active
    ws.append(["너비", "높이", "완료 시간"])

    img_arr = glob.glob(nasPath + inputDir + "/*.png")
    for i in img_arr:
        file_name = os.path.basename(i)

        img = cv2.imread(i)
        gray = make_gray(img)
        cv2.imwrite("temp_" + file_name, gray)
        add_bene(nasPath, outputDir, file_name)

        w, h = img.shape[:2]
        ws.append([w, h, arrow.utcnow().format()])
    
    wb.save(nasPath + outputDir + "/report.csv")
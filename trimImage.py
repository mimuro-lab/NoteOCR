import cv2
import os
from divideRayout import Label

class trimImage:
    def __init__(self, trimedImagePath:str):
        self.image = cv2.imread(trimedImagePath)

    def trimming(self, listOfTsv:list, outputFolder:str, headLabel:str):

        for l in listOfTsv:
            top = l[Label.top]
            bottom = top + l[Label.height]
            left = l[Label.left]
            right = left + l[Label.width]
            trimmedImage = self.image[top:bottom, left:right]
            imageName = headLabel + str(l[Label.page_num]) + "_" + str(l[Label.block_num]) + "_" + str(l[Label.par_num]) + "_" + str(l[Label.line_num])
            imagePath = os.path.join(outputFolder,imageName + ".jpg")
            print("making image  " + imagePath + "  ...", end = "")
            if(cv2.imwrite(imagePath, trimmedImage)):
                print("success!!")
            else:
                print("failed......")


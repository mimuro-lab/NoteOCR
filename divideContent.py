import os

from enum import IntEnum

class Label(IntEnum):
    level = 0
    page_num = 1
    block_num = 2
    par_num = 3
    line_num = 4
    word_num = 5
    left = 6
    top = 7
    width = 8
    height = 9
    conf = 10
    text = 11

class divideContent(object):

    def __init__(self, contentOfTsv:list):
        self.allOfContent = []

        # すべてのコンテンツを取得
        for l in contentOfTsv:
            if(l[Label.conf] != -1):
                self.allOfContent.append(l)

    def writeTextFile(self, listOfCell:list, saveFilePath:str):
        listOfText = []
        listOfConf = []
        for l in listOfCell:
            listOfText.append(l[Label.text])
            listOfConf.append(l[Label.conf])

        with open(saveFilePath, mode="w") as f:
            for l in listOfText:
                f.write(str(l) + "\t")

            f.write("\n")
            for l in listOfConf:
                f.write(str(l) + "\t")
        
    def writePageContent(self, outputFolder:str):
        # pageのみを取得
        pre_page_num = 1
        listOfCellPage = []
        for l in self.allOfContent:
            page_num = l[Label.page_num]

            isAppend = (page_num == pre_page_num)

            if(isAppend):
                listOfCellPage.append(l)
            else :
                saveFileName = "page_" + str(pre_page_num)
                saveFilePath = os.path.join(outputFolder, saveFileName + ".txt")
                print(saveFilePath,end = "") 
                self.writeTextFile(listOfCellPage, saveFilePath)
                print(" is made successfully!")
                listOfCellPage.clear()
                listOfCellPage.append(l)
            pre_page_num = page_num

        saveFileName = "page_" + str(pre_page_num)
        saveFilePath = os.path.join(outputFolder, saveFileName + ".txt")
        print(saveFilePath,end = "") 
        self.writeTextFile(listOfCellPage, saveFilePath)
        print(" is made successfully!")

    def writeBlockContent(self, outputFolder:str):
        # blockのみ取得
        pre_page_num = 1
        pre_block_num = 1
        listOfCellBlock = []
        for l in self.allOfContent:
            page_num = l[Label.page_num]
            block_num = l[Label.block_num]

            isAppend = (page_num == pre_page_num)\
                and (block_num == pre_block_num)\

            if(isAppend):
                listOfCellBlock.append(l)
            else :
                saveFileName = "block_" + str(pre_page_num) + "_" + str(pre_block_num)
                saveFilePath = os.path.join(outputFolder, saveFileName + ".txt")
                print(saveFilePath,end = "") 
                self.writeTextFile(listOfCellBlock, saveFilePath)
                print(" is made successfully!")
                listOfCellBlock.clear()
                listOfCellBlock.append(l)
            pre_page_num = page_num
            pre_block_num = block_num

        saveFileName = "block_" + str(pre_page_num) + "_" + str(pre_block_num)
        saveFilePath = os.path.join(outputFolder, saveFileName + ".txt")
        print(saveFilePath,end = "") 
        self.writeTextFile(listOfCellBlock, saveFilePath)
        print(" is made successfully!")

    def writeParContent(self,outputFolder:str):
        # parのみ取得
        pre_page_num = 1
        pre_block_num = 1
        pre_par_num = 1
        listOfCellPar = []
        for l in self.allOfContent:
            page_num = l[Label.page_num]
            block_num = l[Label.block_num]
            par_num = l[Label.par_num]

            isAppend = (page_num == pre_page_num)\
                and (block_num == pre_block_num)\
                and (par_num == pre_par_num)\

            if(isAppend):
                listOfCellPar.append(l)
            else :
                saveFileName = "par_" + str(pre_page_num) + "_" + str(pre_block_num) + "_" + str(pre_par_num)
                saveFilePath = os.path.join(outputFolder, saveFileName + ".txt")
                print(saveFilePath,end = "") 
                self.writeTextFile(listOfCellPar, saveFilePath)
                print(" is made successfully!")
                listOfCellPar.clear()
                listOfCellPar.append(l)
            pre_page_num = page_num
            pre_block_num = block_num
            pre_par_num = par_num

        saveFileName = "par_" + str(pre_page_num) + "_" + str(pre_block_num) + "_" + str(pre_par_num)
        saveFilePath = os.path.join(outputFolder, saveFileName + ".txt")
        print(saveFilePath,end = "") 
        self.writeTextFile(listOfCellPar, saveFilePath)
        print(" is made successfully!")

    def writeLineContent(self,outputFolder:str):
        # lineのみ取得
        pre_page_num = 1
        pre_block_num = 1
        pre_par_num = 1
        pre_line_num = 1
        
        listOfCellLine = []
        for l in self.allOfContent:
            page_num = l[Label.page_num]
            block_num = l[Label.block_num]
            par_num = l[Label.par_num]
            line_num = l[Label.line_num]

            isAppend = (page_num == pre_page_num)\
                and (block_num == pre_block_num)\
                and (par_num == pre_par_num)\
                and (line_num == pre_line_num)

            if(isAppend):
                listOfCellLine.append(l)
            else :
                saveFileName = "line_" + str(pre_page_num) + "_" + str(pre_block_num) + "_" + str(pre_par_num) + "_" + str(pre_line_num)
                saveFilePath = os.path.join(outputFolder, saveFileName + ".txt")
                print(saveFilePath,end = "") 
                self.writeTextFile(listOfCellLine, saveFilePath)
                print(" is made successfully!")
                listOfCellLine.clear()
                listOfCellLine.append(l)
            pre_page_num = page_num
            pre_block_num = block_num
            pre_par_num = par_num
            pre_line_num = line_num

        saveFileName = "line_" + str(pre_page_num) + "_" + str(pre_block_num) + "_" + str(pre_par_num) + "_" + str(pre_line_num)
        saveFilePath = os.path.join(outputFolder, saveFileName + ".txt")
        print(saveFilePath,end = "") 
        self.writeTextFile(listOfCellLine, saveFilePath)
        print(" is made successfully!")
        

        

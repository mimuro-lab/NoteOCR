
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
        
    def writePageContent(self):
        # pageのみを取得
        pre_page_num = 1
        listOfCellPage = []
        for l in self.allOfContent:
            page_num = l[Label.page_num]
            
            if(page_num == pre_page_num):
                listOfCellPage.append(l)
            else :
                print(listOfCellPage)
                listOfCellPage.clear()
                listOfCellPage.append(l)
      
            pre_page_num = page_num

    def writeBlockContent(self):
        # blockのみ取得
        pre_page_num = 1
        listOfCellPage = []
        for l in self.allOfContent:
            page_num = l[Label.block_num]
            
            if(page_num == pre_page_num):
                listOfCellPage.append(l)
            else :
                print(listOfCellPage)
                listOfCellPage.clear()
                listOfCellPage.append(l)
      
            pre_page_num = page_num

    def writeParContent(self):
        # parのみ取得
        pre_page_num = 1
        listOfCellPage = []
        for l in self.allOfContent:
            page_num = l[Label.par_num]
            
            if(page_num == pre_page_num):
                listOfCellPage.append(l)
            else :
                print(listOfCellPage)
                listOfCellPage.clear()
                listOfCellPage.append(l)
      
            pre_page_num = page_num

    def writeLineContent(self):
        # lineのみ取得
        pre_page_num = 1
        listOfCellPage = []
        for l in self.allOfContent:
            page_num = l[Label.line_num]
            
            if(page_num == pre_page_num):
                listOfCellPage.append(l)
            else :
                print(listOfCellPage)
                listOfCellPage.clear()
                listOfCellPage.append(l)
      
            pre_page_num = page_num
        

        

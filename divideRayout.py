
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

class divideRayout(object):

    def __init__(self, contentOfTsv:list):
        self.allOfRayout = []
        self.page = []
        self.block = []
        self.par = []
        self.line = []
        self.allOfRayout = []

        # すべてのレイアウトを取得
        for l in contentOfTsv:
            if(l[Label.conf] == -1):
                self.allOfRayout.append(l)
        
        # pageのみを取得
        for l in self.allOfRayout:
            if(l[Label.block_num] == 
               0):
                self.page.append(l)

        # blockのみ取得
        for l in self.allOfRayout:
            if(l[Label.block_num] != 0 
               and l[Label.par_num] == 0):
                self.block.append(l)


        # parのみ取得
        for l in self.allOfRayout:
            if(l[Label.block_num] != 0 
               and l[Label.par_num] != 0
               and l[Label.line_num] == 0):
                self.par.append(l)

        # lineのみ取得
        for l in self.allOfRayout:
            if(l[Label.block_num] != 0 
               and l[Label.par_num] != 0
               and l[Label.line_num] != 0
               and l[Label.word_num] == 0):
                self.line.append(l)


        
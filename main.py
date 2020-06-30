from readTSV import readTSV
from divideRayout import divideRayout
from trimImage import trimImage

import os

if __name__ == '__main__':

    tsv = readTSV("resource\sample.tsv")
    rayout = divideRayout(tsv.contentOfTsv)

    trim = trimImage("resource\sample.jpg")
   
    trim.trimming(rayout.page, os.path.join("result", "page"))
    trim.trimming(rayout.block, os.path.join("result", "block"))
    trim.trimming(rayout.par, os.path.join("result", "par"))
    trim.trimming(rayout.line, os.path.join("result", "line"))
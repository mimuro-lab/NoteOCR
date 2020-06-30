from readTSV import readTSV
from divideRayout import divideRayout

if __name__ == '__main__':

    tsv = readTSV("resource\test.tsv")
    rayout = divideRayout(tsv.contentOfTsv)

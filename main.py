from readTSV import readTSV
from divideRayout import divideRayout
from trimImage import trimImage

import os

if __name__ == '__main__':

    inputImage = os.path.join("resource", "sample.PNG")
    imageName = os.path.splitext(os.path.basename(inputImage))[0]
    print(imageName)

    outputFolder = os.path.join("result", imageName)
    os.makedirs(outputFolder, exist_ok=True)
    # フォルダ内を消去する
    for file in os.listdir(outputFolder):
        path = os.path.join(outputFolder, file)
        os.remove(path)
        print("removed ", path)

    tsvPath = os.path.join(outputFolder, "_OUTPUT_TSV")

    cmd = "tesseract " + inputImage + " " + tsvPath + " -l jpn tsv"
    print(cmd)
    os.system(cmd)

    tsvPath += ".tsv"

    # TSVファイルの読み込み
    tsv = readTSV(tsvPath)

    # Rayout成分のみ抜粋
    rayout = divideRayout(tsv.contentOfTsv)
    
    # 切り取り画像の設定
    trim = trimImage(inputImage)

    #trim.trimming(rayout.page, outputFolder, "page_")
    #trim.trimming(rayout.block, outputFolder, "block_")
    #trim.trimming(rayout.par, outputFolder, "par_")
    trim.trimming(rayout.line, outputFolder, "line_")



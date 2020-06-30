import csv

class readTSV:
    
    def __init__(self, tsvFilePath : str):
        # 処理するTSVファイル
        self.filename = tsvFilePath
        # TSVファイルの中身（2次元リスト）
        self.contentOfTsv = []
        with open(tsvFilePath, encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='\t')
            for l in reader:
                self.contentOfTsv.append(l)

        # ラベル
        self.label = self.contentOfTsv.pop(0)
        content = []
        for l in self.contentOfTsv:
            l = list(l)
            for i in range(0, len(l)):
                if(i == 11):
                    l[i] = str(l[i])
                else:
                    l[i] = int(l[i])
            content.append(l)
            
        self.contentOfTsv.clear()
        self.contentOfTsv = content

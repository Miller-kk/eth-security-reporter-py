import sys
sys.path.insert(0, "./Controller")
sys.path.append("./Lib")

## 기본적인 탐지 툴들을 클래스 별로 관리하기 위한 모듈들
## Author: Millerkk
import manticore as mt
import mythril as mr
import mythx as mx
import securify as sf
import slither as sl
import smartcheck as sc

## 탐지 툴들의 Json Output 파일들을 통일 하기 위한 파서 모듈들
## Author: Millerkk
import slitherParser as sParser
import mythxParser as mParser
import securifyParser as seParser
import manticoreParser as mtParser
import prettyPrint as pp



def detectionIntegration(filePath):
    manticore = mt.manticore(filePath)
    myth = mr.mythril(filePath)
    mythx = mx.mythx(filePath)
    securify = sf.securify(filePath)
    slither = sl.slither(filePath)
    smartcheck = sc.smartcheck(filePath)
    return [manticore,myth,mythx,securify,slither,smartcheck]

def jsonIntegration():
    detectionJson = detectionIntegration(sys.argv[1])
    naming  = ["manticore", "mythril", "mythx", "securify", "slither", "smartcheck"]
    totalJson = {}
    for idx, val in enumerate(detectionJson):
        totalJson[detectionJson[idx]] = val
    return totalJson
    
    
def parsingIntegration():
    try:
        slither_result = sParser.slitherParser()
    except:
        slither_result = ""
    try:
        mythx_result = mParser.mythxParser()
    except:
        mythx_result = ""
    try:
        securify_result = seParser.securifyParser()
    except:
        securify_result = ""
    try:
        manticore_result = mtParser.manticoreParser()
    except:
        manticore_result = ""
    return [slither_result,mythx_result,securify_result,manticore_result]
    

detectionIntegration(sys.argv[1])
infoArray = parsingIntegration()
infoTools =["slither","mythx","securify","manticore"]

totalData = jsonIntegration()
print(totalData)


for idx, val in enumerate(infoTools):
    pp.prettyPrint(val, infoArray[idx])



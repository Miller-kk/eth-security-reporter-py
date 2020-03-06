import sys
sys.path.insert(0, "/eth-security-reporter-py/Controller")
sys.path.append("/eth-security-reporter-py/Lib")

## 기본적인 탐지 툴들을 클래스 별로 관리하기 위한 모듈들
## Author: Millerkk
import manticore as mt
import mythril as mr
import mythx as mx
import securify as sf
import slither as sl
import smartcheck as sc
import initializer as init

## 탐지 툴들의 Json Output 파일들을 통일 하기 위한 파서 모듈들
## Author: Millerkk
import slitherParser as sParser
import mythxParser as mParser
import securifyParser as seParser
import manticoreParser as mtParser
import smartcheckParser as scParser
import prettyPrint as pp



def detectionIntegration(filePath):
    manticore = mt.manticore(filePath)
    myth = mr.mythril(filePath)
    mythx = mx.mythx(filePath)
    securify = sf.securify(filePath)
    slither = sl.slither(filePath)
    smartcheck = sc.smartcheck(filePath)
    smartcheck_result = smartcheck.output.decode("utf-8")
    pp.stringTofile(smartcheck_result, "smartcheck")
    
    return [manticore,myth,mythx,securify,slither,smartcheck]


def jsonIntegration(detectionJson):
    naming  = ["slither","mythx","securify","manticore","smartcheck"]
    totalJson = {}
    for idx, val in enumerate(detectionJson):
        totalJson[naming[idx]] = val
    return totalJson
    
    
def parsingIntegration():
        slither_result = sParser.slitherParser()
        #mythx_result = mParser.mythxParser()
        mythx_result = ""
        securify_result = seParser.securifyParser()
        manticore_result = mtParser.manticoreParser()
        smartcheck_result = scParser.smartcheckParser()
        return [slither_result, mythx_result, securify_result, manticore_result, smartcheck_result]
    
def run(fileName):
    init.initFiles()
    detectionIntegration(fileName)
    infoArray = parsingIntegration()
    infoTools =["slither","mythx","securify","manticore","smartcheck"]
    totalData = jsonIntegration(infoArray)
    pp.createTable(totalData)

    for idx, val in enumerate(infoTools):
        pp.prettyPrint(val, infoArray[idx])

#run(sys.argv[1])

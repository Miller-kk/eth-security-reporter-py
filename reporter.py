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



def detectionIntegration(filePath):
    manticore = mt.manticore(filePath)
    myth = mr.mythril(filePath)
    mythx = mx.mythx(filePath)
    securify = sf.securify(filePath)
    slither = sl.slither(filePath)
    smartcheck = sc.smartcheck(filePath)
    
def parsingIntegration():
    slither_result = sParser.slitherParser()
    mythx_result = mParser.mythxParser()
    securify_result = seParser.securifyParser()
    print(securify_result)

integration(sys.argv[1])
#print(sys.argv[1])

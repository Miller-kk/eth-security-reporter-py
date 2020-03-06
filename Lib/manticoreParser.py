def manticoreParser():
    result = []
    newJson = {}
    result_data = open('./manticore/global.findings').read().split("\n")
    for data in result_data:
        print(data)
        if(data == ""):
            newJson = {}
        else:
            if("-" in data):
                newJson["name"] = data.replace("-", "")
                newJson["description"] = ''
            elif (data != ''):
                parseData = data.split(" ")
                if(len(parseData) > 4):
                    if (parseData[4].isdigit()):
                        newJson["impact"] = ''
                        newJson["lines"] = parseData[4]
                        newJson["description"] = data
                        result.append(newJson)
    return result

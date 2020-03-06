import json

def slitherParser():
    result = []
    newJson = {}
    with open('/eth-security-reporter-py/result_data/slither.json') as json_file:
        json_data = json.load(json_file)
        for data in json_data["results"]["detectors"]:
            newJson["name"] = data["check"]
            newJson["description"] = data["description"]
            newJson["impact"] = data["impact"]
            newJson["lines"] = []
            result.append(newJson)
            newJson = {}
        return result

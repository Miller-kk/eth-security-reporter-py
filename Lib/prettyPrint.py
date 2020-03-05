def prettyPrint(tool, infoArray):
    print("\n\n########################################"+tool+" Result########################################\n")
    if(infoArray == ''):
        print("error - " +tool)
    else:
        for info in infoArray:
            print("===============================================================================")
            print("Name: " + info["name"])
            print("description: " + info["description"])
            print("impact: " + info["impact"])
            for line in info["lines"]:
                print("lines: " + str(line))
def prettyPrint(tool, infoArray):
    print("\n\n====================================="+tool+" Result=====================================\n")
    for info in infoArray:
        print("===============================================================================")
        print("Name: " + info["name"])
        print("description: " + info["description"])
        print("impact: " + info["impact"])
        print("lines: " + info["lines"])
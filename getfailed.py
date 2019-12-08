def getfails():
    fails =[]
    with open("fails.txt",'r') as file:
        data=file.read().split("\n")
        for line in data:
            if line != "":
                fails.append(eval(line.split("isCovered")[1].split(", '")[0]))
        file.close
    return fails

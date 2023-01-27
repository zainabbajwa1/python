str="The"
def doubleChar(str):
    myVar=""
    for i in range(len(str)):
        myVar+= str[i] *2
    print(myVar)

doubleChar(str)
str="Heeololeo"

def fun(str):
    newStr= ""
    for i in range(len(str)):
        if(i%2)==0:
            newStr+=str[i]
    print(newStr)

fun(str)
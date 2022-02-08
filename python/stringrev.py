# def stringRev(aString):
#    stri=''
#    lenOfString=len(aString)
#    arrString=list(aString)
#    revStringArr=[]
#    for x in range(0,lenOfString):
#       revStringArr.append(arrString[lenOfString-x-1])
#    return stri.join(revStringArr)

# def stringRev(aString):
#     arrString=list(aString)
#     revString=''
#     for x in arrString:
#         revString=x+revString
#     return revString

def stringRev(aString):
    return aString[::-1]
    
    
print(stringRev('hello'))

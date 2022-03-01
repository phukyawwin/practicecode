noOfTestCases=int(input())
linesString=[]
for x in range(noOfTestCases):
    linesString.append(input())
for x in linesString:
    evenString=''
    oddString=''
    for a in range(len(x)):
        if (a%2==0):
            evenString+=x[a]
        else:
            oddString+=x[a]
    print(evenString +' ' +oddString)
        

def average1(salary):
    salary.sort()
    avg=0
    listLen=len(salary)
    for i in range(1,listLen-1):
        avg+=salary[i]

    return avg/(listLen-2)

def average2(salary):
    salary.sort()
    salary.pop(0)
    salary.pop(-1)
    return sum(salary)*1.0/len(salary)

def average3(salary):
    return (sum(salary)-max(salary)-min(salary))/(len(salary)-2)

salary = [4000,3000,1000,2000]
print(average3(salary))

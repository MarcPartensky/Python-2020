import itertools as it
import numpy as np

n=4

def enum(n):
    for i in reversed(range(1,n+1)): #Number of characters considered
        for j in reversed(range(0,n+1)): #Number of characters used
            for k in it.combinations(range(1,i),j):
                yield k+(i,)


def select(n, r):
    a = 0
    e = enum(n)
    x = next(e)
    while x!=r:
        a+=1
        x = next(e)
    if x==r:
        return a

def getSoldiers(skills, requirement):
    soldiers = []
    for j in range(len(requirement)):
        if int(requirement[j]):
            for i in range(len(skills)):
                if int(skills[i][j]) and not(i+1 in soldiers):
                    soldiers.append(i+1)
                    break
    return soldiers


#Test case
skills = ['00', '10', '01', '11']
requirement = '01'

#using functions
soldiers = tuple(getSoldiers(skills, requirement))
choosen = select(n, soldiers)

#output
print(choosen%(10**9+7))


#Maybe the algorithm is right, but it is too long to execute,
#it didn't pass time limit

const a = 5

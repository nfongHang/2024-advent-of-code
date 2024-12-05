import re
import numpy
f=open("input2024day5advent.txt","r")
part1={}
part2=[]
mode=False
#parsing
for line in f:
    if line=="\n":
        mode=True
    elif not mode:
        line=line.strip().split("|")
        if not line[0] in part1.keys():
            part1.update({line[0]:[line[1]]})
        else:
            part1[line[0]].append(line[1])
    elif mode:
        part2.append(line.strip().split(","))

#THIS MUST COME FIRST   BEFORE THIS APPEARS IN THE LINE
#                  97 | 75

#for utility
def printDict(dictionary : dict):
    for key in dictionary.keys():
        print(key,dictionary[key])

def followsRule(num1,num2) -> bool:
    """
    Returns boolean
    True if the two numbers ( IN ORDER ) follow the rule
    Will return True if the number is not specified
    will return False if it breaks the rule
    """
    #printDict(part1)
    #print(part1.keys())
    # if num1 is in num2's rules, meaning num1 should have gone after num2:
    if num2 in part1.keys():
        if num1 in part1[num2]:
            return False
        #if it isnt in the rules, should be fine ig
    return True
wrong=[]
final=[]
for line in part2:
    ok=True
    for i in range(len(line)-1):
        if not followsRule(line[i],line[i+1]):
            ok=False
    if ok==True:
        final.append(line)
    else:
        wrong.append(line)

#print(final)
total=0
for line in final:
    total+=int(line[len(line)//2])
print("Part 1:",total)



h=[]
for line in wrong:
    for i in range(len(line)-1):
        for i in range(len(line)-1):
            if not followsRule(line[i],line[i+1]):
                #swap
                temp=line[i]
                line[i]=line[i+1]
                line[i+1]=temp
    h.append(line)
total=0
for line in h:
    total+=int(line[len(line)//2])
print("Part 2:",total)
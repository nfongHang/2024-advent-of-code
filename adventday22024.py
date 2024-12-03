f=open("input2024day2advent.txt","r")
data=[]
for line in f:
    line=line.strip("\n")
    line=line.split(" ")

    for num in range(len(line)):
        line[num]=int(line[num])
    
    data.append(line)

safe=0
count=0

#function to test whether if the line is valid
def test(line):
    increasing=-1
    ok=True
    for x in range (len(line)-1):
        diff=line[x]-line[x+1]
        if increasing==-1:
            if diff>0:
                increasing=False
            else:
                increasing=True
        
        if not ok==False:
            #if the difference is within 1-3
            if abs(diff)>=1 and abs(diff)<=3:
                #test if the numbers are increasing
                #if decreasing:
                    if increasing:
                        if not diff<0:
                            ok=False
                    else:
                        if not diff>0:
                            ok=False
            else:
                ok=False
    if ok==True:
        return True
    
# Part 1
for line in data:
    if test(line):
        safe+=1
print("Part 1:", safe)
safe=0

# Part 2
for line in data:
    set=[]
    for i in range(len(line)):
         a=line.copy()
         a.pop(i)
         set.append(a)
    ok=False
    for thing in set:
        result=test(thing)
        if result==True:
             safe+=1
             break

print("Part 2:", safe)
                
f.close()

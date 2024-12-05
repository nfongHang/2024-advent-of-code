import re
import numpy
f=open("input2024day4advent.txt","r")
data=[]
linelen=0
for line in f:
    linelen=len(line)
    data.append(line.strip("\n"))

# dataset is all the strings to be processed via regex at the end
dataset=[]

#PART 1

#horizontal lines
for line in data:
    dataset.append(line)
#vertical lines
#for each row
for i in range(len(data)):
    temp=""
    #each column:
    for x in range(len(data[i])):
        temp+=data[x][i]
    dataset.append(temp)


# split data into single character list in order to work with numpy.diagonal     
for line in data:
    data[data.index(line)]=[*line]

# Iterate through all diagonal patterns
#       join all 2D list of diagonal characters back into a string
for x in range(1-len(data),len(data)):
    dataset.append("".join(numpy.diagonal(data,x)))

# invert data
for line in data:
    data[data.index(line)]=line[::-1]

# Iterate through all diagonal patterns
#       join all 2D list of diagonal characters back into a string
for x in range(1-len(data),len(data)):
    dataset.append("".join(numpy.diagonal(data,x)))


# ----------------------------- PART 1 SOL --------------------------------------------------
a=0
for line in dataset:
    a+=len(re.findall(r"XMAS",line))
    a+=len(re.findall(r"XMAS",line[::-1]))
        #if "XMAS" in item:
        #    a+=1
        #if "XMAS"[::-1] in item:
        #    a+=1

print("Part 1:",a)


# Part 2

dataset=[]


for x in range(1-len(data),len(data)):
    dataset.append("".join(numpy.diagonal(data,x)))

# invert data
for line in data:
    data[data.index(line)]=line[::-1]

for x in range(1-len(data),len(data)):
    dataset.append("".join(numpy.diagonal(data,x)))

def check_x_mas(i,j):

    '''
    All Cases to be tested:
    1.  2.  3.   4.
    M.M S.S M.S. S.M
    .A. .A. .A.  .A.
    S.S M.M M.S  S.M.
    '''

    #if on border: return false
    if i <= 0 or j <= 0 or i >= len(data[0])-1 or j >= len(data)-1:
        return False
    
    #case1:
    #top left                   top right              bottom left          bottom right
    if data[i-1][j+1]=="M" and data[i+1][j+1]=="M" and data[i-1][j-1]=="S" and data[i+1][j-1]=="S":
        return True
    elif data[i-1][j+1]=="S" and data[i+1][j+1]=="S" and data[i-1][j-1]=="M" and data[i+1][j-1]=="M":
        return True
    elif data[i-1][j+1]=="M" and data[i+1][j+1]=="S" and data[i-1][j-1]=="M" and data[i+1][j-1]=="S":
        return True
    elif data[i-1][j+1]=="S" and data[i+1][j+1]=="M" and data[i-1][j-1]=="S" and data[i+1][j-1]=="M":
        return True
    else:
        return False

# --------------------------- PART 2 SOL -------------------------------------
a=0
for j in range(0,len(data)):
    for i in range(0,len(data[j])):
        if data[i][j]=="A":
            if check_x_mas(i,j):
                a+=1
print("Part 2:",a)
import searching_and_sorting 


#Part 1

f=open("input2024day1advent.txt")
list1=[]
list2=[]

for line in f:
    temp=line.split("   ")
    list1.append(int(temp[0]))
    list2.append(int(temp[1].strip()))

list1=searching_and_sorting.mergeSort(list1)
list2=searching_and_sorting.mergeSort(list2)

sum=0

for x in range(len(list1)):
    sum+=abs(list1[x]-list2[x])

print("Distance:",sum)

# Part 2


def countFreq(data):
    freq={}
    for item in data:
        if not item in freq.keys():
            freq.update({item:1})
        else:
            freq[item]+=1
    return freq

freq1=countFreq(list1)
freq2=countFreq(list2)
similarity=0
freq2keys=freq2.keys()
for item in freq1.keys():
    if item in freq2keys:
        similarity+=item*freq2[item]*freq1[item]

print("Similarity:",similarity)




f.close()
import searching_and_sorting 
import datastructures
f=open("input2024day3advent.txt","r")
data=[]

number=["0","1","2","3","4","5","6","7","8","9"]

def checkValidMuls(data,total=0, do=True):
    print("data",data)
    #check do or dont
    
    if data.find("do()")<data.find("mul(") and data.find("do()")!=-1:
        print("DOOOOO1",data[data.find("do()"):])
        do=True
    if data.find("don't()")<data.find("mul(") and data.find("don't()")!=-1:
        print("DOOOOONT1 index:",data.find("don't()"))
        do=False

    # find index of each "mul("
    # flag for first number OK, comma, and a second number and end bracket
    invalid=False
    for index in range(data.find("mul(")+4,len(data)):
        end=False
        if not end:
            firstNum=True
            secondNum=True
            #If its not invalid, reset it
            if not invalid:
                #first number:
                operand1=""
                while firstNum:
                    #try to make int
                    print(data[index])
                    if data[index] in number:
                        #add into operand
                        operand1+=data[index]
                        index+=1

                    else:
                        #if it cannot become int:
                        #check if it is a comma
                        if data[index]==",":
                            firstNum=False # move on
                        else:
                            #else if its just some random thing
                            print('WRONG SMH')
                            firstNum=False
                            invalid=True
                if not invalid:
                    operand1=int(operand1)
                print('moved on to secon, had comma')
                operand2=""
                index+=1
                while secondNum:
                    #try to make int
                    print(data[index])
                    if data[index] in number:
                        #add into operand
                        
                        operand2+=data[index]
                        index+=1

                    else:
                        #if it cannot become int:
                        #check if it is a bracket
                        if data[index]==")":
                            secondNum=False # move on
                            print(line,"\n",operand1,operand2)
                            if operand2!="" and do:
                                total+=operand1*int(operand2)
                                print(total,"yayayaya","op 1 and 2:",operand1,operand2)
                            else:
                                print(total,"didnt add but yayayaya","op 1 and 2:",operand1,operand2)
                            end=True
                        else:
                            #else if its just some random thing
                            secondNum=False
                            invalid=True
                            end=True
        if end:
            if data[index:].find("mul(")!=-1:
                total=checkValidMuls(data[index:],total,do)
                #go to the next index of mul
            print('end!',total)
            return total






for line in f:
    data.append(line)
total=0
for line in data:
    input("start!!!")
    total+=(checkValidMuls(line))
print(total)

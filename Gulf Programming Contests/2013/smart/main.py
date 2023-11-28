def  calculate(line):
    line = "".join(line)
    line = line.split("=")

    
    total=0
    total2=0
    previous_sign2=1
    previous_sign=1
    temp=""
    x_sign=1
    for i in range(len(line)):
        if "?" in line[i]:
            for j in range(len(line[i])):
                if line[i][j]!= "+" and line[i][j]!= "-" and line[i][j]!= "?":

                    temp+=line[i][j]
                    if j==len(line[i])-1:
                        total+=int(temp)*previous_sign
                else:
                    if temp:
                        total+=int(temp)*previous_sign
                    temp=""
                    if line[i][j]=="+":
                        previous_sign=1
                    elif line[i][j]=="-":
                        previous_sign=-1
                    elif line[i][j]=="?":
                        x_sign=previous_sign

            temp=""
        else:
            for j in range(len(line[i])):
                if line[i][j]!= "+" and line[i][j]!= "-" and line[i][j]!= "?":
                    temp+=line[i][j]     
                    if j==len(line[i])-1:
                        total2+=int(temp)*previous_sign2           
                else:
                    if temp:
                        total2+=int(temp)*previous_sign2
                    temp=""
                    if line[i][j]=="+":
                        previous_sign2=1
                    elif line[i][j]=="-":
                        previous_sign2=-1

            temp=""
    unsigned_answer=-1*total+total2
    signed_answer= unsigned_answer*x_sign
    return signed_answer

with open("smart.answer","w"):
    pass

lines=[]

with open("smart.in","r")as file:
    for line in file:
        line_value = line.strip().split()
        lines.append(line_value)

testcase=1
for line in lines:
    answer = calculate(line)
    print( answer)
    testcase+=1
    with open("smart.answer","a") as file:
        file.write(str(answer)+"\n")
def calculate(line):
    answer = line[0]-(line[2]-line[3])
    
    if answer > line[0]:
        answer=line[0]
    if answer <1:
        answer=1
    return answer

with open("league.answer","w"):
    pass

lines=[]
with open("league.in","r")as file:
    for line in file:
        values = [int(value) for value in line.strip().split()]
        lines.append(values)
        


lines.pop(0)
testcase=1
for line in lines:
    answer = calculate(line)
    with open("league.answer","a")as file:
        file.write(str(testcase)+". "+str(answer)+'\n')
    testcase+=1
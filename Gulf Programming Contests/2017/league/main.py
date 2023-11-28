lines=[]

with open("league.in","r") as file:
    for line in file:
        lines.append([int(value) for value in line.strip().split()])
        
lines.pop(0)
testcase=1
text=""
for line in lines:
    teams=line[0]
    answer = teams-1
    answer = answer*2
    answer = answer *3
    
    text+=str(testcase)+". "+str(answer)+"\n"
    testcase+=1
with open("league.answer","w") as file:
    file.write(text)
    
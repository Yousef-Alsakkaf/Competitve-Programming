lines=[]

with open("champion.in","r")as file:
    for line in file:
        values = [int(value) for  value in line.strip().split()]
        lines.append(values)
        
lines.pop(0)
testcase=1
text=""
for i in range(0,len(lines),2):
    first_team_home=lines[i][0]
    second_team_away=lines[i][1]
    second_team_home=lines[i+1][0]
    first_team_away=lines[i+1][1]
    
    total_team1=first_team_home+first_team_away
    total_team2=second_team_home+second_team_away
    
    if total_team1>total_team2:
        text+=str(testcase)+". The first team wins!\n"
    elif total_team1<total_team2:
        text+=str(testcase)+". The second team wins!\n"
    else:
        if first_team_away > second_team_away:
            text+=str(testcase)+". The first team wins!\n"
        elif first_team_away < second_team_away:
            text+=str(testcase)+". The second team wins!\n"
        else:
            text+=str(testcase)+". Extra time is needed!\n"

    testcase+=1
with open("champion.answer","w")as file:
    file.write(text)
            
        
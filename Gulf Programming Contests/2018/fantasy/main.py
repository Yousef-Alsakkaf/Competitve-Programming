def calculate(budget,num_players,allowed_players,players):
    players = sorted(players, key=lambda x: (-x[0], x[1]))
    
    count=0
    remaining_budget=budget
    total=0
    total_players=0
   
    while count<allowed_players:
        found=False
        for i  in range(len(players)):
            player=players[i]
            if player[1]>remaining_budget:
                continue
            
            remaining_budget-=player[1]
            total+=player[0]
            players.pop(i)
            found=True
            break
        if found:
            total_players+=1
        count+=1
       
    
    if total_players<allowed_players:
        return "imposible"
    else:
        return total
lines=[]
with open("fantasy.in","r")as file:
    for line in file:
        lines.append([float(value) for value in line.strip().split()])
        


testcases=int(lines[0][0])
counter=0
lines.pop(0)
players=[]
testcase=1
for i in range(len(lines)):
    if testcases==0:
        break
    if i==counter:
        
        budget,num_players,allowed_players=lines[i]
        num_players=int(num_players)
        budget=int(budget)
        allowed_players=int(allowed_players)
        counter+=num_players+1
        for j in range(i+1,counter):
            players.append(lines[j])
        
        
        answer= calculate(budget,num_players,allowed_players,players)
        testcase+=1
        players=[]
        testcases-=1
       
        
        
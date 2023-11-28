def posible(string):
    list=[]
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            unique= set(string[i:j:])

            if len(unique)==1:
                replace=""
                for k in range(j-i):
                    replace+="X"
                newstring=string[0:i:]+replace+string[j::]
                if string.count("X") != newstring.count("X"):
                    list.append(newstring)
    return list

def min(map,player1,player2,memo_max,memo_min):
    if str(map)in memo_min:
        return memo_min[str(map)]
    if str(map)in memo_max:
        return memo_max[str(map)]*-1
    counter=0
    for line in map:
        counter+=line.count("O")
    if counter==0:
        return -1
    
    point=1
    for i in range(len(map)):
        moves=posible(map[i])
        for move in moves:
            map_copy=map.copy()
            map_copy[i]=move
            resualt=max(map_copy,player1,player2,memo_max,memo_min)
            if resualt==-1:
                memo_min[str(map)]=-1
                point=-1
    memo_min[str(map)]=point
    return point

def max(map,player1,player2,memo_max,memo_min):
    if str(map)in memo_max:
        return memo_max[str(map)]
    if str(map)in memo_min:
        return memo_min[str(map)]*-1
    counter=0
    for line in map:
        counter+=line.count("O")
    if counter==0:
        return 1
    point=-1
    for i in range(len(map)):
        moves=posible(map[i])
        for move in moves:
            map_copy=map.copy()
            map_copy[i]=move
            resualt=min(map_copy,player1,player2,memo_max,memo_min)
            if resualt==1:
                memo_max[str(map)]=1
                point=1
    memo_max[str(map)]=point
    return point
               

lines=[]

with open("minmax.in","r")as file:
    for line in file:
        lines.append(line.strip().split())
        
lines.pop(0)

text=""
memo_max={}
memo_min={}
for line in lines:
    map=line[:4:]
    player1=line[4]
    player2=line[5]

    
    answer = max(map,player1,player2,memo_max,memo_min)
    if answer==1:
        print(player1)
        text+=str(player1)+"\n"
    elif answer==-1:
        print(player2)
        text+=str(player2)+"\n"
        
with open("minmax.answer","w")as file:
    file.write(text)
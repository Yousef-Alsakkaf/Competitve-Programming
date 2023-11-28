def  calculate(map, points,velocity,max,time,length):
    print(map, points,velocity,max,time,length)
    position = map[0]
    escape = map[len(map)-1]
    print(position,escape)
    map.pop(0)
    

    return
lines=[]

with open("elvis.in","r")as file:
    for line in file:
        lines.append([int(valu) for valu in line.strip().split()])
  

lines.pop(0)
counter=0
map=[]
for i in range(len(lines)):
    if i == counter:
        points,velocity,max,time=lines[i]
        counter+= points+1
        for j in range(i+1,counter):
            map.append(lines[j])
        
        
        answer= calculate(map, points,velocity,max,time,4)
        map=[]
        break
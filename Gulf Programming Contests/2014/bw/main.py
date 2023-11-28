import math

def calcualte(old,positions):

    colors=[]
    for position in positions:
        min= float("inf")
        color= ""
        for building in old:
            x= position[0]- building[0]
            x= x**2
            y= position[1]- building[1]
            y= y**2
            
            value = x+y
            
            distance = math.sqrt(value)
            
            if distance<min:
                color=building[2]
                min=distance
        colors.append(color)
    
    answer = "\n".join(colors)
                
    answer=answer+"\n"
    return answer
lines=[]

with open("bw.in","r")as file:
    for line in file:
        values = line.strip().split()
        lines.append(values)

print(lines)
lines.pop(0)
lines.pop()

old=[]
positions=[]
for i in range (len(lines)):
    line=lines[i]
    if len(line)==3:
        line[0]= float(line[0])
        line[1]= float(line[1])
        old.append(line)
    if len(line)==2:
        line[0]=float(line[0])
        line[1]=float(line[1])
        positions.append(line)
        
        if i +1 ==len(lines):
            #end of testcase start calculating
            answer = calcualte(old,positions)
            print(answer)
            with open("bw.answer","w") as file:
                file.write(answer)
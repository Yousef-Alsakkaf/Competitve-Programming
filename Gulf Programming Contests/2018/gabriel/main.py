import math
def find_distance(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def find_mid(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return [(x2+x1)/2,(y2+y1)/2]

def calculate(map,num_of_nodes):
   
    list=[]
    for i in range(len(map)):
        templist=[]
        for j in range(len(map)):
            if i ==j:
                continue
            
            midpoint=find_mid(map[i],map[j])
            distance=find_distance(midpoint,map[j])
            found=False
            for k in range(len(map)):
                if map[k]== map[i] or map[k]== map[j]:
                    continue
                
                distance2= find_distance(midpoint,map[k])
                if distance2<distance:
                    found=True
                    break
            if found:
                continue
            templist.append(j+1)
        list.append(templist)
            
            
    return list
lines=[]

with open("gabriel.in","r") as file:
    for line in file:
        lines.append([int(value)for value in line.strip().split()])



lines.pop(0)
counter=0
testcase=1
text=""
for i in range(len(lines)):
    if i == counter:
 
        if len(lines[i])==0:
            break
        num_of_nodes=lines[i][1]
        counter+=num_of_nodes+1
        map=[]
        for j in range(i+1,counter):
            map.append([lines[j][1],lines[j][2]])
        answer = calculate(map,num_of_nodes)
        text+= str(testcase)+"\n"
        for z in range(len(answer)):
            temp= answer[z]
            for x in range(len(temp)):
                temp[x]=str(temp[x])
            text+=str(z+1)+" "+" ".join(temp)+"\n"
            print(str(z+1)+" "+" ".join(temp))
        testcase+=1

with open("gabriel.answer","w")as file:
    file.write(text)
        
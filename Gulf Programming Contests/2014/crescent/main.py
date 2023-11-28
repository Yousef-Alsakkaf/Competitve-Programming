import math
def distance(x1,x2,y1,y2):
    
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def calculate(ax ,ay ,cx, cy, d,points):
    print(ax ,ay ,cx, cy, d,points)
    
    radius1= distance(cx,ax,cy,ay)
    cx2= cx+d
    cy2=cy
    radius2=radius1
    list=[]
    for point in points:
        value1=distance(cx,point[0],cy,point[1])
        value2=distance(cx2,point[0],cy2,point[1])
        check1= abs(value1-radius1)<=1 and abs(value1-radius1)>=0
        check2= abs(value2-radius2)<=1 and abs(value2-radius2)>=0
        if check1 or check2:
            list.append("on crescent")
        elif value1< radius1 and value2> radius2:
            list.append("inside crescent")
        else:
            list.append("outside crescent")
    
    print(list)
    
    answer = "\n".join(list)
    return answer

lines=[]

with open("crescent.in","r")as file:
    for line in file:
        values = [int(value) for  value in line.strip().split()]
        lines.append(values)
        
print(lines)
lines.pop(0)
counter =0
points=[]
text=""
for i in range(len(lines)):
    if i ==counter:
        ax ,ay ,cx, cy, d= lines[i]
        num_of_dots=lines[i+1][0]
        counter = num_of_dots+2
        for j in range(i+2,counter):
            points.append(lines[j])
        
        answer= calculate(ax ,ay ,cx, cy, d,points)
        print(answer)
        answer +="\n"
        text+=answer
        
with open("crescent.answer","w") as file:
    file.write(text)
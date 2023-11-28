import math
def calculate(h1,h2,h3):
    print(h1,h2,h3)
    person_height=1.67
    arm_length=0.5
    
    original_X= 5*math.cos(math.radians(30))

    angle = math.radians(30)
    max_steps=9
    
    lamp1=[3,10-h1]
    lamp2=[2,10-h2]
    lamp3=[1,10-h3]
    list=[-1,-1,-1]
    for i in range(max_steps+1):
        steps=i
        angled_covored= 0.5*steps
        x=(original_X- (math.cos(angle)*angled_covored))+arm_length
        y=(math.sin(angle)*angled_covored)+person_height
        
        print(x,lamp1[0])
        print(y,lamp1[1])
        print(x,lamp2[0])
        print(y,lamp2[1])
        print(x,lamp3[0])
        print(y,lamp3[1])
        if x>lamp1[0] and y>lamp1[1] and list[0]==-1:
            list[0]=i
        if x>lamp2[0] and y>lamp2[1] and list[1]==-1:
            list[1]=i
        if x>lamp3[0] and y>lamp3[1] and list[2]==-1:
            list[2]=i
            
        print(list)
        text=""
        for answer in list:
            if answer==-1:
                text+="N "
            else:
                text+= str(answer)+" "
                
    return text

lines=[]

with open("ladder.in","r")as file:
    for line in file:
        lines.append([int(value) for value in line.strip().split()])
        
print(lines)

lines.pop(0)

for line in lines:
    h1,h2,h3=line
    answer = calculate(h1/10,h2/10,h3/10)
    print(answer)
    break
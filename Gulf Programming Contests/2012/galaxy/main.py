import math
def distance(p1,p2):
    x1,y1=p1
    x2,y2=p2
    
    return  math.sqrt((x2-x1)**2+(y2-y1)**2)
def triengle(p1,p2,p3):
    x1,y1=p1
    x2,y2=p2
    x3,y3=p3

    return 1/2 *abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
    
def radius(distance1,distance2,distance3,area):
    return (distance1*distance2*distance3)/(4*area)    
def calculate(galaxies):
    
    areas=[]
    for i in range(len(galaxies)):
        x1,y1,x2,y2,x3,y3=galaxies[i]
     
        distance1=distance([x1,y1],[x2,y2])
        distance2=distance([x2,y2],[x3,y3])
        distance3=distance([x3,y3],[x1,y1])
        
        area=triengle([x1,y1],[x2,y2],[x3,y3])
        
        areas.append(radius(distance1,distance2,distance3,area)**2)
    areas.sort()

    counter=0
    i=0
    
    while i <len(areas)-1:
        
        found=False
        j=i+1
        
        if j<len(lines)and areas[j]>=2*areas[i]:
                counter+=1
                i=j
                continue
        while j<len(lines)and areas[j]<2*areas[i]:
            
            j+=1

            if j== len(areas):
                break
            if j<len(lines)and areas[j]>=2*areas[i]:
                
                found=True
                counter+=1
                i=j
                break
            
        if not found:  
            i+=1
            
   
    
    return counter
    
    
lines=[]
with open("galaxy.in","r")as file:
    for line in file:
        lines.append([int(value)for value in line.strip().split()])
        
print(lines)
text=""
lines.pop(0)
counter=0
galaxies=[]
for i in range(len(lines)):
    if i ==counter:
        num=lines[i][0]
        counter+=num+1
        for j in range(i+1,counter):
            galaxies.append(lines[j])
        
        answer= calculate(galaxies)
        galaxies=[]
        text+= str(answer)+"\n"
        
with open("galaxy.answer","w")as file:
    file.write(text)
       
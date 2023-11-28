import time
import math
def isRange(cord1,cord2,R):

    x1,y1=cord1
    x2,y2=cord2
  
    return math.sqrt((x1-x2)**2+(y1-y2)**2)<=R
    
    
def calculate(map,T,I,R,D):
    # print(map,T,I,R,D)
    infected=[]
    normal=[]
    for i in range(len(map)):
        for j in range(len(map[i])):
    
            if map[i][j]==1:

                normal.append([i,j])
            if map[i][j]==-1:
                infected.append([i,j])
    
    
    hash={"0":[]}
    for i in range(len(infected)):
        hash["0"].append(infected[i])

    t=I
    while t<D:
        



        keys=[]
        for key in hash:
            if t-T>=int(key):
                cords= hash[key]
                for cord in cords:
                    infected.remove(cord)
                keys.append(key)
                
        for key in keys:
            del hash[key]
        length= len(infected)
        
        i=0
       

        while i<length:
            j=0

            while j<len(normal):
                if isRange(infected[i],normal[j],R):

                    cord = normal.pop(j)
                    infected.append(cord)
                    if str(t) not in hash:
                        hash[str(t)]=[cord]
                    else:
                        hash[str(t)].append(cord)
                    j-=1
                    
                j+=1
            i+=1

        t+=I
     

    return len(infected)


lines=[]
with open("flu.in","r") as file:
     # Iterate through the lines in the file
    for line in file:

        
         # Convert the values to integers and append to the 'lines' list
        line_values = line.strip().split()
        lines.append(line_values)
counter = 0
map=[]
for i in range(len(lines)):
    if i ==counter:
        
        if lines[i]==["0","0"]:
            break
        
        
        w,h=lines[i]
        w= int(w)
        h=int(h)
        counter+=h+2

        T,I,R,D=lines[i+1]
        T=int(T)
        I=int(I)
        R=int(R)
        D=int(D)

        for j in range(i+2,counter):
            map.append(lines[j][0])
       
        map2=[]
        for z in range(len(map)):
            array=[]
            for k in range(len(map[z])):
                if map[z][k]=="X":
                    array.append(0)
                if map[z][k]=="P":
                    array.append(1)
                if map[z][k]=="I":
                    array.append(-1)
            map2.append(array)
            
 
        answer = calculate(map2,T,I,R,D)
        map=[]    
        print(answer)  
        



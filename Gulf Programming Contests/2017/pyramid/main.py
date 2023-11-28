def calculate(map):

    changed=False
    
    for i in range(len(map)-1):
        for j in range(len(map[i])):
            if map[i][j]=="-" and map[i+1][j+1]!="-" and map[i+1][j]!="-":
                map[i][j]= map[i+1][j]+map[i+1][j+1]
                changed=True
    
    
    for i in range(len(map)-1,0,-1):
        for j in range(len(map[i])-1):
            if map[i][j]=="-" and map[i][j+1]!="-" and map[i-1][j]!="-":
                map[i][j]= map[i-1][j]-map[i][j+1]
                changed=True
        
        for j in range(1,len(map[i])):
            if map[i][j]=="-" and map[i-1][j-1]!="-" and map[i][j-1]!="-":
                map[i][j]= map[i-1][j-1]-map[i][j-1]
                changed=True
        
        
    if changed:
        calculate(map)
    
    return
lines=[]

with open("pyramid.in","r") as file:
    for line in file:
        lines.append(line.strip().split())


counter=0
map=[]
testcase=1
text=""
for i in range(len(lines)):
    if lines[i][0]=="-1":
        break
    if i == counter:
        height= int(lines[i][0])
        counter+=height+1
        for j in range(i+1,counter):
            map.append(lines[j])
            
        for k in range(len(map)):
            for z in range(len(map[k])):
                try:
                    map[k][z]=int(map[k][z])
                except:
                    a=5
      
        if testcase==20:
            print(map)                    
        
        calculate(map)
       
            
        
        if map[0][0]!="-":
            print(testcase,". ",map[0][0])
            text+=str(testcase)+": "+str(map[0][0])
        else:
            print(testcase,". not solvable")
            text+=str(testcase)+": Not solvable"
        
        text+="\n"
        testcase+=1
        
        map=[]

with open("pyramid.answer","w")as file:
    file.write(text)
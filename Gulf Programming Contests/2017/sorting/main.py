def bubble(index,people):
    check=True
    positive= index==abs(index)

    for i in range(len(people)):
        for j in range(len(people)):
            if i==j:
                continue
            if positive:
                if people[i][abs(index)]<people[j][abs(index)]:
                    temp=people[i]
                    people[i]=people[j]
                    people[j]=temp
            else:
                if people[i][abs(index)]>people[j][abs(index)]:
                    temp=people[i]
                    people[i]=people[j]
                    people[j]=temp
                
    
def calculate(c,r,k,people,instructions):
  

    for i in range(len(instructions)):
        for j in range(len(instructions[i])):
            
         
            if instructions[i][j]==abs(instructions[i][j]):
                instructions[i][j]-=1
            else:
                instructions[i][j]+=1
    
    text=""
    num=1
    people_base=people.copy()
    
    for instruction in instructions:
        [2 -3]
        i=len(instruction)-1
        people=people_base
        while i >=0:
            if abs(instruction[i])<=c-1:
                bubble(instruction[i],people)
            i-=1
        print(people)
        text+="Instruction "+str(num)+"\n"
        num+=1
        for person in people:
            for i in range(len(person)):
                try:
                    person[i]=str(person[i])
                except:
                    a=5
            text+= " ".join(person)
            text+=" \n"
            
        
    print(text)    
            
            
            
    
    

    
        
    return text
lines=[]

with open("sorting.in","r") as file:
    for line in file:
        lines.append(line.strip().split())


lines.pop(0)
counter1=0
counter2=0
people=[]
instructions=[]
testcase=1
text=""
for i in range(len(lines)):
    if i == counter1:
        c, r ,k =[int(value )for value in lines[i]]
    
        counter2+=r+1
        counter1+=r+k+1
        
        for j in range(i+1,counter2):
            person=lines[j]
            for j in range(len(person)):
                if "." in person[j]:
                    try:
                        person[j]=float(person[j])
                    except:
                        a=5
            people.append(person)
        
        for j in range(counter2,counter1):
            line=[int(value) for value in lines[j]]
            line.pop(len(line)-1)
            instructions.append(line) 
        
        answer = calculate(c,r,k,people,instructions)
        people=[]
        instructions=[]
        counter2=counter1
        text+="Table "+str(testcase)+"\n"
        text+=answer

print(text)
text=text[:len(text)-1:]
with open("sorting.answer","w") as file:
    file.write(text)
# arr=[['hary', 301.0, 3.5], ['hary', 201.0, 3.6], ['mary', 105.0, 3.9], ['ali', 203.0, 4.0]]
# index=2

# bubble(-1,arr)
# print(arr)
# bubble(0,arr)
# print(arr)
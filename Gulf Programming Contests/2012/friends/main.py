def calculate(relations,querieslist):
    map={}
    for i in range(len(relations)):
        relation=relations[i]
        if relation[0] not in map:
            map[relation[0]]=[relation[1]]
        else:
            map[relation[0]].append(relation[1])
            
        if relation[1] not in map:
            map[relation[1]]=[relation[0]]
        else:
            map[relation[1]].append(relation[0])
            
    
    for key in map:
        map[key].sort()
    
 
    list=[]
    for i in range(len(querieslist)):
        answer=[]
        person1,person2=querieslist[i]
        if person1 in map and person2 in map:
            
            for j in range(len(map[person1])):
                if map[person1][j] in map[person2]:
                    answer.append(map[person1][j])
            list.append(answer)
        
    
    text=""
    for i in range(len(list)):
        text+=str(len(list[i]))
        text+=" "+" ".join(list[i])
        text+="\n"
        
    print(text)
    return text


lines=[]
with open("friends.in","r")as file:
    for line in file:
        lines.append(line.strip().split())
        
print(lines)

lines.pop(0)
counter=0
relations=[]
querieslist=[]
textasnwer=""
for i in range(len(lines)):
    if i == counter:
        connections=int(lines[i][0])
        check=counter+connections+1
        for j in range(i+1,check):
            relations.append(lines[j])
        j=check-1
        quries=int(lines[j+1][0])
        counter+=connections+quries+2
        for j in range(j+2,counter):
            querieslist.append(lines[j])
        answer = calculate(relations,querieslist)
        textasnwer+=answer


with open("firends.answer","w")as file:
    file.write(textasnwer)
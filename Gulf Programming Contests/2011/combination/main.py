def  calculate(target,coins,list,string):
   
    if target==0:

        list.append(string)
        return 1
    elif target<0 :
        return 0
    
    total=0
    for coin in coins:
        string_copy=string
        
        string_copy+=str(coin)
        target_copy=target
        target_copy-=coin
        
        
        
        total+=calculate(target_copy,coins,list,string_copy)
        
    
    return total
        
    
    


lines=[]
with open("combination.in","r") as file:
    for line in file:
        lines.append([int(value) for value in line.strip().split()])

lines.pop(0)
lines.pop(0)

counter=0
text=""
for i in range(len(lines)):
    print(i)
    print(counter)
    if i==counter:
        print("hello")
        target , num_coins= lines[i]
        
        coins=lines[i+1]
        
        counter+=2
        if num_coins>0:
            counter+=1
            
   
        list =[]
        answer = calculate(target,coins,list,"")
        temp=list.copy()
    
        for i in range(len(list)):
            for j in range(len(list)):
                value1=list[i]
                value2=list[j]
                value1=sorted(value1)
                value2=sorted(value2)
    
                if i ==j:
                    continue
                elif value1==value2 and list[i] in temp and list[j] in temp :
                    
                    temp.remove(list[j])
                    
        print(len(temp))
        text+=str(len(temp))+"\n\n"
        
        
                    
        
with open("combination.answer","w")as file:
    file.write(text)   
       
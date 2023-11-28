def calculate(num,sequance,memo):
    
    if str(num) in memo:
        min=float("inf")
        answers= memo[str(num)]
        target=" "
        for answer in answers:  
       
            if len(answer)<min:
                min =len(answer)
                for i in range(len(answer)):
                    answer[i]=str(answer[i])
    
      
                target= " ".join(answer)
  
            elif len(answer)==min:
           
                check= target.split(" ")
            
                for i in range(len(check)):
                    check[i]=int(check[i])

                if answer<check:
             
                    for i in range(len(answer)):
                        answer[i]=str(answer[i])
                    target= " ".join(answer)
    
        return target
    
    
    
    if len(sequance)>0:
        if sequance[len(sequance)-1]== num:
            return str(sequance[len(sequance)-1])
        else:
            while sequance[len(sequance)-1]<num:
                sequance.append(sequance[len(sequance)-1]+len(sequance)+1)
    
    
    for i in range(len(sequance)):
        if sequance[i]>=num:
    
            new_sequanc=sequance[:i+1:]
            
    answers=[]     
    
    for i in range(len(new_sequanc)):
    
        if new_sequanc[i]==num:
            if num not in memo:
                memo[str(num)]=[[new_sequanc[i]]]
            else:
                memo[str(num)].append([new_sequanc[i]])
            return str(new_sequanc[i])
            answers.append([new_sequanc[i]])

        else:
            left=0
            right= len(new_sequanc)-1
            while left<=right:

                if new_sequanc[i]+new_sequanc[left]==num:
                    #return str(new_sequanc[i])+" "+str(new_sequanc[left])
                    answers.append([new_sequanc[i],new_sequanc[left]])
                    if num not in memo:
                        memo[str(num)]=[[new_sequanc[i],new_sequanc[left]]]
                    else:
                        memo[str(num)].append([new_sequanc[i],new_sequanc[left]])
                    break
                elif new_sequanc[i]+new_sequanc[right]==num:
                    #return str(new_sequanc[i])+" "+str(new_sequanc[right])
                    answers.append([new_sequanc[i],new_sequanc[right]])
                    if num not in memo:
                        memo[str(num)]=[[new_sequanc[i],new_sequanc[right]]]
                    else:
                        memo[str(num)].append([new_sequanc[i],new_sequanc[right]])
                    break
                else:
                    if new_sequanc[i]+new_sequanc[left]+new_sequanc[right]>num:
                        right-=1
                    elif new_sequanc[i]+new_sequanc[left]+new_sequanc[right]<num:
                        left+=1
                    else:
                        # return str(new_sequanc[i])+" "+str(new_sequanc[left])+" "+str(new_sequanc[right])
                        answers.append([new_sequanc[i],new_sequanc[left],new_sequanc[right]])
                        if num not in memo:
                            memo[str(num)]=[[new_sequanc[i],new_sequanc[left],new_sequanc[right]]]
                        else:
                            memo[str(num)].append([new_sequanc[i],new_sequanc[left],new_sequanc[right]])
                        break


    min=float("inf")
    
    target=" "
    for answer in answers:  
       
        if len(answer)<min:
            min =len(answer)
            for i in range(len(answer)):
                answer[i]=str(answer[i])
    
      
            target= " ".join(answer)
  
        elif len(answer)==min:
           
            check= target.split(" ")
            
            for i in range(len(check)):
                check[i]=int(check[i])

            if answer<check:
             
                for i in range(len(answer)):
                    answer[i]=str(answer[i])
                target= " ".join(answer)
         
            
    
    return target
    


lines=[]
with open("tri.in","r")as file:
    for line in file:
        lines.append([int(value) for value in line.strip().split()])

lines.pop(0)

# test=[10,19,16,17,48,49]
# 
# for case in test:
#     answer= calculate(case,sequance)
    



sequance=[1]

text=""
testcase=1
memo={"1":[[1,2],[3,3,4]]}

for line in lines:
    answer = calculate(line[0],sequance,memo)
    text+= str(testcase)+". "+str(answer)+"\n"
    print(str(testcase)+". "+str(answer)+"\n")
    
    testcase+=1
with open("tri.answer","w")as file:
    file.write(text)
def calculate(countries):
   
  
    for i in range(len(countries)):
         countries[i].pop(0)
    min_list =countries[0]
    
    for i in range(1,len(countries)):
       
        if len(countries[i])<len(min_list):
            min_list=countries[i]
    
    answer =""
    for i in range(len(min_list)):
        check=True
        for j in range(len(countries)):
            if min_list[i] not in countries[j]:
                check=False
                break
        if check:
            answer+=str(min_list[i])+","
           
    if not answer:
        return "No Trip"
    
    
    answer = answer[:-1:]
    
    answers= answer.split(",")
    
    for i in range(len(answers)):

        answers[i]=int(answers[i])
    answers.sort()
    for i in range(len(answers)):
        answers[i]=str(answers[i])
    answer=",".join(answers)
            
  
            
    if answer:
        return answer
  
        


with open("trip.answer","w"):
    pass

lines=[]

with open("trip.in","r")as file:
    for line in file:
        values = [int (value) for value in line.strip().split()]
        lines.append(values)


lines.pop(0)
counter=0

countries=[]
testcase=1
for i in range(len(lines)):
    if i ==counter:
        counter +=lines[i][0]+1
        count= lines[i][0]
        
        for j in range(i+1,i+count+1):
            country= lines[j]
            countries.append(country)
        answer = calculate(countries)

        with open("trip.answer","a") as file:
            file.write(str(testcase)+". "+str(answer)+"\n")
            testcase+=1
        countries=[]
      
            


lines=[]

with open("digits.in","r") as file:
    for line in file:
        lines.append([int(value) for value in line.strip().split()])
        
lines.pop(0)
map={
    "0":"Zero",
     "1":"One",
      "2":"Two",
       "3":"Three",
        "4":"Four",
         "5":"Five",
          "6":"Six",
           "7":"Seven",
            "8":"Eight",
             "9":"Nine",
              
}

testcase=1
textanswer=""
for line in lines:
    number=str(line[0])
    
    answer=""
    for n in number:
        answer+=map[n]
    
   
    answer = len(answer)
   
    text=str(testcase)+". "+str(answer)+"\n"
    print(text)
    textanswer+=text
    testcase+=1


with open("digits.answer","w")as file:
    file.write(textanswer)
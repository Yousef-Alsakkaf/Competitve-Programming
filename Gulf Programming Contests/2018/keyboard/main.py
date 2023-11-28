def calculate(mode,moves):

    map=[["1","2","3"],["4","5","6"],["7","8","9"],[None,"0",None]]
    
    map_moves={
        "0":{
            "D":[1,0],
            "U":[-1,0],
            "L":[0,-1],
            "R":[0,1],
            
            },
         "1":{
            "D":[0,1],
            "U":[0,-1],
            "L":[1,0],
            "R":[-1,0],
            
            },
          "2":{
            "D":[-1,0],
            "U":[1,0],
            "L":[0,1],
            "R":[0,-1],
            
            },
           "3":{
                "D":[0,-1],
                "U":[0,1],
                "L":[-1,0],
                "R":[1,0],
            
            }
    }
    
    
    print(moves)
    textAnswer=""
    for case in moves:
        i=1
        j=1
        answer =""
        for  move in case[0]:

            #as long as the move is not the ok button move the cursor which is i and j
            if move!="K":
                di , dj = map_moves[mode][move]
                i +=di
                j+=dj
                
                if i >3:
                    i=3
                if i<0:
                    i=0
                if j>2:
                    j=2
                if j<0:
                    j=0
                

            else:
                
                #check the point that has been pressed and skip if it is * or #
                if map[i][j]:
                    answer +=map[i][j]
        textAnswer+=answer+"\n"
        print("new test case has been added not the final answer is ",textAnswer," for the case ",case)
    return textAnswer

with open("keyboard.answer","w"):
    pass


lines=[]

with open("keyboard.in","r") as file:
    for line in file:
        values = line.strip().split()
        lines.append(values)
        


lines.pop(0)
counter =0
testcases=0
testcase=1

moves=[]
for i in range(len(lines)):
    if i ==counter:
        #new test case
        mode ="0"
        if int(lines[i][0])==0:
            mode="0"#normal
        elif int(lines[i][0])==90:
            mode="1"#rotated to the right
        elif int(lines[i][0])==180:
            mode="2"#rotated down
        elif int(lines[i][0])==270:
            mode="3"#rotated to the left
        testcases= int(lines[i][1])
        counter+=testcases+1
        for j in range(i+1,counter):
            moves.append(lines[j])
        answer = calculate(mode,moves)
        print(answer)
        textAnswer = str(testcase)+"\n"+ str(answer)
        with open("keyboard.answer","a")as file:
            file.write(textAnswer)
        print(textAnswer)
        
        testcase+=1
        moves=[]
        
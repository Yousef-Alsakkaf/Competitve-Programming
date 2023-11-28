def calculate(length,map_horizontal,map_vertical):
    #this stores the number of squares from each length
    squares= [0 for i in range(length-1)]

    
    map = [[0 for i in range(length)]for j in range(length)]
    # print(len(map))
    #this for loop is counting for each size square
    for n in range(1,length):
        # print(n)
        for i in range(len(map)-n):
           for j in range(len(map[i])-n):
                # print("for the point (",i,j,") of the square ",n)
                #add the points of the horzintal lines
                check=True
                for k in range(j,j+n):
                    if map_horizontal[i][k] != 1:
                        # print("the point (",i,k,") in the horzontal is 0")
                        # print("")
                        check=False
                        break
                    if map_horizontal[i+n][k] != 1:
                        # print("the point (",i+n,k,") in the horzontal is 0")
                        # print("")
                        check=False
                        break
                for k in range(i,i+n):
                    if map_vertical[k][j]!=1:
                        # print("the point (",k,j,") in the vertical is 0")
                        # print("")
                        check=False
                        break
                    if map_vertical[k][j+n]!=1:
                        # print("the point (",k,j+n,") in the vertical is 0")
                        # print("")
                        check=False
                        break
                if check:
                    squares[n-1]+=1
 
                    
                
               
        
    return squares

with open("square.answer","w"):
    pass

lines=[]
with open("square.in","r") as file:
    for line in file:
        values = [int(value) for value in line.strip().split()]
        lines.append(values)

counter=0
map_horizontal=[]
map_vertical= []

testcase = 1
for i in range(len(lines)):
    if len(lines[i])==1:
        if lines[i][0]==0:
            #terminate
            break
        else:
            #new test case
            length= lines[i][0]
            counter =length
    else:
        #store the varibales
        if counter !=0:
            map_horizontal.append(lines[i])
            counter-=1
        else:
            map_vertical.append(lines[i])
            if len(lines[i+1])==1:
                #end of test case start calcuclating
                answer = calculate(length,map_horizontal,map_vertical)
                textAnswer = "Case "+str(testcase)+"\n"
                for i in range(len(answer)):
                    if answer[i]!=0:
                        textAnswer+=str(i+1)+": "+str(answer[i])+"\n"
                
                textAnswer+="\n"
                print(textAnswer)
                with open("square.answer","a")as file:
                    file.write(textAnswer)
                testcase+=2
                map_horizontal=[]
                map_vertical=[]
                
                
                
          
               
        
            
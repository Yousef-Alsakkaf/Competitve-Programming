def decode(line):
    list=[]
    sentence= line[0]

    #since all the charcters are stroed as strings there is no way for the program to know if it faces
    #a number or a charecter. so in this for loop we change the numbers to intgers
    for char in sentence:
        try:
            #try to change the type to number to determain the parts of the string
            number=int(char)
            list.append(number)
          
        except:
            #if it came here that means the char is not a number
            list.append(char)
      
    
    #initalize a temp record
    temp=""
    
    #initlize a starting record
    start=""
    
    #initalize an ending record
    end =""
    
    ##the plan here is to add any charecter to the temp untill we hit a number
    ## if we hit a number decide what to do with the temp whenter to add it to the start
    ## or to the end
    for element in list:
        if type(element)==str:
            temp+=element
        elif type(element)==int:
            if element%2==0:
                start=temp+start
                temp=""
            elif element%2==1:
                end=end+temp
                temp=""
                
    finish_sentence=start+end
    return finish_sentence


##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################

with open('secret.answer', 'w') as file:
    pass
path = "secret.in"
lines=[]
with open(path,"r") as file:
     # Iterate through the lines in the file
    for line in file:
        # Strip newline characters and split the line into a list of values
        line_values = line.strip().split()
        
        # Append the list of values to the 'lines' list
        lines.append(line_values)
#remove the first line
lines.pop(0)

testcase=1
for line in lines:
    answer=decode(line)
    with open('secret.answer', 'a') as file:
        # Write the new line to the file
        file.write(str(testcase)+". "+str(answer)+"\n")
    testcase+=1
   
def calculate(line):
    #the idea here is just to get how many days will be spend so its simple devision
    answer= line[0]//line[1]
   
    return answer
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################

with open('diapers.answer', 'w') as file:
    pass

path = "diapers.in"
lines=[]
with open(path,"r") as file:
     # Iterate through the lines in the file
    for line in file:
        # Strip newline characters and split the line into a list of values
        line_values = line.strip().split()
        
         # Convert the values to integers and append to the 'lines' list
        line_values = [int(value) for value in line_values]
        lines.append(line_values)
        
testcase=1
#format
for i in range(1,len(lines)):
    line = lines[i]
    
    answer=calculate(line)
    with open('diapers.answer', 'a') as file:
        # Write the new line to the file
        file.write(str(testcase)+". "+str(answer)+"\n")
        testcase+=1
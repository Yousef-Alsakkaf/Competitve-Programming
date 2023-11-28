def calculate(numSocks,lineSocks):
    ##check if there is a sock that has more than 1pair
    ##if it doesnt exist then its imposible
    ##else the min is the diffrent color of socks +1
    for sock in lineSocks:
        if sock >1:
            return numSocks+1
    
    return "Impossible"

##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################

with open('socks.answer', 'w') as file:
    pass
path = "socks.in"
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
for i in range(1,len(lines),2):
    lineNumSocks= lines[i]
    numSocks=lineNumSocks[0]
    lineSocks=lines[i+1]
    answer=calculate(numSocks,lineSocks)
    with open('socks.answer', 'a') as file:
        file.write(str(testcase)+". "+str(answer)+"\n")
        testcase+=1   
    
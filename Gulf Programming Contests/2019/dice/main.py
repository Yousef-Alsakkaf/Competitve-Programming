def calculate(attacker,defender):
    #finding the amout of time that they would fight which is the minimum
    length1= len(attacker)
    length2=len(defender)
    minimum= min([length1,length2])
    
    #initalize scores
    sattacker=0
    sdefender=0
    
    #the approach here  is to sort the lists and let them fight to the maximum amount of times that they can which is the minmum length of the two list
    #and count the winner in each round
    attacker.sort(reverse=True)
    defender.sort(reverse=True)
    
    for i in range(minimum):

        if attacker[i]>defender[i]:
            sdefender+=1
        else:
            sattacker+=1
    return str(sattacker)+" "+str(sdefender)


##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################

with open('dice.answer', 'w') as file:
    pass


path = "dice.in"
lines=[]
with open(path,"r") as file:
     # Iterate through the lines in the file
    for line in file:
        # Strip newline characters and split the line into a list of values
        line_values = line.strip().split()
        
         # Convert the values to integers and append to the 'lines' list
        line_values = [int(value) for value in line_values]
        lines.append(line_values)

#delete the first line 
lines.pop(0)

testcase=1
for i in range(0,len(lines),3):
    variables= lines[i]
    attacker= lines[i+1]
    defender= lines[i+2]
    answer = calculate(attacker,defender)
    with open('dice.answer', 'a') as file:
        # Write the new line to the file
        file.write(str(testcase)+". "+ str(answer)+"\n")
        testcase+=1
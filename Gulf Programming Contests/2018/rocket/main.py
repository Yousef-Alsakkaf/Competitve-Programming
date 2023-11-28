def calculate(num,list):
    #the trick here to save a bit of time is to calculate only half the sequance 45 
    # excluding the target number then multiply it by 2 and addin the target number
    #because we didnt calculate it before
    g=1
    
    maxCalculated = list[len(list)-1]
    for i in range(maxCalculated+3,num,3):
        g+=i
    
    g=g*2+num

    return g

##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################

with open('rocket.answer', 'w') as file:
    pass
path = "rocket.in"
lines=[]
with open(path,"r") as file:
     # Iterate through the lines in the file
    for line in file:
        # Strip newline characters and split the line into a list of values
        line_values = line.strip().split()
        
         # Convert the values to integers and append to the 'lines' list
        line_values = [int(value) for value in line_values]
        lines.append(line_values)


#format
for line in lines:
    if(line[0]==0):
        break
    list=[1]
    
    answer = calculate(line[0],list)
    with open('rocket.answer', 'a') as file:
        file.write(str(answer)+"\n")



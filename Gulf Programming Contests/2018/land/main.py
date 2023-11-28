def getIndex(num1,num2):
    return (num1+num2)%3

def calculate(square,horizantal,vertical):
    #initlize the size of the lands for each princes
    size0=0#blue
    size1=0#green
    size2=0#red
    for i in range(len(vertical)):
        for j in range(len(horizantal)):
            if getIndex(i,j) ==0:
                size0+=vertical[i]*horizantal[j]
            elif getIndex(i,j) ==1:
                size1+=vertical[i]*horizantal[j]
            elif getIndex(i,j) ==2:
                size2+=vertical[i]*horizantal[j]
 
    return str(size0)+" "+str(size2)+" "+str(size1)


##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################

with open('land.answer', 'w') as file:
    pass
path = "land.in"
lines=[]
with open(path,"r") as file:
     # Iterate through the lines in the file
    for line in file:
        # Strip newline characters and split the line into a list of values
        line_values = line.strip().split()
        
         # Convert the values to integers and append to the 'lines' list
        line_values = [int(value) for value in line_values]
        lines.append(line_values)

counter=0

for i in range(len(lines)):
    if lines[i][0]==0:
        print(lines[0])
        #terminate
        break
    if i ==counter:
        #start new testcase
        square= lines[i][0]
        horizantal= lines[i+1]
        vertical= lines[i+2]
        answer= calculate(square,horizantal,vertical)
        with open('land.answer', 'a') as file:
            file.write(str(answer)+"\n")
        counter+=3
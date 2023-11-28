def findrepeat(listnum):
    unique={}
    for num in listnum:
        if num not in unique:
            #store the unique value
            unique[num]=1
            
        else:
            unique[num]+=1
                    
   
    return unique

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################

with open('photo.answer', 'w') as file:
    pass

path = "photo.in"
lines=[]
with open(path,"r") as file:
     # Iterate through the lines in the file
    for line in file:
        # Strip newline characters and split the line into a list of values
        line_values = line.strip().split()
        
         # Convert the values to integers and append to the 'lines' list
        line_values = [int(value) for value in line_values]
        lines.append(line_values)
        
testcase=1            #answer
            
                
        
#formating
for i in range(1,len(lines)):
    line = lines[i][1::]
    line.sort()

    #retrun a list of objects of the similar numbers. each the value that a certian number is repeated
    final = findrepeat(line)
    print(testcase, final)
    keys= list(final.keys())
    total=1
    for key in keys:
        total*=factorial(final[key])
    with open('photo.answer', 'a') as file:
        # Write the new line to the file
        file.write(str(testcase)+". "+str(total)+"\n")
        testcase+=1
def transform(num,base):
    final=[]
    if num==0:
        return "0"
    
    while num!=0:
        value=num%base
        final.append(value)
        num=num//base
        
    return final
def check(str):
    if str==str[::-1]:
        return "yes"
    else:
        return "no"
    
    
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################

with open('palindrome.answer', 'w') as file:
    pass

path = "palindrome.in"
lines=[]
with open(path,"r") as file:
     # Iterate through the lines in the file
    for line in file:
        # Strip newline characters and split the line into a list of values
        line_values = line.strip().split()
        
         # Convert the values to integers and append to the 'lines' list
        line_values = [int(value) for value in line_values]
        lines.append(line_values)



#formating
testcase=1
for line in lines:
    
    num=line[0]
    base=line[1]
    
    #perform check
    final=transform(num,base)
    
    #check palindrom
    answer= check(final)
    #answer
    with open('palindrome.answer', 'a') as file:
        # Write the new line to the file
        file.write(str(answer)+"\n")
        
    testcase+=1
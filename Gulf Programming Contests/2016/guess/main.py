def calculate(unknown,tries):
    #we have 3 cases that we should consider as edge cases
    
    #the first is if she gave all here number
    #in this case the percatage should immedatly be 100.00%
    if unknown==0 and tries !=0:
        return 100.00
    
    
    combinations= 1/(10)**unknown
    
    percentage= combinations*tries
    
    percentage= float(percentage*100)
     #the second is if the percatage when we get it. if it exceeds 100% it should retrun 100%
    if percentage>100:
        return 100.00
    
    
    return percentage



with open('guess.answer', 'w') as file:
    pass
file_path = 'guess.in'

# Initialize an empty list to store the lines
lines = []

# Open the file for reading
with open(file_path, 'r') as file:
    # Iterate through the lines in the file
    for line in file:
        # Strip newline characters and split the line into a list of values
        line_values = [int(value) for value in line.strip().split()]
        
        # Append the list of values to the 'lines' list
        lines.append(line_values)


testcase=1
for i in range(1,len(lines)):
    line=lines[i]
    unknown= line[0]-line[1]
    tries= line[2]
    answer = calculate(unknown,tries)  
    formatted_answer = "{:.2f}".format(answer)
    with open('guess.answer', 'a') as file:
        file.write(str(testcase)+". "+str(formatted_answer)+"%\n")
        testcase+=1
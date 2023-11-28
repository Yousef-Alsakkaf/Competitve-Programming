
def calculate(base):
    #the trick here is the understand the charactarstic of pisano
    #in the pisano sequance the 0 and 1 that are at the start of the sequance 
    #are never repeated unless the full sequance is being repeated
    
    #so the idea is to find when will the 0 and 1 being repeated instead of considering the whole sequance
    a, b = 0, 1
    period = 0
    while True:
        a, b = b, (a + b) % base

        period += 1
        if a == 0 and b == 1:
            return period
        
        
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################

with open('pisano.answer', 'w') as file:
    pass

file_path = 'pisano.in'

# Initialize an empty list to store the 1lines
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
for line in lines:
    if line[0]==0:
        break
    else:
        answer = calculate(line[0])
        with open('pisano.answer', 'a') as file:
            file.write(str(answer)+"\n")
            testcase+=1
    
        
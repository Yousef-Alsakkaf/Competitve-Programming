
with open('league.answer', 'w') as file:
    pass
file_path = 'league.in'

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



max=-1
incorrect=0
testcase=1
#the trick here is to find the relationship between the number of teams and the number of matches
#which is matchs=teams-1
for i in range(1,len(lines)):
    num_of_teams=lines[i][0]
    answer = num_of_teams-1
    with open('league.answer', 'a') as file:
        # Write the new line to the file
        file.write(str(testcase)+". "+str(answer)+"\n")
    
    testcase+=1
 

#this function is just makeing a binary string out of a number
def binary(num):
    bina=""
    if num==0:
        bina+="0"
    while num!=0:
        value = num%2
         
        bina += str(value)  # Convert the remainder to a string and add to the result
        num //= 2  # Update num by performing integer division
    
    
    reversed_bina = bina[::-1]

    return reversed_bina

#this function is returning the number of diffrent charcters in the 2 strings
def diffrance(s1,s2):
    diffrent=0
    for i in range(len(s1)):
        
        if s1[i]!=s2[i]:
          
            diffrent+=1
    return diffrent

#this function is switching the chrecters of a string to ones or zeros depending on the condition
def create(s1,con):
    s=""
    if(con=="set"):
        for i in range(len(s1)):
            s+="1"
    elif(con=="reset"):
        for i in range(len(s1)):
             s+="0"
    
    
    return s

#this function is finding the minimum of 3 integers
def findMin(num1,num2,num3):
    min=num1
   
    if(num2<min):
        min=num2+1
    if(num3<min):
        min=num3+1
    return min    


#this function is completing the string with zeros untill it reaches 24
def complete(s1):
    diffrance= 24-len(s1)
    completion=""
    for i in range(diffrance):
        completion+="0"
    s1=completion+s1
    return s1









##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################

with open('biplay.answer', 'w') as file:
    pass


# Specify the file path
file_path = 'biplay.in'

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
#formating
for i in range(len(lines)):
    if lines[i][0]==0 and  lines[i][1]==0:
        break
    q=lines[i]
    
    num1=q[0]
    num2=q[1]
    if(num1==num2):
        
        with open('biplay.answer', 'a') as file:
            new_line = str(testcase)+". "+ str(0)
            new_line += '\n'  # Add a newline character at the end
            
            # Write the new line to the file
            file.write(new_line)
        testcase+=1
        continue
    #switch the numbers to binary strings
    bnum1= binary(num1)
    bnum2= binary(num2)

    #complete the numbers if they are not
    bnum1=complete(bnum1)
    bnum2=complete(bnum2)
    
    #create the string zeros and one
    setn= create(bnum2,"set")
    resetn= create(bnum2,"reset")


    #the idea is that you only have 3 convinant paths to go to
    
    #1 just filp all the numbers that are diffrent
    #2 make zeros and filp all the numbers that are diffrent
    #3 make ones filp all the numbers that are diffrent
    
    # the best solution will be the minimum moves of these 3 approaches
    # Open the file in append mode ('a' mode)
    print(findMin(diffrance(bnum1,bnum2), diffrance(bnum2, setn), diffrance(bnum2, resetn)))
    with open('biplay.answer', 'a') as file:
        new_line = str(testcase)+". "+ str(findMin(diffrance(bnum1,bnum2), diffrance(bnum2, setn), diffrance(bnum2, resetn)))
        new_line += '\n'  # Add a newline character at the end
        
        # Write the new line to the file
        file.write(new_line)
    testcase+=1
    
    
    
    
       
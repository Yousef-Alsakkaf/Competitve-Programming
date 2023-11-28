def calculate(numbers):
    changed=False
    state=True#treu means increase false means decrese
    num_of_changes=0
    
    #the idea now is to find the first change that happened to the sequance
    #so we loop over the numbers and find the first change that happens
    index=0
    while not changed:

        if numbers[index]<numbers[index+1]:
            state=True#first chang is increasing


            changed=True
        elif numbers[index]>numbers[index+1]:
            state=False#first change is decreasing

            changed=True
        index+=1
    

        
    #now loop over the all the numbers
    for i in range(0,len(numbers)-1):

        if state: 
            #check if it has changed
            if numbers[i]>numbers[i+1]:
    
                state=False#decrese
                num_of_changes+=1
            
        else:
            #check if it has changed
            if numbers[i]<numbers[i+1]:

                state=True#increase
                num_of_changes+=1
            
        
    if num_of_changes==0:
        return "mono"
    elif num_of_changes==1:
        return "bi"
    else:
        return "poly"
    
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################

with open('sequence.answer', 'w') as file:
    pass
file_path = 'sequence.in'

# Initialize an empty list to store the lines
lines = []
testcase=1
# Open the file for reading
with open(file_path, 'r') as file:
    # Iterate through the lines in the file
    check=True
    counter=0
    numbers=[]
    for line in file:
        number= line.strip().split()
        for i in range(len(number)):
            if check :
                #new test case
                counter= int(number[i])
           
                check=False
            elif number[i]!=" ":
                #take the numbers
                numbers.append(int (number[i]))
                if len(numbers)==counter:

                    #start calculating
                    answer = calculate(numbers)
                    with open('sequence.answer', 'a') as file:
                        # Write the new line to the file
                        file.write(str(testcase)+" "+str(answer)+"\n")
                        testcase+=1
                    numbers=[]
                    counter=0
                    check=True
         
        
        


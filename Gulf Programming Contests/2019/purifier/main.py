def calculate(t1,t2):
    #spliting the numbers between :
    time1=t1.split(":")
    
    #transforming the time to munites
    hour1=int(time1[0])*60
    muinte1=int(time1[1])
    total1=hour1+muinte1
    
    
    #spliting the numbers between :
    time2=t2.split(":")
    
    #transforming the time to munites
    hour2=int(time2[0])*60
    muinte2=int(time2[1])
    total2=hour2+muinte2
    
    #find the busy time in munites
    busy=total2-total1
    
    return busy


##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################
##################################   main   ########################################

with open('purifier.answer', 'w') as file:
    pass

path = "purifier.in"
lines=[]
with open(path,"r") as file:
     # Iterate through the lines in the file
    for line in file:
        # Strip newline characters and split the line into a list of values
        line_values = line.strip().split()
        
        # Append the list of values to the 'lines' list
        lines.append(line_values)

counter=1#the pointer of a new testcase
days=0
neededhours=0
totalbusymin=0
testcase=0


#formatting
for i in range(len(lines)):
    #skip the firstline
    if i==0:
        continue
    #start of a testcase
    if i ==counter:
        testcase+=1#count how many testcases have been done
        
        counter+=int(lines[i][1])+1#set the value of the pointer to the new testcase
        
        days=int(lines[i][1])

        neededhours=int(lines[i][0])
    else:

        #add 14 hours if the day is a holiday
        if lines[i][0]!="-" :
            for time in lines[i]:
                single=time.split("-")  
                totalbusymin+=calculate(single[0],single[1])
        totalbusymin+=10*60    
        #if last day to calculate

        if i+1==counter:
            #end of a test case start calculating
            #get last varibales
            neededmin=neededhours*60
            freemin=(days*24*60)-totalbusymin
            

            #answer
            with open('purifier.answer', 'a') as file:
                # Write the new line to the file
                if freemin>=neededmin:
                    file.write(str(testcase)+". Yes\n")
                else:
                    file.write(str(testcase)+". No\n")
               
                
                
           
            



            ##reset all counters
            days=0
            neededhours=0
            totalbusymin=0
            
            
            
            
    
        
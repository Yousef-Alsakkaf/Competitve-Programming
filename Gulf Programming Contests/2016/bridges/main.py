def calculate(people):
   
    tracks={"max":0,
            "count":0}
    time=0
    max=0
    while people or tracks["count"]:

        if time in people:
            for person in people[time]:
                finish_time=person[0]+person[1]
                
                if finish_time not in tracks:
                    tracks[finish_time]=[]
                    
                tracks[finish_time].append(person)
                
                tracks["count"]+=1
                if tracks["max"]<tracks["count"]:
                    tracks["max"]=tracks["count"]
            del people[time]    

        if time in tracks:
            count= len(tracks[time])
            tracks["count"]-=count
            tracks[time]=[]
        
        time+=1
        
        

    return tracks["max"]

with open("bridges.answer","w"):
    pass
file_path = 'bridges.in'

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
counter= 1
people={}
if not people:
    print("hello")
for i in range(1,len(lines)):
    if i ==counter:

        counter+=lines[i][0]+1

        for j in range(i+1,i+lines[i][0]+1):
            
            if lines[j][0] not in people:
                people[lines[j][0]]=[]
                people[lines[j][0]].append(lines[j])
            else:
                people[lines[j][0]].append(lines[j])

        answer= calculate(people)

        with open("bridges.answer","a")as file:
            file.write(str(testcase)+". "+str(answer)+"\n")
        people={}
        testcase+=1
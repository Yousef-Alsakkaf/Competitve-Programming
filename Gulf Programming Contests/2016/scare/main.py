
def calculate(current_gpa,target_gpa,current_credit,remaining_courses):
    map={
        "A":4,
        "A-":3.7,
        "B+":3.3,
        "B":3,
        "B-":2.7,
        "C+":2.4,
        "C":2,
        "C-":1.7,
    }
    remaining_courses=int(remaining_courses)
    array=["A" for i in range(remaining_courses)]
    asked_gpa= ((target_gpa*(remaining_courses*3+current_credit))-(current_credit*current_gpa))/(remaining_courses*3)
    
    
    less=False
    if current_gpa>target_gpa:
        less=True
    
    array=array[::-1]
    
    found=False
    last=False
    temp=[]
    for key in map:
        for i in range(len(array)):
            total=0
            for j in range(len(array)):
                total+=map[array[j]]
            total=total/len(array)

            if(total<=asked_gpa) and asked_gpa<=4:
                print("found") 
                if i ==len(array):
                    last=True
                found=True
                break
            else:
                temp= array.copy()
                array[i]=key

        if found:
            break 
    
    if last:
        temp=array
    
    if less and not found:
        
        temp=""
        for i in range(remaining_courses):
            temp+= "C- "
        return temp
    temp=temp[::-1]
    
    
    answer = ""
    for courses in temp:
        answer+=str(courses)+" "
        
    if found:

        return answer
    else:
 
        return "Target GPA unattainable"


with open("scare.answer","w"):
    pass
file_path = 'scare.in'

# Initialize an empty list to store the lines
lines = []

# Open the file for reading
with open(file_path, 'r') as file:
    # Iterate through the lines in the file
    for line in file:
        # Strip newline characters and split the line into a list of values
        line_values = [float(value) for value in line.strip().split()]
        
        # Append the list of values to the 'lines' list
        lines.append(line_values)


for i in range(1,len(lines)):
    answer = calculate(lines[i][0],lines[i][1],lines[i][2],lines[i][3])
    print
    with open("scare.answer","a") as file:
        file.write(str(answer)+'\n')
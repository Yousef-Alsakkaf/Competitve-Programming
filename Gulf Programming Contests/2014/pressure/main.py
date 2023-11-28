import math
def distance(x1,x2,y1,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


def calculate(people_x,people_y,sensor_x,sensor_y,x,y,avarage_weight,range,num_of_people,num_of_sensors):

    people=[]
    sensors=[]
    num_of_sensors=int(num_of_sensors)
    num_of_people=int(num_of_people)
    i = 0
    j = 0
   
    

    while i < int(num_of_people):

        person = [people_x[i], people_y[i]]
        people.append(person)
        i += 1

    while j < int(num_of_sensors):
        
 
        sensor = [sensor_x[j], sensor_y[j]]
        sensors.append(sensor)
        j += 1
   
    total_weight=[]
    for sensor in sensors:
        total=0
        for person in people:
            if distance(sensor[0],person[0],sensor[1],person[1])<=range:
                total+=avarage_weight
        total_weight.append(str(int(total)))


    answer = " ".join(total_weight)
    return answer
        
lines=[]
with open("pressure.in","r")as file:
    for line in file:
        values = [float(value) for  value in line.strip().split()]
        lines.append(values)
        
        
        
text=""

counter=0
people_x=[]
people_y=[]
sensor_x=[]
sensor_y=[]
for i in range(len(lines)+1):
    if i==len(lines):
        answer = calculate(people_x,people_y,sensor_x,sensor_y,x,y,avarage_weight,range,num_of_people,num_of_sensors)
        print(answer)
        people_x=[]
        people_y=[]
        sensor_x=[]
        sensor_y=[]
        text+=answer+"\n"
        
    elif len(lines[i])==0:
        answer = calculate(people_x,people_y,sensor_x,sensor_y,x,y,avarage_weight,range,num_of_people,num_of_sensors)
        people_x=[]
        people_y=[]
        sensor_x=[]
        sensor_y=[]
        text+=answer+"\n"
        print(answer)
        
    elif i==counter:
        check=0
        x,y,avarage_weight,range,num_of_people,num_of_sensors=lines[i]
        if num_of_sensors>0:
            check+=2
            sensor_x=lines[i+1]
            sensor_y=lines[i+2]
            if num_of_people>0:
                people_x=lines[i+3]
                people_y=lines[i+4]
                check+=2
        elif num_of_people>0:
            people_x=lines[i+1]
            people_y=lines[i+2]
            check+=2
        
        counter += check+2
            
        
        
    
        


with open("pressure.answer","w")as file:
    file.write(text)
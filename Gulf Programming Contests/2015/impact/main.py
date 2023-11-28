      
def calculate_intersection_area(square1, square2):
    #getting the bottom left and the top right corner cords from the square
    #x1 y1 botttom left for sqare 1 
    #x2 y2 top right for square 1
     #x3 y3 botttom left for sqare 2
    #x4 y4 top right for square 2
    x1, y1, x2, y2  = square1
    x3, y3, x4, y4  = square2


    x_distance = min(x2, x4) - max(x1, x3)
    y_distance = min(y2, y4) - max(y1, y3)
    
    #if any of them is negative they dont overlap
    if x_distance<0 or y_distance<0:
        return 0
    
    # Calculate the area of the intersection rectangle
    return x_distance * y_distance

def formatlist(list):
    for i in range(1,len(list)):
        list[i]=int(list[i])
    return list
def calculate(num_of_cities,x,y,impact_length,cityies):
    #calculating the number of unique cityes who got impacted 
    # if a city hasnt been impacted it wont be added to the hash map
    #the stucture is like this 
    # {
    #     "cityname":[numbe of reagions got effected, True or fales for if it got wiped or no]
    # }
    unique_cityies={}
    
    city_death_toll={}
    rocket_buttom_left=[x-impact_length,y+impact_length]
    rocket_top_right=[x+impact_length,y-impact_length]
    
    
    for i in range(len(cityies)):
        cityies[i]=formatlist(cityies[i])
    
    for city in cityies:

        
        city_top_left=[city[1],city[2]]
        city_buttom_left=[city_top_left[0],city_top_left[1]+city[4]]
        city_top_right=[city_top_left[0]+city[3],city_top_left[1]]
        
        #due to the unorignial format of the map i am dealing with it as it is 
        # the buttom left qurter of a grid
        # so any y point is multiplied by -1 when i pass the positions to calculate 
        area=calculate_intersection_area([city_buttom_left[0],city_buttom_left[1]*-1,city_top_right[0],city_top_right[1]*-1],[rocket_buttom_left[0],rocket_buttom_left[1]*-1,rocket_top_right[0],rocket_top_right[1]*-1])
        city_area=city[3]*city[4]
       
        death_toll= int((area/city_area)*city[5])
        if city[0] not in city_death_toll:
            city_death_toll[city[0]]=death_toll
        else:
            city_death_toll[city[0]]+=death_toll
        
       
        if area>0:
             #in case the area is bigger than zero 
            #add the city key if it doesnt exist with a defualt 1 city and true 
            #and check if it got wiped or no
            if city[0] not in unique_cityies:
                unique_cityies[city[0]]=[1,True]
                #check if it got wiped
                if area!=city_area:
                    unique_cityies[city[0]][1]=False
            #if it already exists just add a the city to the total number of citys that has been impacted
            #and check if it has been wiped or no
            else:
                unique_cityies[city[0]][0]+=1
                #check if it got wiped
                if area!=city_area:
                    unique_cityies[city[0]][1]=False
                    
        #this else is just to adjust to value of the true false statment
        #the idea is that if the city isnt impacted than it hasnt been wiped
        else:
            
            if city[0] not in unique_cityies:
                unique_cityies[city[0]]=[0,False]
                #check if it got wiped
                if area!=city_area:
                    unique_cityies[city[0]][1]=False
            else:

                #check if it got wiped
                if area!=city_area:
                    unique_cityies[city[0]][1]=False

    sorted_dict = dict(sorted(unique_cityies.items()))
    print(sorted_dict)
    print(city_death_toll)
    return [sorted_dict,city_death_toll]
with open("impact.answer ","w"):
    pass

lines=[]

with open("impact.in","r") as file:
    for line in file:
        values = line.strip().split()
        lines.append(values)
        
 
 


cityies=[]
num_of_cities=0
for line in lines:
    if len(line)==1:
        #start of a new test case 
        num_of_cities=int(line[0])

    elif len(line)==3:
        #end the test case 
        #get the rocket impact
        x= int(line[0])
        y=int(line[1])
        impact_length= int(line[2])
        
        #start calculating
        unique , death_toll = calculate(num_of_cities,x,y,impact_length,cityies)
        textanswer = ""
        for city in unique:
            textanswer+= str(city)+" "+ str(unique[city][0])+" "+str(int(death_toll[city]))+"\n"
            if unique[city][1]:
                textanswer+= str(city)+" is wiped out\n"

        with open("impact.answer","a")as file:
            file.write(textanswer)
        cityies=[]
    else:
        #get the city info
        cityies.append(line)
        
# Input coordinates for the corners of two squares as (x1, y1, x2, y2, x3, y3, x4, y4)
rectangle1 = (0, 0, 2, 2)
rectangle2 = (-1, 1, 1, 3)

intersection_area = calculate_intersection_area(rectangle1, rectangle2)
print("Area of intersection:", intersection_area)


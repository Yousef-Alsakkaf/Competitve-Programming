def find(map,i,j,value,invaded):
    # Define the relative positions of the 8 adjacent cells
    neighbors_relative_positions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    # Initialize a list to store the content of neighboring cells
    neighbor_contents = []

    # Iterate through the relative positions and check the content of neighboring cells
    for dx, dy in neighbors_relative_positions:
        # Calculate the absolute position of the neighbor
        neighbor_x = i + dx
        neighbor_y = j + dy

        # Check if the neighbor is within the bounds of the map
        if 0 <= neighbor_x < len(map) and 0 <= neighbor_y < len(map[0]) and map[neighbor_x][neighbor_y]<=value and invaded[neighbor_x][neighbor_y]==float("inf")*-1:
            # Get the content of the neighbor cell
            neighbor_content = map[neighbor_x][neighbor_y]
            neighbor_contents.append([neighbor_x,neighbor_y])
    return neighbor_contents


def calculate(map,di,dj,invaded,time,original_i,original_j,cityies):
    cityies+=1
    invaded[di][dj]=0
    
    max=float("inf")*-1
    times=float("inf")*-1
    
    
    
    #set the max if there is not neigbors
    if len(find(map,di,dj,map[di][dj],invaded))==0:
        max = time
        if di!=original_i or dj!=original_j:
            max-=1
    print(find(map,di,dj,map[di][dj],invaded))
    #loop over the neighbours to calculate the number of cityies and time to invade them      
    for cord in find(map,di,dj,map[di][dj],invaded):
        print(" the adjecunt for ",map[di][dj], " is ",map[cord[0]][cord[1]])
        time_copy=time+0
        print("time copy is ",time_copy)
        if invaded[cord[0]][cord[1]]==float("inf")*-1:
            times,cityiess = calculate(map,cord[0],cord[1],invaded,time_copy+1,original_i,original_j,cityies)
            cityies=cityiess
        
            print(" the number of cityies that has been invaded  from ", map[di][dj]," is ",cityies)
            if times>max:
                max=times
                
            
    
    return [max, cityies]
lines=[]

with open("alien.in","r") as file:
    for line in file:
        values = [int(value) for value in line.strip().split()]
        lines.append(values)


lines.pop(0)
counter = 0
map=[]
text=""
for  i in range(len(lines)):
    if i ==counter:
        #start of a new test case get hte dimenshion of the grid
        counter+= lines[i][0]+2
    else:
        if i+1==len(lines):
            #end of test case start calcuclating
            di= lines[i][0]
            dj= lines[i][1]
            invaded=[[float("inf")*-1 for i in range(len(map))] for j in range(len(map))]
            time , cityies = calculate(map,di,dj,invaded,0,di,dj,0)
            text+= str(cityies)+" "+str(time)+"\n"
            map=[]
        elif i+1== counter:
            #end of test case start calcualting
            di= lines[i][0]
            dj= lines[i][1]
            invaded=[[float("inf")*-1 for i in range(len(map))] for j in range(len(map))]

            time , cityies = calculate(map,di,dj,invaded,0,di,dj,0)
            text+= str(cityies)+" "+str(time)+"\n"
            map=[]
        else:
            # add the map
            map.append(lines[i])
            
with open("alien.answer","w")as file:
    file.write(text)
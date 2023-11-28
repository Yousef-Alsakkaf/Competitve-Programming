def neighbor(i,j,map):
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
        if 0 <= neighbor_x < len(map) and 0 <= neighbor_y < len(map[0]):
            # Get the content of the neighbor cell
            neighbor_content = map[neighbor_x][neighbor_y]
            neighbor_contents.append(neighbor_content)
    return neighbor_contents
def neighbor_cord(i,j,map):
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
        if 0 <= neighbor_x < len(map) and 0 <= neighbor_y < len(map[0]):
            # Get the content of the neighbor cell
            neighbor_content = map[neighbor_x][neighbor_y]
            neighbor_contents.append([neighbor_x,neighbor_y])
    return neighbor_contents

def score(map,dic,crane):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j]=="0":
                neighbor_content=neighbor(i,j,map)
                buildings=0
                total=0
                distance=0
                for close in neighbor_content:
                    try:
                        value=int(close)
                        if value>0 and value <= crane:
                            total+=value
                            buildings+=1
                            distance+=crane-value
                        
                    except:
                        continue
                if total >0:
                    distance=distance/buildings
                    dic[str(i)+" "+str(j)][crane]=[total,distance]
    
def find(map,dic,free_positions) :
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j]=="0":
                dic[str(i)+" "+str(j)]={}
                free_positions.append(str(i)+" "+str(j))

    
    return free_positions
def reset(crane_heights,map,dic,free_positions):
    dic={}
    free_positions=[]
    free_positions=find(map,dic,free_positions)
    
    ##make a dicitionary for every crane
    for crane in crane_heights:
  
        score(map,dic,crane)
     
    for key in dic:
        dic[key] = dict(sorted(dic[key] .items(), key=lambda x: (-x[1][0], x[1][1])))
    return [dic,free_positions]    

def adjust_map(map,target_position):
    
    cord= target_position.split(" ")
    i=int(cord[0])
    j=int(cord[1])
    list_neighbor=neighbor_cord(i,j,map)
   
    
    for i,j in list_neighbor:
        if map[i][j]!="X" and map[i][j]!="0":
            map[i][j]="0"
    
    
def calculate(map,crane_heights):
    

    for i in range(len(crane_heights)):
        crane_heights[i]=int(crane_heights[i])
    crane_heights.sort()
    answer=0
    dic={}
    free_positions=[]
    
    dic , free_positions=reset(crane_heights,map,dic,free_positions)
    print(dic)
    answer =0 
    
    for i in range(len(crane_heights)):
        #print("in loop")
        ##print(crane_heights[i])
        max_ratio=float("inf")*-1
        target_position=""
        
        for position in free_positions:
            
            if crane_heights[i] in  dic[position]:
                if dic[position][crane_heights[i]][1]!=0:
                    ratio = dic[position][crane_heights[i]][0]/dic[position][crane_heights[i]][1]
                else:
                    ratio = dic[position][crane_heights[i]][0]
                print("the ratio for ",crane_heights[i]," in position ",position," is ",ratio," the max so far is ",max_ratio)
                if ratio>max_ratio:
                    print("ratio changed")
                    max_ratio=ratio
                    target_position=position
                    
        if target_position:                  
            adjust_map(map,target_position)
            answer += dic[target_position][crane_heights[i]][0]
            print("the best position for ",crane_heights[i]," is ",target_position," which will give ",dic[target_position][crane_heights[i]][0])
            dic , free_positions=reset(crane_heights,map,dic,free_positions)
    

            
         
     
    dic={}
        
            
           
    return answer


file_path = 'crane.in'
lines = []

with open(file_path,"r") as file:
     # Iterate through the lines in the file
    for line in file:
        # Strip newline characters and split the line into a list of values
        line_values = line.strip().split()
        
        # Append the list of values to the 'lines' list
        lines.append(line_values)

counter=1
counter2=2
map=[]
for i in range(1,len(lines)):
    if i ==counter:
        #new testcase
        counter+= int(lines[i][1])+2

        crane_num=int(lines[i][2])
        width= int(lines[i][0])
        height= int(lines[i][1])
        
    elif i ==counter2:
        #get the height of the cranes
        crane_heights=[]
        for height in lines[i]:
            crane_heights.append(int(height))
        counter2=counter+1

    else:
        #the actual map
        map.append(lines[i])
        
        #if statmend to check if it is the end of the testcase so we start the calculation here
        if i+1==counter:
            answer = calculate(map,crane_heights)
            print(answer)
            map=[]
            break
            
            
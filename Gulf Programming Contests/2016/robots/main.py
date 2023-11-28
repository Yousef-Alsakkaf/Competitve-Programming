
def calculate(map,length,number_of_mines,positions):
    for mine in positions:
        i=mine//5
        j=mine%5
        map[i][j]=1
    
    i=0
    j=0
    robots=0
    while number_of_mines>0:

        robots+=1
        i=0
        j=0
        while i<length and j < length:
            right_wine=False
            up_wine=False
            right_increase=False
            up_increase=False

            #chekcing the horizontal
            for k in range(j,length):
                if map[i][k]==1:
                    right_wine=True
                    right_increase=k-j

                    break
            for k in range(i,length):
                if map[k][j]==1:
                    up_wine=True
                    up_increase=k-i
                    break
            if up_wine:
                i+=up_increase
                map[i][j]=0
                number_of_mines-=1
            elif right_wine:
                j+=right_increase
                map[i][j]=0
                number_of_mines-=1
            else:
                if i==length-1 and j==length-1:
                    break
                if i+1!=length:
                    i+=1
                if j+1!=length:
                    j+=1
   
    return robots

with open("robots.answer","w"):
    pass

lines=[]


with open("robots.in","r") as file :
    
    for line in file :
        values = [int(value) for value in line.strip().split()]
        lines.append(values)
        
        

length=lines[0][1]
map=[[0 for i in range(length)]for j in range(length)]
print(map)

testcase=1
for i in range(1,len(lines),2):
    number_of_mines=lines[i][0]
    positions=lines[i+1]
    answer = calculate(map,length,number_of_mines,positions)
    map=[[0 for i in range(length)]for j in range(length)]
    with open("robots.answer","a") as file:
        file.write("Case "+str(testcase)+": "+str(answer)+"\n")
        testcase+=1
def fill(buttom_left,top_right,matrix):
    x1,y1=buttom_left
    x2,y2=top_right
    counter=0
    for i in range(y1,y2+1,):
        for j in range(x1,x2+1,):
            if matrix[i][j]==0:
                matrix[i][j]=-1
                counter+=1
    return counter
            
    
    
    
def calculate(posters,board_h,board_w):
    matrix=[[0 for i in range(board_w)]for j in range(board_h)]
    counter=0
    for poster in posters:
        buttom_left=[poster[0],poster[1]]
        top_right=[poster[0]+poster[2]-1,poster[1]+poster[3]-1]
        counter+=fill(buttom_left,top_right,matrix)

    print(counter)
    
    return counter
        
lines=[]

with open("posters.in","r")as file:
    for line in file:
        lines.append([int(value) for value in line.strip().split()])
        


lines.pop(0)

counter = 0
text=""
posters=[]
for i in range(len(lines)):
    if i ==counter:
        board_w,board_h=lines[i]
        num_of_posters=lines[i+1][0]
        counter+=num_of_posters+2
        for j in range(i+2,counter):
            posters.append(lines[j])
        
        answer = calculate(posters,board_h,board_w)
        posters=[]
        text+= str(answer) +"/"+str(board_w*board_h)+"\n"
        
with open("posters.answer","w")as file:
    file.write(text)
        
       
def find(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=="K":
  
                return i,j
    
def posible(board,i,j):
    moves=[]
    moves.append( [i-2,j+1])
    moves.append( [i-2,j-1])
    moves.append( [i+2,j+1])
    moves.append( [i-2,j-1])
    moves.append( [i-1,j+2])
    moves.append( [i-1,j-2])
    moves.append( [i+1,j+2])
    moves.append( [i+1,j-2])
    neighbor_contents = []
    for neighbor_x,neighbor_y in moves:
        # Check if the neighbor is within the bounds of the map
        if 0 <= neighbor_x < len(board) and 0 <= neighbor_y < len(board[0]) :
            # Get the content of the neighbor cell
            if board[neighbor_x][neighbor_y]=="X":
                neighbor_content = board[neighbor_x][neighbor_y]
                neighbor_contents.append([neighbor_x,neighbor_y])
    return neighbor_contents
        
def calculate(board,target,current):
    counter=0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=="X":
                counter+=1
    if counter==0 and current<=target:
        return 1
    elif current>target:
        return 0
    i,j=find(board)
    moves=posible(board,i,j)
    for di,dj in moves:
        board_copy=board.copy()

        board_copy[di]=board_copy[di][:dj:]+"K"+board_copy[di][dj+1::]
        board_copy[i]=board_copy[i][:j:]+"E"+board_copy[i][j+1::]
  
        target_counter=calculate(board_copy,target,current+1)
        if target_counter==1:
            return 1
    return 0


lines=[]
with open("knight.in","r") as file:
    for line in file:
        lines.append(line.strip().split())


lines.pop(0)

counter=0
board=[]
text=""
for i in range(len(lines)):
    if i ==counter:
        
        length=int(lines[i][0])
        counter+=length+1
        
        
        for j in range(i+1,counter,):
            board.append(lines[j][0])
        
        
        target=0
        for k in range(len(board)):
            for z in range(len(board[k])):
                if board[k][z]=="X":
                    target+=1
            
        answer = calculate(board,target,0)
        if answer:
            text+="Y\n"
        else:
            text+="N\n"
        board=[]

with open("knight.answer","w")as file:
    file.write(text)
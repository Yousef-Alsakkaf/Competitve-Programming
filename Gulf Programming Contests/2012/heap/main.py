def posible(line):
    
    list=[]
    for i in range(len(line)):
        copy=line.copy()
        while copy[i]>0:
            copy[i]-=1
            copy2=copy.copy()
            list.append(copy2)

    return list
    

def mini(line,maxa_memo,mini_memo):
    
    if str(line) in mini_memo:
        return mini_memo[str(line)]
    if str(line) in maxa_memo:
        return maxa_memo[str(line)]*-1
    check=True
    for heap in line:
        if heap >0:
            check=False
            break
    if check:
        return 1
    
    posible_moves=posible(line)
    for moves in posible_moves:
        point= maxa(moves,maxa_memo,mini_memo)
        if point==-1:
            mini_memo[str(line)]=-1
            maxa_memo[str(line)]=1
            return -1
    mini_memo[str(line)]=1
    maxa_memo[str(line)]=-11
    return 1
def maxa(line,maxa_memo,mini_memo):
    if str(line) in maxa_memo:
        return maxa_memo[str(line)]
    if str(line) in mini_memo:
        return mini_memo[str(line)]*-1
    check=True
    for heap in line:
        if heap >0:
            check=False
            break
    if check:
        return -1
    
    posible_moves=posible(line)

    for moves in posible_moves:
        point= mini(moves,maxa_memo,mini_memo)
        if point==1:
            maxa_memo[str(line)]=1
            mini_memo[str(line)]=-1
            return 1
    maxa_memo[str(line)]=-1
    mini_memo[str(line)]=1
    return -1
        
    
    
    

lines=[]
with open("heap.in","r")as file:
    for line in file:
        lines.append([int(value)for value in line.strip().split()])
        
lines.pop(0)
for line in lines:
    answer = maxa(line,{},{})
    print(answer)
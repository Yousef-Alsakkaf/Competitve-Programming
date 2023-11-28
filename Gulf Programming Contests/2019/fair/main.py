def get_combinations(values,combinations,string,n,counter):

    if counter==n:
        combinations.append(string)
        return
    i =0
    while i <len(values):

        stringcopy=string+values[i]
        values_copy=values.copy()
        values_copy.pop(i)
        counter_copy=counter+0
        get_combinations(values_copy,combinations,stringcopy,n,counter_copy+1)
        i+=1
        
        
        
        
def compare(str1,str2):

    if str1==str2:
        
        return False
    else:
        for i in range(len(str1)):
            if str1[i] in str2:
                return False

        return True        
    
    

def calculate(n,values):
    combinations=[]
    get_combinations(values,combinations,"",n,0)

    minvalue=float("inf")
    for i in range(len(combinations)):
        for j in range(len(combinations)):
            if  not compare(combinations[i],combinations[j]):
                continue
            else:
                value = abs(int(combinations[i])-int(combinations[j]))
                minvalue=min(value,minvalue)

    return minvalue

with open("fair.answer","w")as file:
    pass
lines=[]
with open("fair.in","r") as file:
    for line in file:
        values = line.strip().split()
        lines.append(values)






# # Example usage:
# values = ['1', '2', '3', '4','5', '6', '7', '8',"9","0"]
# n = 5
# combinations = []
# minvalue=float("inf")
# get_combinations(values,combinations,"",n,0)

    
# print(minvalue)
text=""   
lines.pop()       
for i in range(0,len(lines),2):
    n= int(lines[i][1])
    values= lines[i+1]
    answer=  calculate(n,values)
    with open("fair.answer","a")as file:
        file.write(str(answer)+"\n")
    



    
def calculate(num1,num2):

 
    reminder1=num1%4
    
    if reminder1==0:
        base0=-1
        base1=-1
        base2=1
        base3=1
        if num2%4 == 0:
            return base0
        if num2%4 == 1:
            return base1
        if num2%4 == 2:
            return base2
        if num2%4 == 3:
            return base3
    
    if reminder1==1:
        base0=-1
        base1=1
        base2=1
        base3=-1
        if num2%4 == 0:
            return base0
        if num2%4 == 1:
            return base1
        if num2%4 == 2:
            return base2
        if num2%4 == 3:
            return base3
        
       
    if reminder1==2:
        base0=1
        base1=1
        base2=-1
        base3=-1
        if num2%4 == 0:
            return base0
        if num2%4 == 1:
            return base1
        if num2%4 == 2:
            return base2
        if num2%4 == 3:
            return base3
    if reminder1==3:
        base0=1
        base1=-1
        base2=-1
        base3=1
        if num2%4 == 0:
            return base0
        if num2%4 == 1:
            return base1
        if num2%4 == 2:
            return base2
        if num2%4 == 3:
            return base3

        
# def get_element(i, j):
#     # Calculate the index in the repeating 4x4 pattern
#     pattern_i = i % 4
#     pattern_j = j % 4

#     # Check the pattern to determine "W" or "L"
#     if (pattern_i < 2 and pattern_j < 2) or (pattern_i >= 2 and pattern_j >= 2):
#         return -1
#     else:
#         return 1        
  





lines=[]

with open("squares.in","r") as file:
    for line in file:
        lines.append(line.strip().split())



lines.pop(0)
text=""
testcase=1
for line in lines:
    balls1,balls2,player1=line
    balls1=int(balls1)
    balls2=int(balls2)
    
    answer = calculate(balls1,balls2)
    if player1=="M":
        if answer==1:
            text+=str(testcase)+". I Win!\n"
        else:
            text+=str(testcase)+". I Lose!\n"
    if player1=="F":
        if answer==1:
            text+=str(testcase)+". I Lose!\n"
        else:
            text+=str(testcase)+". I Win!\n"
    testcase+=1
with open("squares.answer","w")as file:
    file.write(text)
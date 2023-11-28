# def calculate(line):
#     answerlist=[]
    
#     for word in line:
        
#         if len(word)>3:
            
#             subword= word[1:len(word)-1:]
#             subword=subword[::-1]

#             answerlist.append(word[0]+subword+word[len(word)-1])
#         else:
#             answerlist.append(word)
    
    
#     return " ".join(answerlist)
            

# lines=[]

# with open("shadow.in","r") as file:
#     for line in file:
#         lines.append(line.strip().split())

# print(lines)
# lines.pop(0)
# text=""
# for line in lines:
#     line.pop(0)
#     answer = calculate(line)
#     text += answer +"\n"
    
# with open("shadow.answer","w")as file:
#     file.write(text)


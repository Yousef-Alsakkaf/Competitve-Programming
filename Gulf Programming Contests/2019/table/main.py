
def fz(map):
    col1_length= max(len(map["1"][[len(i) for i in map["1"]].index(max([len(i) for i in map["1"]]))]),len(map["4"][[len(i) for i in map["4"]].index(max([len(i) for i in map["4"]]))]))
    col2_length= max(len(map["2"][[len(i) for i in map["2"]].index(max([len(i) for i in map["2"]]))]),len(map["5"][[len(i) for i in map["5"]].index(max([len(i) for i in map["5"]]))]))
    col3_length= max(len(map["3"][[len(i) for i in map["3"]].index(max([len(i) for i in map["3"]]))]),len(map["6"][[len(i) for i in map["6"]].index(max([len(i) for i in map["6"]]))]))
    return [col1_length,col2_length,col3_length]     
def split(map,index,index2):
    sentences=map[index][index2].split(" ")
    half=len(sentences)//2
    first=sentences[:half:]
    second=sentences[half::]
    map[index].pop(index2)
    map[index].insert(index2," ".join(second))
    map[index].insert(index2," ".join(first))
def format(length,map,col1_length,col2_length,col3_length,current_length):
    if current_length<=length:
        return

    list=[col1_length,col2_length,col3_length]
    index=list.index(max(list))
    
    first_index=0
    second_index=0
    third_index=0
    first_index_length=0
    second_index_length=0
    third_index_length=0
    if  max(len(map["1"][[len(i) for i in map["1"]].index(max([len(i) for i in map["1"]]))]),len(map["4"][[len(i) for i in map["4"]].index(max([len(i) for i in map["4"]]))])) ==len(map["1"][[len(i) for i in map["1"]].index(max([len(i) for i in map["1"]]))]):
        first_index="1"
        first_index_length=[len(i) for i in map["1"]].index(max([len(i) for i in map["1"]]))
    else:
        first_index="4"
        first_index_length=[len(i) for i in map["4"]].index(max([len(i) for i in map["4"]]))
        
    if  max(len(map["2"][[len(i) for i in map["2"]].index(max([len(i) for i in map["2"]]))]),len(map["5"][[len(i) for i in map["5"]].index(max([len(i) for i in map["5"]]))])) ==len(map["2"][[len(i) for i in map["2"]].index(max([len(i) for i in map["2"]]))]):
        second_index="2"
        second_index_length=[len(i) for i in map["2"]].index(max([len(i) for i in map["2"]]))
    else:
        second_index="5"
        second_index_length=[len(i) for i in map["5"]].index(max([len(i) for i in map["5"]]))
        
    if  max(len(map["3"][[len(i) for i in map["3"]].index(max([len(i) for i in map["3"]]))]),len(map["6"][[len(i) for i in map["6"]].index(max([len(i) for i in map["6"]]))])) ==len(map["3"][[len(i) for i in map["3"]].index(max([len(i) for i in map["3"]]))]):
        third_index="3"
        third_index_length=[len(i) for i in map["3"]].index(max([len(i) for i in map["3"]]))
    else:
        third_index="6"
        third_index_length=[len(i) for i in map["6"]].index(max([len(i) for i in map["6"]]))
        
    
        
        
    if index==0:
        list2 = map["1"]
        list3= map["4"]
        index2= [len(i) for i in list2].index(max([len(i) for i in list2]))
        index3= [len(i) for i in list3].index(max([len(i) for i in list3]))
        
        
        
        if len(map["1"][index2])>len(map["4"][index3]):
            
            if len(map["1"][index2].split(" "))==1:
                if len(map[second_index][second_index_length].split(" "))==1:
                   if len(map[third_index][third_index_length].split(" "))==1: 
                       return
                   else:
                       split(map,third_index,third_index_length)
                       col1_length,col2_length,col3_length=fz(map)
           
                       format(length,map,col1_length,col2_length,col3_length,col1_length+col2_length+col3_length)
                       return
                else:
                    split(map,second_index,second_index_length)
                    col1_length,col2_length,col3_length=fz(map)
           
                    format(length,map,col1_length,col2_length,col3_length,col1_length+col2_length+col3_length)
                    return
                
            
            
            split(map,"1",index2)
            
            col1_length,col2_length,col3_length=fz(map)
           
            format(length,map,col1_length,col2_length,col3_length,col1_length+col2_length+col3_length)
           
        else:
            
            if len(map["4"][index3].split(" "))==1:
                if len(map[second_index][second_index_length].split(" "))==1:
                   if len(map[third_index][third_index_length].split(" "))==1: 
                       return
                   else:
                       split(map,third_index,third_index_length)
                       col1_length,col2_length,col3_length=fz(map)
           
                       format(length,map,col1_length,col2_length,col3_length,col1_length+col2_length+col3_length)
                       return
                else:
                    split(map,second_index,second_index_length)
                    col1_length,col2_length,col3_length=fz(map)
           
                    format(length,map,col1_length,col2_length,col3_length,col1_length+col2_length+col3_length)
                    return
        
            split(map,"4",index3)
           
            col1_length,col2_length,col3_length=fz(map)
            format(length,map,col1_length,col2_length,col3_length,col1_length+col2_length+col3_length)
    elif index==1:
        list2 = map["2"]
        list3= map["5"]
        index2= [len(i) for i in list2].index(max([len(i) for i in list2]))
        index3= [len(i) for i in list3].index(max([len(i) for i in list3]))
       
        
        if len(map["2"][index2])>len(map["5"][index3]):
            if len(map["2"][index2].split(" "))==1:
                if len(map[first_index][first_index_length].split(" "))==1:
                   if len(map[third_index][third_index_length].split(" "))==1: 
                       return
                   else:
                       split(map,third_index,third_index_length)
                       col1_length,col2_length,col3_length=fz(map)
           
                       format(length,map,col1_length,col2_length,col3_length,col1_length+col2_length+col3_length)
                       return
                else:
                    split(map,first_index,first_index_length)
                    col1_length,col2_length,col3_length=fz(map)
           
                    format(length,map,col1_length,col2_length,col3_length,col1_length+col2_length+col3_length)
                    return
             
            split(map,"2",index2)
            
            col1_length,col2_length,col3_length=fz(map)
            format(length,map,col1_length,col2_length,col3_length,col1_length+col2_length+col3_length)
        else:
            if len(map["5"][index3].split(" "))==1:
                if len(map[first_index][first_index_length].split(" "))==1:
                   if len(map[third_index][third_index_length].split(" "))==1: 
                       return
                   else:
                       split(map,third_index,third_index_length)
                       col1_length,col2_length,col3_length=fz(map)
           
                       format(length,map,col1_length,col2_length,col3_length,col1_length+col2_length+col3_length)
                       return
                else:
                    split(map,first_index,first_index_length)
                    col1_length,col2_length,col3_length=fz(map)
           
                    format(length,map,col1_length,col2_length,col3_length,col1_length+col2_length+col3_length)
                    return
            split(map,"5",index3)
            
            col1_length,col2_length,col3_length=fz(map)
            format(length,map,col1_length,col2_length,col3_length,col1_length+col2_length+col3_length)
    
    elif index==2:
        list2 = map["3"]
        list3= map["6"]
        index2= [len(i) for i in list2].index(max([len(i) for i in list2]))
        index3= [len(i) for i in list3].index(max([len(i) for i in list3]))

        if len(map["3"][index2])>len(map["6"][index3]):
 
            if len(map["3"][index2].split(" "))==1:
 
                if len(map[second_index][second_index_length].split(" "))==1:
                   if len(map[first_index][first_index_length].split(" "))==1: 
                       return
                   else:
                       split(map,first_index,first_index_length)
                       col1_length,col2_length,col3_length=fz(map)
           
                       format(length,map,col1_length,col2_length,col3_length,col1_length+col2_length+col3_length)
                       return
                else:
                    split(map,second_index,second_index_length)
                    col1_length,col2_length,col3_length=fz(map)
           
                    format(length,map,col1_length,col2_length,col3_length,col1_length+col2_length+col3_length)
                    return
            split(map,"3",index2)
           
            col1_length,col2_length,col3_length=fz(map)
            format(length,map,col1_length,col2_length,col3_length,col1_length+col2_length+col3_length)
        else:
            if len(map["6"][index3].split(" "))==1:
                if len(map[second_index][second_index_length].split(" "))==1:
                   if len(map[first_index][first_index_length].split(" "))==1: 
                       return
                   else:
                       split(map,first_index,first_index_length)
                       col1_length,col2_length,col3_length=fz(map)
           
                       format(length,map,col1_length,col2_length,col3_length,col1_length+col2_length+col3_length)
                       return
                else:
                    split(map,second_index,second_index_length)
                    col1_length,col2_length,col3_length=fz(map)
           
                    format(length,map,col1_length,col2_length,col3_length,col1_length+col2_length+col3_length)
                    return
            split(map,"6",index3)
            
            col1_length,col2_length,col3_length=fz(map)
            format(length,map,col1_length,col2_length,col3_length,col1_length+col2_length+col3_length)
          
   
    
    
    

def calculate(length,map):
 
  
   
    
   
    col1_length= max(len(map["1"][0]),len(map["4"][0]))
    col2_length= max(len(map["2"][0]),len(map["5"][0]))
    col3_length= max(len(map["3"][0]),len(map["6"][0]))
    total=col1_length+col2_length+col3_length
   
    if col1_length+col2_length+col3_length>length:
        
        format(length,map,col1_length,col2_length,col3_length,col1_length+col2_length+col3_length)
    
      
    
    num_lines=max(len(map["1"]),len(map["2"]),len(map["3"]))+max(len(map["4"]),len(map["5"]),len(map["6"]))
    
    return num_lines
lines=[]
with open("table.in","r") as file:
    for line in file:
        lines.append(line.strip().split())
        

map={}
testcase=1
text=""
for i in range(0,len(lines),7):
    
    if lines[i][0]=="0":
        break
    length= int(lines[i][0])
    map["1"]=[" ".join(lines[i+1])]
    map["2"]=[" ".join(lines[i+2])]
    map["3"]=[" ".join(lines[i+3])]
    map["4"]=[" ".join(lines[i+4])]
    map["5"]=[" ".join(lines[i+5])]
    map["6"]=[" ".join(lines[i+6])]
    answer = calculate(length,map)
  
    if testcase==5:
        print(map) 
        col1,col2,col3=fz(map)
        print( col1+col2+col3)            
    map={}
    print(answer)
    
    text+=str(answer)+"\n"
    testcase+=1
   
with open("table.answer","w")as file:
    file.write(text)
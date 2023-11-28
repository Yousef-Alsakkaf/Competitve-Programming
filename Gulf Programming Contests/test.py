def generate_combinations(charecters,length,current,list,string):
    if length<current:
        return 
    
    for char in charecters:
        stringcopy=string
        stringcopy+=char
        list.append(stringcopy)
        charecterscopy=charecters.copy()
        charecterscopy.remove(char)
        
        generate_combinations(charecterscopy,length,current+1,list,stringcopy)
        

input_str = "hello"
list=[]
charecters=[char for char in input_str]
generate_combinations(charecters,len(input_str),1,list,"")
print(list)

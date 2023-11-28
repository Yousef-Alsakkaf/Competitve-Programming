def calculate(line):

<<<<<<< HEAD
    sentence_list = [char for char in line]

    list=[]
    list.append(line)
=======
    sentence_list = [char for char in line[0]]

    list=[]
    list.append(line[0])
>>>>>>> 687f8abf5f27624b05347836c77a2dcf15f44669
    for i in range(len(sentence_list)-1):
        char = sentence_list.pop(0)
        sentence_list.append(char)
        sentence= "".join(sentence_list)
        list.append(sentence)
<<<<<<< HEAD

    
    list.sort()

    print(list.index(line))
    return
=======
    list.sort()
    return list.index(line[0])
>>>>>>> 687f8abf5f27624b05347836c77a2dcf15f44669

with open("sorter.answer","w"):
    pass

lines=[]

with open("sorter.in","r")as file:
    for line in file:
<<<<<<< HEAD
        value = line.strip()
=======
        value = line.split("\n")
>>>>>>> 687f8abf5f27624b05347836c77a2dcf15f44669
        lines.append(value)

lines.pop(0)


for line in lines:
<<<<<<< HEAD
    answer = calculate(line)
=======
    answer = calculate(line)
    with open("sorter.answer","a") as file:
        file.write(str(answer)+"\n")
    
>>>>>>> 687f8abf5f27624b05347836c77a2dcf15f44669

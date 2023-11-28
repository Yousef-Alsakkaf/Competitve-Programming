lines=[]

with open("peak.in","r") as file:
    for line in file:
        lines.append(line.strip().split())


lines.pop(0)
counter=0
for i in range(len(lines)):
    if i ==counter:
        
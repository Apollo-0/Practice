file = open("transcript00.txt","r")
transcript00 = []

for line in file:
    transcript00.append(line.strip())
    
file.close()

print(transcript00[0])
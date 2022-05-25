#more efficient way of reading two files

file = open("transcript01.txt","r")
#create list for the first text file
transcript01 = []
#populate list with text
for line in file:
    transcript01.append(line.strip())
file.close()


file = open("transcript01.5.txt","r")
transcript01_5 = []
for line in file:
    transcript01_5.append(line.strip())
file.close


#determine length of list
transcript01_length = len(transcript01)

#for every item in range of the length of the list print the items
#then it goes through each item and print in turn

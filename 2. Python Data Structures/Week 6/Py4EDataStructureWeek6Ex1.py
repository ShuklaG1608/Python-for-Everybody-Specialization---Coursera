'''Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.'''

name = input("Enter file:")
handle = open(name)
mydiction = dict()
myList = []
hoursList = []
for lines in handle:
    if lines.startswith("From "):
        words = lines.split()
        myList.append(words[5])

for hours in myList:
    h = hours.split(':')
    hoursList.append(h[0])


for word in hoursList:
    mydiction[word] = mydiction.get(word,0)+1
    temp = sorted(mydiction.items())
temp.sort()
for hrs,ct in temp:
    print(hrs,ct)

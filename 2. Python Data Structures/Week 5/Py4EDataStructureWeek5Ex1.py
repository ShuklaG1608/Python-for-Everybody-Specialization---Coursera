'''Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program 
looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python 
dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is 
produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.'''

name = input("Enter file:")
handle = open(name)
myList = []
diction = dict()
for lines in handle:
    if lines.startswith("From: "):
        words = lines.split()
        myList.append(words[1])

for word in myList:
    diction[word] = diction.get(word,0)+1
    
    
myCount =None
myWord = None
for k,v in diction.items():
	if myCount is None or v>myCount:
		myCount = v
		myWord = k
print(myWord,myCount)

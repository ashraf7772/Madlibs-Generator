with open("story.txt", "r") as f: #reading the file story.txt
    story = f.read() #gives all the text inside the file

#print(story)
words = set() #A set to store what all the different words are
wordStart = -1 #this variable will tell us if we have found the starting index of a word
targetStart = "<"
targetEnd = ">"

for i, char in enumerate(story): #get index and value                                 #lines 10-17 locate all the 
    if char == targetStart:                                                           #different words that are inside
        wordStart = i                                                                 #story.txt

    if char == targetEnd and wordStart != -1:
        word = story[wordStart: i + 1]
        words.add(word) #add to the set
        wordStart = -1  #reset the start of words

#print(words)
ansDic = {} #ansDic stands for answer dictionairy or the answers. Here we have all our words

#for loop below to loop through all the unique words we
#have and ask the user to give us a value for them
for word in words:        #ans means answer basically
    ans = input("Type a word for " + word + "(write after :): ") #not a ','. We use + because this is an input statement and not a print statement.
    ansDic[word] = ans

for word in words:                           #here in this for loop we go through and replace
    story = story.replace(word, ansDic[word])        #our words with the user generated words

print(story)


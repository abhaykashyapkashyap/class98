intro=input("enter your introduction")
chracter=0
word = 1
for i in intro:
    chracter=chracter+1
    if(i==' '):
        word = word+1
print("number of character in the string")
print(chracter)
print("number of word in the string")
print(word)
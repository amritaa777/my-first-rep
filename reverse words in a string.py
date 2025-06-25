#reverse words in a string
sentence=input('ENTER A SENTENCE')
empty=''
words=sentence.split()
#print(words)
for i in range(len(words)):
    if i==0:
        empty=empty+words.pop()
    #print(empty)
    else:
        empty=empty+' '+words.pop()
rev=empty
print(rev)
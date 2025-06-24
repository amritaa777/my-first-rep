word1=input('ENTER STRING 1')
word2=input('ENTER STRING 2')
empty=''
"""
x=len(word1)
try:
    for i in range(x):
        emp=word1[i]+word2[i]
        
    print(emp)
except:
    emp=emp+word2[i:]
    print(emp)
"""

lenw1=len(word1)
lenw2=len(word2)

w1=list(word1)
w2=list(word2)

if lenw1>lenw2:
    for i in range(lenw2):
        empty=empty+word1[i]+word2[i]
    empty=empty+word1[lenw2:]
    print(empty)
else:
    for i in range(lenw2):
        empty=empty+word1[i]+word2[i]
    empty=empty+word1[lenw2:]
    print(empty)
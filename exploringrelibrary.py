#re.findall()
import re
str="""Hello my number is 123456789 and my friend's number is 987654321 1"""
regex='\d+'
match=re.findall(regex,str)
print(match)

import re
str="""Hello my number is 123456789 and my friend's number is 987654321 1"""
regex='m'
match=re.findall(regex,str)
print(match)


#re.compile()
import re
p=re.compile('[a-e]')
print(p)

import re
p=re.compile('[a-e]')
print(p)
print(p.findall('Aye, said Mr.Gibenson Stark'))

import re
d=re.compile('\s')
print(d.findall('Aye, . said Mr.Giberson Stark'))

import re
o=re.compile('\d')
print(o.findall('I went to home at 11 A.M on July 4th 1886'))

import re 
k=re.compile('\d+')
print(k.findall('I went to home at 11 A.M on July 4th 1886'))

import re
i=re.compile('\w')
print(i.findall('He said * in some_Lang.'))

import re
c=re.compile('\w+')
print(c.findall('I went home at 11 A.M. he \
said *** in some_language.'))

import re
v=re.compile('\W+')
print(v.findall('He said *** in some_lang.'))

import re
x=re.compile('\W')
print(x.findall('He said *** in some_lang.'))

import re
h=re.compile('fgh*')
print(h.findall('fghhhhfggfhhhfghhhghfghh'))

import re
h=re.compile('fgh*')
print(h.findall('fghhhhfggfhhhfghhhghfghjh'))

import re
h=re.compile('fg*h*')
print(h.findall('fghhhhfggffhhhfghhhghfghh'))

num = 27
out = ''
# string = 'i am cesar'
string = 'abc'
exa = ' abcdefghijklmnopqrstuvwxyz'
for i in string:
    k = exa.index(i)
    out = out + exa[k+num]
print(out)
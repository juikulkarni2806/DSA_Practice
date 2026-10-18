#reversing a String
s="Hello"
revS=" "
for i in range(len(s) -1,-1,-1):
    revS+=s[i]
print(revS)
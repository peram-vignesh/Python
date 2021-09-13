def length (a,b):
    c=len(a)
    d=len(b)
    if c==d:
        z="True"
    else :
        z='False'
    return z
str1=str(input('Enter the first arguement:'))
str2=str(input('Enter the second arguement:'))
print(length(str1,str2))

def root6(n,x):
   
    n+=1
    x=x/x**n
    return x
root1=int(input('Enter the root:'))
num1=input('Enter the Number')
if num1.isnumeric()== 'True':
    num1=int(num1)
else:
    num1=2
print(root6(root1,num1))

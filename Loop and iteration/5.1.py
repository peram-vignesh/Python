num1 = 0
total=0
num=0
while num1 != "done":
    num1=input('enter a number')
    if num1.isnumeric()== True:
        num1=int(num1)
    elif num1 =='done':
        break
    else:
        num1=0
        print('Entered a string')
    total = total+num1
    num=num+1
print(total,num,total/num)

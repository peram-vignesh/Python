def rand(x,y):
    import random
    randlist=random.sample(range(x,y),3)
    return randlist
num1=int(input('Enter the first number:'))
num2=int(input('Enter the second number:'))
print(rand(num1,num2))

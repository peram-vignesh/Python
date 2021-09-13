def volume(l,b,h):
    volume=l*b*h
    return volume
length=int(input('Enter the length of the box'))
breadth=int(input("Enter the breadth of the box"))
height=int(input('Enter the height of the box'))
print('Volume of the box:', volume(length,breadth,height))


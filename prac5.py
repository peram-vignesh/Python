def fail(z):
    y=z*z*z
    return y
cube=input('enter the number:')
if cube.isnumeric()==True:
    cube=int(cube)
else :
    cube=2
print(fail(cube))
    

hours=int(input('Number of hours worked:'))
pay=int(input('pay per hour:'))
if hours > 40:
    x=hours-40
    z=pay*1.5
    x= x * z
    y=40*pay
    total=x+y
else:
    total=hours*pay
print(total)

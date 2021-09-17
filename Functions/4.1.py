def computepay(hours,rate):
    pay = hours*rate
    return pay
hour=int(input('Number of hours worked'))
rate=int(input('Pay per Hour'))
print(computepay(hour,rate))
import time
from datetime import date

# second = 1686000636.834957

# local_time = time.time(second)

# print("The Second is",local_time)

# dates = date.today()

# print("Today date is", dates)


timesatmp = time.strftime('%H:%M:%S')

print(timesatmp)

timesatmp = time.strftime('%H')

print(timesatmp)

timesatmp = time.strftime('%M')

print(timesatmp)

timesatmp = time.strftime('%S')

print(timesatmp)

z = int(input("Enter the value of: "))

match z:

    case 0:
        print("Value is Zero")

    case 4:
        print("Value is Mid")
    
    case _ if z!=10:
        print(z,"is not equal to 10")

    case _ if z!= 15:
        print(z, "is not equal to 15")
    case _:
        print(z)

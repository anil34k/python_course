year =  2024
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(f'{year} is leap year')
    if year % 2 == 0:
        print(f'{year} is even')
    else:
        print(f'{year} is odd')
else:
    print("not a leap year")
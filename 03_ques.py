year = int(input("enter a year"))

if (year % 400 == 0) and (year % 100 == 0):
    print("It is a leap year")

else:
    if (year % 4 ==0) and (year % 100 != 0):
        print("It is a leap year")

    else:
        print("It is not a leap year")
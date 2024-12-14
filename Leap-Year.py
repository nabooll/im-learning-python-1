#Leap Years!
year = int(input("What Year : "))

#We are gonna check if the year is leap or no by using these:
#Its divided by 4, divided by 100 (if its not then its still count as leap year), and divided by 400.

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It's Leap Year!")
        else:
            print("Not Leap Year!")

    else:
        print("Not Leap Year!")
else:
    print("Not Leap Year!")
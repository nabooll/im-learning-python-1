#Gross pay with overtime
hour = input("Enter Hour of work : ")
rate = input("Enter Rate of work : ")

#Now we gotta change it, so the input can transform into real numbers (we use float here)
hour = float(hour)
rate = float(rate)

#The instruction says, if the hour of work is above 40, then they get the 1.5x hourly rate!
#We are going to use conditional here, so we use if else statement
if hour < 40:
    pay = round(hour * rate , 2)
    print(f"We gonna pay you as much as ${pay}")
else:
    overtime = hour - 40
    pay = round((40 * rate) + (overtime * rate * 1.5) , 2)
    print(f"We gonna pay you as much as ${pay}")
bill = 0 #The Bill starts from zero ofcourse!
size = input("size = ")
if size == "M": #M stands for Mini size, and it will cost $5
    bill += 5
elif size == "N": #N stands for Normal size, it will cost $8
    bill += 8
else: #If the size is bigger than Normal size, it will cost more than $10
    bill += 10

add_mushroom = input("add_mushroom = ") #Y if you want to add mushroom, N if you don't want additional mushroom
if add_mushroom == "Y":
    add_mushroom = 0
    print(input("what size : "))
    if add_mushroom == "M" or "N": #M stands for Mini
        bill += 1
    elif add_mushroom == "L": #L stands for Large size, it means more mushroom!
        bill += 2
else:
    bill += 0

extra_cheese = input("extra cheese : ") #If you want to put additional cheese, input Y! if not, input N!
extra_cheese == 0
if extra_cheese == "Y":
    bill += 1
else:
    bill += 0

print (f"Your final bill is: ${bill}")
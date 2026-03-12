i=0
while i<10:
    i = i + 1
    if i==4:
        continue
    if i==15:
        break
    print(i)
else:
    print("I is no longer greater than 10")



# For loop

number = int(input("Enter a number: "))
print("The table of :",number)

for value in range(1,11):
    print (value*number)
else:
  print("Finally finished!")
balance = 100000

amount =int(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid amount.")

elif amount > balance:
    print ("Insaficiant balance.")

else:
    print("Withdrawal Sucseddfull.")

balance = 100000
amount = int(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid amount.")
elif amount > balance:
    print("Insufficient balance.")
else:
    print("Withdrawal Successful.")


#ternary operator

value = int(input("Enter any value: "))
result = "positive" if value > 0 else "negative" if value < 0 else "zero"
print(result)
is_hot = False
is_cold = True

if is_hot:
  print("It is hot today")
  print("Drink plenty of water")
elif is_cold:
  print("It is a cold day")
  print("Wear warm clothes")
else:
  print("It is a lovely day")

# formatted string
price = 1000000
print(f"Enjoy your day ${price}")

# logical operator
has_good_credit = False
has_high_income = True
has_criminal_record = False

if has_good_credit and has_high_income:
  print("Elligible for loan")
elif has_good_credit or has_high_income:
  print("Elligible for loan to pay in 30 days")
elif  has_high_income and not has_criminal_record:
  print("Elligible for 2 days loan")
try:
  age = int(input('Age: '));
  income = 1000 / age
  print(age)
except ValueError:
  print('Invalid value')
except ZeroDivisionError:
  print('Age should not be equal to 0')

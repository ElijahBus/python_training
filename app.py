from pathlib import  Path

# Absolute path : start from the drive
# Relative path : relative to the current 
# 

path = Path("ecommerce")
# print(path.exists())

path2 = Path("emails")
# path2.mkdir()
# path2.rmdir()

current_path = Path()
for file in current_path.glob('*'):
  print(file)
  
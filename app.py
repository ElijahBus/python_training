import converters
from converters import lbs_to_kg
import random

# import ecommerce.shipping
# from ecommerce.shipping import calc_shipping
from ecommerce import shipping

lbs_to_kg(200)

print(converters.kg_to_lbs(70))

# Package usage
shipping.calc_shipping()

# Generate random values 

for i in range(3):
  print(random.randint(2,6))
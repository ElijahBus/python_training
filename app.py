# customer = {
#   'name': 'Elijah',
#   'age': 30,
#   'is_verified' : True,
# }
# customer['name'] = "JOshua"
# customer['birthdate'] = 'Sep 12, 2020'
# print(customer.get('birthdate', 'Oct 12, 1990'))

# Challenge : digits to words converter
# phone = input("Phone: ")
# digits_mapping = {
#   "1": "One",
#   "2": "Two",
#   "3": "Three"
# }

# output = ""
# for char in phone:
#   output += digits_mapping.get(char, "!") + " "
# print(output)

#Challenge Emoji converter

message = input("> ")
words = message.split(" ");

emojis = {
  ':)': "😇 ",
  '(:': "😠 "
}
output = ""
for word in words:
  output += emojis.get(word, word) + " "
print(output)
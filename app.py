class Common:
  def move(self):
    print("move")

class Point(Common):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def draw(self):
    print("draw")


class Person:
  def __init__(self, name):
    self.name = name

  def talk(self):
    print(f"Hi, I am {self.name}")

class Dog(Common):
  pass


point1 = Point(10,20)
print(point1.move())
print(point1.x)

person1 = Person("Charlie")
person1.talk();

dog = Dog()
dog.move()

class Animal:
    def __init__(self, name):
        self.name = name

    def myName(self):
        print("내 이름은 " + self.name + "야")

class Cat(Animal):
    def voice(self):
        print("야옹")

class Dog(Animal):
    def voice(self):
        print("멍멍")

cat = Animal("고양이")
dog = Animal("강아지")

cat.myName()
cat.voice()
dog.myName()
dog.voice()
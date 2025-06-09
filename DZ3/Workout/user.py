class User:
    age = 0

    def __init__(self, name):
        print('Я создался')
        self.username = name

    def seyName(self):
        print('меня зовут', self.username)

    def sayAge(self):
        print(self.age)

    def setAge(self, newAge):
        self.age = newAge

    def addCard(self, card):
        self.card = card

    def getCard(self):
        return self.card

from user import User
from card import Card


user1 = User('Alex')
user2 = User('Mark')
user3 = User('Marta')

user1.seyName()
user1.sayAge()
user1.setAge(33)
user1.sayAge()


card = Card('4556 1289 3248 4669', '11/30', 'Alex F')
user1.addCard(card)
user1.getCard().pay(1000)

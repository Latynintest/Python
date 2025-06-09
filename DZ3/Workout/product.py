class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def returnName(self):
        return self.name

    def returnPrice(self):
        return self.price

    def returnStr(self):
        return f'{self.name} {self.price}'

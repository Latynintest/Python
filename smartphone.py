class Smartphone:
    def __init__(self, phone_brand, phone_model, subscriber_number):
        self.phone_brand = phone_brand
        self.phone_model = phone_model
        self.subscriber_number = subscriber_number

    def __str__(self):
        return (f'{self.phone_brand} - {self.phone_model}.'
                f'{self.subscriber_number}')

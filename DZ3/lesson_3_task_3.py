from address import Address
from mailing import Mailing


from_address = Address(305009, 'Курск', 'Дубровинского', 10, 2)
to_address = Address(123056, 'Москва', 'Васильевская', 3, 5)

cost = 1000
track = '1421171600738'

mailing = Mailing(to_address, from_address, cost, track)

print(mailing)

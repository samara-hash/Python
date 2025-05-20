from address import Address
from mailing import Mailing

to_address = Address("140700", "Шатура", "Жарова", "33", "12")
from_address = Address("115583", "Москва", "Каширская", "65", "23")

mailing = Mailing(to_address, from_address, 1200, "UAF275454")

print(mailing)
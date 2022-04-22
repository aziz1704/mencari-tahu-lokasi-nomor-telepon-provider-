import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
c=input("Masukan nomer telepon :")
phone_number=phonenumbers.parse(c)
print(geocoder.description_for_number(phone_number,"en"))
print(carrier.name_for_number(phone_number, "en"))
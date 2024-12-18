phones = ["Samsung S24","iPhone 16","Nothing Phone 2","Google Pixel 9"]
confirmed_phones = []

print(phones)
print(confirmed_phones)

def confirming_phones(phones: list,confirmed_phones: list):
    while phones:
        phone = phones.pop()
        confirmed_phones.append(phone)

confirming_phones(phones,confirmed_phones)

print(phones)
print(confirmed_phones)
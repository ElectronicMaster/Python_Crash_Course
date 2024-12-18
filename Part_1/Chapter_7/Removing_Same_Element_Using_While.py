pets = ['cat','dogs','goldfish','cat','rabbit','cat']

only_instance = list(set(pets))

while 'cat' in pets:
    pets.remove('cat')

print(only_instance)
print(pets)
aliens = []

for i in range(30):
    new_alien = {'color':'green','speed':'medium','points':10}
    aliens.append(new_alien)

for alien in aliens[:3]:
    print(alien)
print('...')
print(f'Total number of aliens present : {len(aliens)}')

for alien in aliens[:3]:
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print('...')
print(f'Total number of aliens present : {len(aliens)}')
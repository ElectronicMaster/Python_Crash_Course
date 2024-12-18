users = {
    'aeinstien':{
        'first':'albert',
        'last':'einstien',
        'location':'preinstein'
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'london'
    }
}

for username,user_info in users.items():
    print(f'Username : {username}')
    full_name = f'{user_info['first']} {user_info['last']}'
    print(f'Full name : {full_name.title()}')
    print(f'location : {user_info['location']}\n')
def password_controller(pwd):
    if len(pwd)>8:
        return 'Valid'
    else:
        return 'In Valid'
    
password_list = ['xysz$#@&^','abc66661234','1234677890','xyzhhhhh']
for pwd in password_list:
    result = password_controller(pwd)
    print(f'{pwd} : {result}')

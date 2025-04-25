def display_name(fname,lname):
    if fname=='' or lname=='':
        return 'name & last name is manidatary'
    return f'{fname} {lname}'

res = display_name('xyz','abc')
print(res)

#write a program that take 1 student marks and marks grater than 35 -pass, otherwise - fail

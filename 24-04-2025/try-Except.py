try:
    n1 = int(input('Enter first number'))
    n2 = int(input('Enter second number'))
    res = n1/n2
except  Exception as e:
    print(f'error: {e}')
else:
    print(res)

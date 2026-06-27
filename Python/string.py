var = 'abdo'
variable = 50

mysring = 'the string is: {} and the second string is: {}'.format(var, variable)
print(mysring)

mysring = 'the string is: %s and the second string is: %d' % (var, variable)
print(mysring)


num1 = '%d + 50' % variable
print(num1)

num2 = '{} + 50'.format(variable)
print(num2)   # this is a string

num3 = variable + 50
print(num3)   # this is a number



var = 'abdo'
my_string = f'the string is: {var} and the second string is:{variable}'
print(my_string)



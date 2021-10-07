def menu():
    print('Select the fruit program')
    print('1:Red Apple')
    print('2:Green Apple')
    print('3:Banana')
menu()
x = int(input('Select an option '))
if x == 1:
    print('You choose the Red Apple')
elif x == 2:
    print('You choose the Green Apple')
elif x == 3:
    print('You choose the Banana')
else:
    print('Your choose is not a menu option')
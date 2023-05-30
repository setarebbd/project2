

print('yek adad bein 01 ta 100 tasavor konid ')
low = 1
high = 100
guess = 50
while True:
    print('guess is:', guess)
    a = input('aya adad shoma bozorgtar az guess hast?(y/n)')
    if a == 'y':
        low = guess+1
        guess = (low+high)//2
    elif a == 'n':
        high = guess-1
        guess = (low+high)//2
    else:
        print('y/n')

    if low == high:
        break
print('wooow adade shoma ', low, ' ast')

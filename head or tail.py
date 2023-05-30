import random
import sys

while True:
    options = [1, 2, 3, 4, 5, 6]
    tas = random.choice(options)
    req = input('do you want try your chance?(y/n)  ')
    if req == 'y':
        print('your chance: ', tas)
    else:
        sys.exit()

import random

def guess(x):
    random_number = random.randint(1,x)
    guess=0
    while guess != random_number:
        if(random_number<10):
           guess=input(f'Gues a number 1 and  {x}: ')
        print(guess)
    else:
        print("sory the number is to long ")

guess(10)

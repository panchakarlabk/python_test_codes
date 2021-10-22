import random
def guess():
    x = 10;
    random_number = random.randint(1,x)
    guess=0
    while guess != random_number:
        x = 10;
        guess = input(f'Please enter any number: ')
        if (x == 1 or x<=10):
         print(guess)
        else:
            print("sory the number os too long ")

guess()

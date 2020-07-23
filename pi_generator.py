#This is a program that generates pi to the nth decimal place where n is an input provided by the user
import requests
import os
import time

def player_input():
    n = 0
    while n==0 or n > 1000:
        try:
            n = int(input('To how many decimal places (less than 1000) do you want to find "Pi" in?: '))
            return n
        except:
            print('Wrong input! enter an integer!')
            continue

def pi_generator(n):
    #generate pi to 'n' decimal places
    print(f'Generating pi to {n} decimal places...')
    r = requests.get(f'https://api.pi.delivery/v1/pi?start=0&numberOfDigits={n}')
    if not r.ok:
        print('Sorry! Server down! Please try again later')
    r_dict= r.json()
    pi = r_dict['content']
    Pi = pi[:1] + '.' + pi[1:]    
    print(Pi)

def play_again():
    while True:
        func = input('Play again? "y" / "n": ').upper()
        if func!= 'Y' and func != 'N':
            print('Wrong input! choose "y" or "n"!')
            continue
        break
    return func== 'Y'


#Pi Generator Program
os.system('cls')

print('Welcome to My Pi Generator Program!')
time.sleep(1)
while True:
    pi_generator(player_input())
    time.sleep(3)
    if play_again():
        continue
    else:
        break
print ("Thanks for using Pi Generator Program")
print("-----------------")
time.sleep(2)
    

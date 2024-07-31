import random as rd
import os

def Createtxt(arquivo, login, counter):
    if os.path.exists(arquivo):
        counter += 1
        arquivo = f'random_password_{counter}.txt'
        Createtxt(arquivo, login, counter)
    else:
        arquivo = open(arquivo, "w")
        arquivo.write(f'login: {login}\npassword: {new_password}')
        arquivo.close()
    

list_char = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm123456789!@#$%&*'
new_password = ''

login = str(input("Seu login: "))

for c in range(0, 10):
    char_password = list_char[rd.randrange(0, len(list_char))]
    new_password = new_password + char_password
print(f'{new_password}')

arquivo = 'random_password.txt'
Createtxt(arquivo, login, 0)